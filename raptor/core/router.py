import re
from typing import List, Dict, Callable, Optional, Any
import importlib

class RouteParameter:
    def __init__(self, name: str, pattern: str = r'[^/]+', optional: bool = False):
        self.name = name
        self.pattern = pattern
        self.optional = optional

class Route:
    def __init__(self, method: str, path: str, action: str):
        self.method = method.upper()
        self.path = path
        self.action = action
        self.route_name = None
        self.middlewares = []
        self.parameters = {}
        self.compiled_pattern = None
        self._compile_pattern()
    
    def _compile_pattern(self):
        """Convert Laravel-style route to regex pattern"""
        pattern = self.path
        
        # Handle {parameter} syntax
        param_pattern = re.compile(r'\{([^}]+)\}')
        params = param_pattern.findall(pattern)
        
        for param in params:
            param_name = param
            param_regex = r'([^/]+)'
            
            # Handle optional parameters {param?}
            if param.endswith('?'):
                param_name = param[:-1]
                param_regex = r'([^/]*)'
                self.parameters[param_name] = RouteParameter(param_name, optional=True)
            else:
                self.parameters[param_name] = RouteParameter(param_name)
            
            # Replace {param} with regex group
            pattern = pattern.replace(f'{{{param}}}', param_regex)
        
        # Escape special regex characters and add anchors
        pattern = '^' + pattern + '$'
        self.compiled_pattern = re.compile(pattern)
    
    def matches(self, method: str, path: str) -> bool:
        """Check if route matches the request"""
        if self.method != method.upper():
            return False
        return bool(self.compiled_pattern.match(path))
    
    def extract_parameters(self, path: str) -> Dict[str, str]:
        """Extract parameters from URL"""
        match = self.compiled_pattern.match(path)
        if not match:
            return {}
        
        params = {}
        param_names = list(self.parameters.keys())
        
        for i, value in enumerate(match.groups()):
            if i < len(param_names):
                params[param_names[i]] = value
        
        return params
    
    def name(self, name: str):
        """Set route name (Laravel-style method chaining)"""
        self.route_name = name
        return self
    
    def middleware(self, middleware: List[str]):
        """Add middleware to route"""
        self.middlewares.extend(middleware if isinstance(middleware, list) else [middleware])
        return self
    
    @staticmethod
    def get(path: str, action: str):
        return Route('GET', path, action)
    
    @staticmethod
    def post(path: str, action: str):
        return Route('POST', path, action)
    
    @staticmethod
    def put(path: str, action: str):
        return Route('PUT', path, action)
    
    @staticmethod
    def patch(path: str, action: str):
        return Route('PATCH', path, action)
    
    @staticmethod
    def delete(path: str, action: str):
        return Route('DELETE', path, action)
    
    @staticmethod
    def options(path: str, action: str):
        return Route('OPTIONS', path, action)

class RouteGroup:
    def __init__(self, prefix: str = '', middleware: List[str] = None):
        self.prefix = prefix.rstrip('/')
        self.middlewares = middleware or []
    
    @staticmethod
    def prefix(prefix: str):
        return RouteGroup(prefix)
    
    def middleware(self, middleware: List[str]):
        self.middlewares = middleware
        return self
    
    def group(self, routes: List[Route]) -> List[Route]:
        """Apply group settings to routes"""
        grouped_routes = []
        
        for route in routes:
            # Apply prefix
            new_path = self.prefix + route.path
            if new_path == '':
                new_path = '/'
            
            # Create new route with modified path
            new_route = Route(route.method, new_path, route.action)
            new_route.route_name = route.route_name
            new_route.middlewares = self.middlewares + route.middlewares
            
            grouped_routes.append(new_route)
        
        return grouped_routes

class Router:
    def __init__(self):
        self.routes: List[Route] = []
        self.named_routes: Dict[str, Route] = {}
        self.controllers = {}
    
    def register_routes(self, routes: List[Route]):
        """Register multiple routes"""
        for route in routes:
            self.add_route(route)
    
    def add_route(self, route: Route):
        """Add a single route"""
        self.routes.append(route)
        
        # Register named route
        if route.route_name:
            self.named_routes[route.route_name] = route
    
    def resolve(self, method: str, path: str) -> Optional[Dict[str, Any]]:
        """Resolve route by method and path"""
        for route in self.routes:
            if route.matches(method, path):
                params = route.extract_parameters(path)
                return {
                    'route': route,
                    'parameters': params,
                    'controller': self._parse_controller_action(route.action),
                    'middlewares': route.middlewares
                }
        return None
    
    def _parse_controller_action(self, action: str) -> Dict[str, str]:
        """Parse Controller@method syntax"""
        if '@' in action:
            controller, method = action.split('@', 1)
            return {
                'controller': controller,
                'method': method
            }
        else:
            # Handle callable or closure
            return {
                'controller': None,
                'method': action
            }
    
    def url(self, name: str, parameters: Dict[str, str] = None) -> str:
        """Generate URL from route name (Laravel-style)"""
        if name not in self.named_routes:
            raise ValueError(f"Route '{name}' not found")
        
        route = self.named_routes[name]
        url = route.path
        
        if parameters:
            for param_name, param_value in parameters.items():
                url = url.replace(f'{{{param_name}}}', str(param_value))
        
        return url
    
    def register_controller(self, name: str, controller_class):
        """Register controller class"""
        self.controllers[name] = controller_class
    
    def load_controllers_from_directory(self, directory: str = 'controllers'):
        """Auto-load controllers from directory"""
        import os
        import importlib
        
        if os.path.exists(directory):
            for file in os.listdir(directory):
                if file.endswith('_controller.py'):
                    module_name = file[:-3]
                    controller_name = module_name.replace('_controller', '')
                    
                    try:
                        module = importlib.import_module(f"{directory}.{module_name}")
                        controller_class = getattr(module, f"{controller_name.capitalize()}Controller")
                        self.register_controller(controller_name, controller_class)
                    except (ImportError, AttributeError) as e:
                        print(f"Warning: Could not load controller {module_name}: {e}")
