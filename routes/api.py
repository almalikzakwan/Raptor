from raptor.core.router import Route, RouteGroup

# API routes (similar to Laravel's api.php)
api_routes = RouteGroup.prefix('/api/v1').group([
    # System routes
    Route.get('/status', 'ApiController@status').name('api.status'),
    Route.get('/health', 'ApiController@health').name('api.health'),
    
    # User API routes
    Route.get('/users', 'Api\\UserController@index').name('api.users.index'),
    Route.post('/users', 'Api\\UserController@store').name('api.users.store'),
    Route.get('/users/{id}', 'Api\\UserController@show').name('api.users.show'),
    Route.put('/users/{id}', 'Api\\UserController@update').name('api.users.update'),
    Route.delete('/users/{id}', 'Api\\UserController@destroy').name('api.users.destroy'),
    
    # Blog API routes
    Route.get('/posts', 'Api\\PostController@index').name('api.posts.index'),
    Route.post('/posts', 'Api\\PostController@store').name('api.posts.store'),
    Route.get('/posts/{id}', 'Api\\PostController@show').name('api.posts.show'),
])

# Protected API routes (with auth middleware)
protected_api_routes = RouteGroup.prefix('/api/v1').middleware(['auth:api']).group([
    Route.post('/logout', 'Api\\AuthController@logout').name('api.logout'),
    Route.get('/me', 'Api\\UserController@me').name('api.me'),
    Route.put('/profile', 'Api\\UserController@updateProfile').name('api.profile.update'),
])

# Combine all API routes
all_api_routes = api_routes + protected_api_routes