#!/usr/bin/env python3
from raptor import Raptor

# Create application instance
app = Raptor()

# Register custom middleware (optional)
# app.register_middleware('auth', AuthMiddleware)
# app.register_middleware('cors', CorsMiddleware)

if __name__ == '__main__':
    print("🦅 Starting Raptor Framework - Laravel-style Routing Edition")
    print("Architecture Features:")
    print("  🛣️  Laravel-style Route Declaration")
    print("  📂 Separate Route Files (web.py, api.py)")
    print("  🏗️  MVC (Model-View-Controller) Pattern")
    print("  🎯 Named Routes with URL Generation")
    print("  🔗 Route Parameters and Groups")
    print("  🛡️  Middleware Support")
    print("  📍 Auto-Controller Loading")
    print("  💾 File-based Data Storage")
    
    print("\nRouting Features:")
    print("  • Route::get(), Route::post(), Route::put(), Route::delete()")
    print("  • Route parameters: /users/{id}")
    print("  • Named routes: ->name('users.show')")
    print("  • Route groups with prefix and middleware")
    print("  • URL generation: app.url('users.show', {'id': 1})")
    print("  • Controller@method syntax")
    print("  • Namespaced controllers: Api\\UserController")
    
    # Run the application
    app.run(host='0.0.0.0', port=8000)