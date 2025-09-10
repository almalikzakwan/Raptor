import socket
import threading
from urllib.parse import parse_qs, urlparse
import json
import importlib
import os
from typing import Dict  # Add this import
from .router import Router, Route

class Request:
    def __init__(self, method, path, headers=None, body=None):
        self.method = method
        self.path = path
        self.headers = headers or {}
        self.body = body
        self.params = {}  # URL parameters from route
        self.query = {}   # Query string parameters
        
        # Parse query parameters
        parsed_url = urlparse(path)
        self.path_info = parsed_url.path
        self.query = parse_qs(parsed_url.query)
        
    def input(self, key: str, default=None):
        """Get input from query or body (Laravel-style)"""
        # First check query parameters
        if key in self.query:
            value = self.query[key]
            return value[0] if isinstance(value, list) and len(value) > 0 else value
        
        # Then check URL parameters
        if key in self.params:
            return self.params[key]
        
        # TODO: Parse body for POST data
        return default

class Response:
    def __init__(self, content="", status=200, content_type='text/html', headers=None):
        self.content = content
        self.status = status
        self.content_type = content_type
        self.headers = headers or {}

class Raptor:
    def __init__(self):
        self.router = Router()
        self.host = '127.0.0.1'
        self.port = 8000
        self.middleware_stack = []
    
    def load_routes(self):
        """Load routes from routes directory"""
        try:
            # Load web routes
            from routes.web import all_web_routes
            self.router.register_routes(all_web_routes)
            print(f"📍 Loaded {len(all_web_routes)} web routes")
        except ImportError as e:
            print(f"Warning: Could not load web routes: {e}")
        
        try:
            # Load API routes
            from routes.api import all_api_routes
            self.router.register_routes(all_api_routes)
            print(f"🔌 Loaded {len(all_api_routes)} API routes")
        except ImportError as e:
            print(f"Warning: Could not load API routes: {e}")
    
    def register_middleware(self, name: str, middleware_class):
        """Register middleware"""
        self.middleware_stack.append({'name': name, 'class': middleware_class})
    
    def response(self, content, status=200, content_type='text/html'):
        """Generate HTTP response"""
        status_text = {200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'}.get(status, 'Unknown')
        headers = f"HTTP/1.1 {status} {status_text}\r\n"
        headers += f"Content-Type: {content_type}\r\n"
        headers += f"Content-Length: {len(content.encode())}\r\n"
        headers += "Connection: close\r\n\r\n"
        return headers.encode() + content.encode()
    
    def json(self, data, status=200):
        """JSON response helper"""
        content = json.dumps(data, indent=2)
        return self.response(content, status, 'application/json')
    
    def render_template(self, template_name, context=None):
        """Simple template rendering"""
        try:
            template_path = os.path.join('views', template_name)
            with open(template_path, 'r') as file:
                template_content = file.read()
                
            if context:
                for key, value in context.items():
                    template_content = template_content.replace(f"{{{{{key}}}}}", str(value))
                    
            return template_content
        except FileNotFoundError:
            return f"<h1>Template {template_name} not found</h1>"
    
    def url(self, name: str, parameters: Dict[str, str] = None) -> str:
        """Generate URL from route name"""
        return self.router.url(name, parameters)
    
    def handle_request(self, client_socket):
        try:
            request_data = client_socket.recv(1024).decode()
            lines = request_data.split('\r\n')
            
            if lines:
                method, path, _ = lines[0].split(' ')
                
                # Parse headers
                headers = {}
                body = ""
                header_section = True
                
                for line in lines[1:]:
                    if line == "" and header_section:
                        header_section = False
                        continue
                    if header_section and ':' in line:
                        key, value = line.split(':', 1)
                        headers[key.strip().lower()] = value.strip()
                    elif not header_section:
                        body += line
                
                # Create request object
                request = Request(method, path, headers, body)
                
                # Resolve route
                route_result = self.router.resolve(method, path)
                
                if route_result:
                    route = route_result['route']
                    request.params = route_result['parameters']
                    controller_info = route_result['controller']
                    
                    # Get controller and method
                    controller_name = controller_info['controller']
                    method_name = controller_info['method']
                    
                    if controller_name:
                        # Load controller
                        controller_instance = self._load_controller(controller_name)
                        if controller_instance:
                            response = getattr(controller_instance, method_name)(request)
                        else:
                            response = Response("Controller not found", 404)
                    else:
                        # Handle callable/closure
                        response = Response("Direct callable not implemented", 500)
                    
                    # Send response
                    if isinstance(response, Response):
                        client_socket.send(self.response(response.content, response.status, response.content_type))
                    elif isinstance(response, bytes):
                        client_socket.send(response)
                    else:
                        client_socket.send(self.response(str(response)))
                else:
                    client_socket.send(self.response("404 - Route Not Found", 404))
                    
        except Exception as e:
            error_response = f"500 - Internal Server Error: {str(e)}"
            client_socket.send(self.response(error_response, 500))
        finally:
            client_socket.close()
    
    def _load_controller(self, controller_name: str):
        """Load controller instance"""
        try:
            # Handle namespaced controllers (Api\\UserController)
            if '\\\\' in controller_name:
                namespace, class_name = controller_name.split('\\\\', 1)
                module_path = f"controllers.{namespace.lower()}.{self._snake_case(class_name)}"
            else:
                class_name = controller_name
                module_path = f"controllers.{self._snake_case(class_name)}"
            
            module = importlib.import_module(module_path)
            controller_class = getattr(module, class_name)
            return controller_class()
            
        except (ImportError, AttributeError) as e:
            print(f"Error loading controller {controller_name}: {e}")
            return None
    
    def _snake_case(self, name: str) -> str:
        """Convert CamelCase to snake_case"""
        import re
        return re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name).lower()
    
    def run(self, host='127.0.0.1', port=8000):
        self.host = host
        self.port = port
        
        # Load routes and controllers
        self.load_routes()
        self.router.load_controllers_from_directory()
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)
        
        print(f"🦅 Raptor server running on http://{host}:{port}")
        print(f"📍 Total routes registered: {len(self.router.routes)}")
        print(f"🎯 Named routes: {len(self.router.named_routes)}")
        
        # Print route table
        self._print_route_table()
        
        try:
            while True:
                client_socket, addr = server_socket.accept()
                client_thread = threading.Thread(target=self.handle_request, args=(client_socket,))
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            print("\nShutting down server...")
        finally:
            server_socket.close()
    
    def _print_route_table(self):
        """Print Laravel-style route table"""
        print("\n📋 Route List:")
        print("+---------+--------------------+----------------------+------------------+")
        print("| Method  | URI                | Name                 | Action           |")
        print("+---------+--------------------+----------------------+------------------+")
        
        for route in self.router.routes:
            method = route.method.ljust(7)
            uri = route.path.ljust(18)
            name = (route.route_name or '').ljust(20)
            action = route.action.ljust(16)
            print(f"| {method} | {uri} | {name} | {action} |")
        
        print("+---------+--------------------+----------------------+------------------+\n")