from raptor.core.router import Route

# Define web routes (similar to Laravel's web.php)
web_routes = [
    # Home routes
    Route.get('/', 'HomeController@index').name('home'),
    Route.get('/about', 'HomeController@about').name('about'),
    Route.get('/contact', 'HomeController@contact').name('contact'),
    
    # User management routes
    Route.get('/users', 'UserController@index').name('users.index'),
    Route.get('/users/create', 'UserController@create').name('users.create'),
    Route.post('/users', 'UserController@store').name('users.store'),
    Route.get('/users/{id}', 'UserController@show').name('users.show'),
    Route.get('/users/{id}/edit', 'UserController@edit').name('users.edit'),
    Route.put('/users/{id}', 'UserController@update').name('users.update'),
    Route.delete('/users/{id}', 'UserController@destroy').name('users.destroy'),
    
    # Blog routes (example of nested resources)
    Route.get('/blog', 'BlogController@index').name('blog.index'),
    Route.get('/blog/{slug}', 'BlogController@show').name('blog.show'),
    Route.get('/categories/{category}/posts', 'BlogController@category').name('blog.category'),
]

# Route groups with middleware (Laravel-style)
from raptor.core.router import RouteGroup

# Admin routes with auth middleware
admin_routes = RouteGroup.prefix('/admin').middleware(['auth', 'admin']).group([
    Route.get('/', 'AdminController@dashboard').name('admin.dashboard'),
    Route.get('/users', 'AdminController@users').name('admin.users'),
    Route.get('/settings', 'AdminController@settings').name('admin.settings'),
])

# Combine all web routes
all_web_routes = web_routes + admin_routes