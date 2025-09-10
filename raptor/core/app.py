import socket
import threading
from urllib.parse import parse_qs, urlparse
import json

class Raptor:
    def __init__(self):
        self.routes = {}
        self.host = '127.0.0.1'
        self.port = 8000
    
    def route(self, path, methods=['GET']):
        def decorator(func):
            for method in methods:
                route_key = f"{method}:{path}"
                self.routes[route_key] = func
            return func
        return decorator
    
    def response(self, content, status=200, content_type='text/html'):
        status_text = {200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'}.get(status, 'Unknown')
        headers = f"HTTP/1.1 {status} {status_text}\r\n"
        headers += f"Content-Type: {content_type}\r\n"
        headers += f"Content-Length: {len(content.encode())}\r\n"
        headers += "Connection: close\r\n\r\n"
        return headers.encode() + content.encode()
    
    def json(self, data, status=200):
        content = json.dumps(data)
        return self.response(content, status, 'application/json')
    
    def handle_request(self, client_socket):
        try:
            request = client_socket.recv(1024).decode()
            lines = request.split('\r\n')
            if lines:
                method, path, _ = lines[0].split(' ')
                route_key = f"{method}:{path}"
                
                if route_key in self.routes:
                    # Simple request object
                    class Request:
                        def __init__(self, method, path):
                            self.method = method
                            self.path = path
                    
                    response = self.routes[route_key](Request(method, path))
                    if isinstance(response, bytes):
                        client_socket.send(response)
                    else:
                        client_socket.send(self.response(str(response)))
                else:
                    client_socket.send(self.response("404 - Not Found", 404))
        except Exception as e:
            client_socket.send(self.response(f"500 - Internal Server Error: {str(e)}", 500))
        finally:
            client_socket.close()
    
    def run(self, host='127.0.0.1', port=8000):
        self.host = host
        self.port = port
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)
        
        print(f"🦅 Raptor server running on http://{host}:{port}")
        
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