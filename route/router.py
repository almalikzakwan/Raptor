import importlib
from functools import wraps
from flask import Flask

class Route:
    _app = None
    _active_middlewares = []

    @classmethod
    def init_app(cls, app: Flask):
        cls._app = app

    @classmethod
    def middleware(cls, *names):
        return RouteGroup(names)

    @classmethod
    def _resolve_view(cls, action_or_view):
        """
        Resolves a view function or controller action into a callable Flask view function.
        Supports:
          1. Standard Python function: home_view
          2. Array notation: [HomeController, 'index']
          3. String notation: 'app.controllers.home_controller.HomeController@index'
        """
        # Resolve Array notation [HomeController, 'index']
        if isinstance(action_or_view, (list, tuple)) and len(action_or_view) == 2:
            controller_cls, method_name = action_or_view
            def view_wrapper(*args, **kwargs):
                controller_instance = controller_cls()
                method = getattr(controller_instance, method_name)
                return method(*args, **kwargs)
            # Give the wrapper a unique __name__ for Flask registry
            view_wrapper.__name__ = f"{controller_cls.__name__}_{method_name}"
            return view_wrapper

        # Resolve String notation 'app.controllers.home_controller.HomeController@index'
        elif isinstance(action_or_view, str) and '@' in action_or_view:
            module_class_path, method_name = action_or_view.split('@')
            module_path, class_name = module_class_path.rsplit('.', 1)
            
            # Dynamically import controller module and get class
            module = importlib.import_module(module_path)
            controller_cls = getattr(module, class_name)
            
            def view_wrapper(*args, **kwargs):
                controller_instance = controller_cls()
                method = getattr(controller_instance, method_name)
                return method(*args, **kwargs)
                
            view_wrapper.__name__ = f"{class_name}_{method_name}"
            return view_wrapper

        return action_or_view

    @classmethod
    def _apply_middlewares(cls, view_func, middlewares):
        wrapped = view_func
        # Apply middlewares in reverse registration order
        for middleware_name in reversed(middlewares):
            from middleware.kernel import route_middleware
            middleware_cls = route_middleware.get(middleware_name)
            if middleware_cls:
                def make_wrapper(current_wrapped, m_cls):
                    @wraps(current_wrapped)
                    def wrapper(*args, **kwargs):
                        response = m_cls().handle()
                        if response is not None:
                            return response
                        return current_wrapped(*args, **kwargs)
                    return wrapper
                wrapped = make_wrapper(wrapped, middleware_cls)
        return wrapped

    @classmethod
    def get(cls, rule, view_func, **options):
        resolved_view = cls._resolve_view(view_func)
        middlewares = list(cls._active_middlewares)
        wrapped_view = cls._apply_middlewares(resolved_view, middlewares)
        options.setdefault('methods', ['GET'])
        endpoint = options.pop('endpoint', resolved_view.__name__)
        cls._app.add_url_rule(rule, endpoint, wrapped_view, **options)
        return view_func

    @classmethod
    def post(cls, rule, view_func, **options):
        resolved_view = cls._resolve_view(view_func)
        middlewares = list(cls._active_middlewares)
        wrapped_view = cls._apply_middlewares(resolved_view, middlewares)
        options.setdefault('methods', ['POST'])
        endpoint = options.pop('endpoint', resolved_view.__name__)
        cls._app.add_url_rule(rule, endpoint, wrapped_view, **options)
        return view_func


class RouteGroup:
    def __init__(self, middlewares):
        self.middlewares = middlewares

    def __enter__(self):
        Route._active_middlewares.extend(self.middlewares)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for _ in self.middlewares:
            if Route._active_middlewares:
                Route._active_middlewares.pop()

    def group(self, callback):
        with self:
            callback()
        return self

    def get(self, rule, view_func, **options):
        with self:
            Route.get(rule, view_func, **options)
        return self

    def post(self, rule, view_func, **options):
        with self:
            Route.post(rule, view_func, **options)
        return self
