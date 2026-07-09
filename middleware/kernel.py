from middleware.auth import Authenticate

# Register middleware follow with alias name (like Kernel.php in Laravel).
route_middleware = {
    'auth': Authenticate,
}
