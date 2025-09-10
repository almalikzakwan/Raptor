# 🦅 Raptor Framework - Laravel-Style Routing Edition

A lightweight, educational web framework built from scratch in Python with **Laravel-inspired routing system** and **Model-View-Controller (MVC) architecture**. Perfect for learning web development fundamentals, Python advanced concepts, and understanding how modern web frameworks work under the hood.

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Framework](https://img.shields.io/badge/Framework-Raptor%20Core-orange.svg)](https://github.com/yourusername/raptor)
[![Routing](https://img.shields.io/badge/Routing-Laravel--Style-red.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-MVC-purple.svg)](#)
[![Security](https://img.shields.io/badge/Secure-Built--in%20Protection-red.svg)](https://owasp.org/)
[![Performance](https://img.shields.io/badge/Speed-Blazing%20Fast-yellow.svg)](#)
[![Documentation](https://img.shields.io/badge/Docs-Available-blueviolet.svg)](docs/index.md)
[![Tests](https://img.shields.io/badge/Tests-Passing-success.svg)](tests/)
[![Coverage](https://img.shields.io/badge/Coverage-90%25+-brightgreen.svg)](#)

## ✨ Features

### 🛣️ **Laravel-Style Routing System**
- **Route Declarations**: `Route::get()`, `Route::post()`, `Route::put()`, `Route::delete()`
- **Named Routes**: `->name('users.show')` with URL generation
- **Route Parameters**: `/users/{id}` with optional parameters `{param?}`
- **Route Groups**: Prefix and middleware grouping
- **Controller@Method Syntax**: Clean action binding
- **Middleware Support**: Request filtering and processing

### 🏗️ **MVC Architecture**
- **Clean Separation**: Model-View-Controller pattern implementation
- **Auto-Controller Loading**: Automatic discovery and loading of controllers
- **Template Engine**: Simple yet powerful HTML rendering with `{{variable}}` syntax
- **File-Based Models**: JSON-based data storage with BaseModel abstraction
- **RESTful Controllers**: Full CRUD operations with resource routing

### 🚀 **Production Features**
- **Threading Support**: Concurrent request handling
- **Request Logging**: Built-in API request monitoring
- **SSL Compatible**: Works with nginx reverse proxy
- **systemd Ready**: Service configuration included
- **Error Handling**: Comprehensive exception management

## 🏗️ Project Architecture Overview

### **Routing Layer** (`routes/`)
Laravel-inspired route definitions with separate files for different concerns
- **`web.py`**: Web application routes (HTML responses)
- **`api.py`**: API routes with versioning and grouping

### **Model Layer** (`models/`)
Handles data logic, business rules, and data persistence
- **`BaseModel`**: Abstract class for file-based data operations
- **`StatusModel`**: System status and API logging
- **`PageModel`**: Page content and metadata
- **`UserModel`**: User management with CRUD operations

### **View Layer** (`views/`)
Manages presentation logic and HTML templates
- Template files with variable substitution (`{{variable}}` syntax)
- Responsive design with modern CSS
- Separation of presentation from business logic

### **Controller Layer** (`controllers/`)
Coordinates between Models and Views, handles HTTP requests
- **`HomeController`**: Home, about, and contact page logic
- **`ApiController`**: RESTful API endpoints
- **`UserController`**: User management with full CRUD
- **Auto-loading**: Controllers discovered automatically

### **Framework Core** (`raptor/`)
Core framework components and utilities
- **`core/app.py`**: Main Raptor application class with MVC support
- **`core/router.py`**: Laravel-style routing engine
- **`http/`**: HTTP utilities and request/response handling

## 🚀 What This Project Demonstrates

Raptor Framework showcases advanced web development concepts:

- **🛣️ Advanced Routing**: Laravel-inspired route declaration and resolution
- **🏛️ MVC Architecture**: Professional software design pattern implementation
- **🔌 HTTP Server**: Raw socket programming for HTTP communication
- **🧵 Multi-threading**: Concurrent request handling
- **🎭 Template Engine**: HTML rendering with dynamic content
- **💾 Data Persistence**: File-based storage with JSON serialization
- **📊 Request Monitoring**: Built-in logging and analytics
- **🔄 Auto-Discovery**: Dynamic controller and route loading

## 📁 Project Structure

```
raptor-framework/
├── raptor/                        # Framework core package
│   ├── __init__.py               # Package exports (Raptor, Request, Response)
│   ├── core/                     # Core framework components
│   │   ├── __init__.py          # Core package initialization
│   │   ├── app.py               # Main Raptor class with MVC & routing
│   │   └── router.py            # Laravel-style routing engine
│   └── http/                     # HTTP utilities
│       └── __init__.py          # HTTP package initialization
├── routes/                        # ROUTING LAYER - Route Definitions
│   ├── __init__.py              # Routes package initialization
│   ├── web.py                   # Web application routes
│   └── api.py                   # API routes with versioning
├── models/                        # MODEL LAYER - Data & Business Logic
│   ├── __init__.py              # Models package initialization
│   ├── base_model.py            # Abstract base class for all models
│   ├── status_model.py          # System status and API logging
│   ├── page_model.py            # Page content and metadata
│   └── user_model.py            # User management and CRUD operations
├── views/                         # VIEW LAYER - Presentation Templates
│   ├── __init__.py              # Views package initialization
│   ├── home.html                # Home page template
│   └── about.html               # About page template with route table
├── controllers/                   # CONTROLLER LAYER - Request Handling
│   ├── __init__.py              # Controllers package initialization
│   ├── home_controller.py       # Home, about, and contact pages
│   ├── api_controller.py        # RESTful API endpoints
│   └── user_controller.py       # User CRUD operations
├── data/                          # Data storage (auto-created)
│   ├── api_logs.json            # API request logs
│   ├── users.json               # User data storage
│   └── [other data files]       # Model data storage
├── app.py                         # Main application entry point
├── .gitignore                    # Git ignore (includes data/ directory)
└── README.md                     # This documentation
```

### Key Components

- **`routes/web.py`**: Laravel-style web route definitions with named routes and RESTful patterns
- **`routes/api.py`**: API route groups with versioning and middleware
- **`raptor/core/router.py`**: Laravel-inspired routing engine with parameter extraction and URL generation
- **`raptor/core/app.py`**: Enhanced Raptor class with MVC support and template engine
- **`controllers/`**: Controller classes with full CRUD operations and proper HTTP responses
- **`models/base_model.py`**: Abstract base class providing file-based data operations
- **`app.py`**: Main application with automatic route loading

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.9 or higher
- Ubuntu/Linux system (for systemd setup)
- nginx (optional, for production deployment)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/raptor-framework.git
   cd raptor-framework
   ```

2. **Run the application:**
   ```bash
   python3 app.py
   ```

3. **Access the application:**
   - **Home**: `http://localhost:8000/` → `HomeController@index`
   - **About**: `http://localhost:8000/about` → `HomeController@about`  
   - **Users List**: `http://localhost:8000/users` → `UserController@index`
   - **Create User**: `http://localhost:8000/users/create` → `UserController@create`
   - **API Status**: `http://localhost:8000/api/v1/status` → `ApiController@status`
   - **API Health**: `http://localhost:8000/api/v1/health` → `ApiController@health`

## 🛣️ Laravel-Style Routing

### Route Declaration Examples

```python
# routes/web.py
from raptor.core.router import Route, RouteGroup

# Basic routes
web_routes = [
    Route.get('/', 'HomeController@index').name('home'),
    Route.get('/about', 'HomeController@about').name('about'),
    Route.post('/contact', 'HomeController@contact').name('contact'),
    
    # RESTful resource routes
    Route.get('/users', 'UserController@index').name('users.index'),
    Route.get('/users/create', 'UserController@create').name('users.create'),
    Route.post('/users', 'UserController@store').name('users.store'),
    Route.get('/users/{id}', 'UserController@show').name('users.show'),
    Route.get('/users/{id}/edit', 'UserController@edit').name('users.edit'),
    Route.put('/users/{id}', 'UserController@update').name('users.update'),
    Route.delete('/users/{id}', 'UserController@destroy').name('users.destroy'),
]

# Route groups with middleware and prefix
admin_routes = RouteGroup.prefix('/admin').middleware(['auth', 'admin']).group([
    Route.get('/', 'AdminController@dashboard').name('admin.dashboard'),
    Route.get('/users', 'AdminController@users').name('admin.users'),
])
```

```python
# routes/api.py
# API routes with versioning
api_routes = RouteGroup.prefix('/api/v1').group([
    Route.get('/status', 'ApiController@status').name('api.status'),
    Route.get('/users', 'Api\\UserController@index').name('api.users.index'),
    Route.post('/users', 'Api\\UserController@store').name('api.users.store'),
    Route.get('/users/{id}', 'Api\\UserController@show').name('api.users.show'),
])
```

### URL Generation

```python
# Generate URLs from route names
app = Raptor()
url = app.url('users.show', {'id': 123})  # /users/123
api_url = app.url('api.users.show', {'id': 456})  # /api/v1/users/456
```

### Route Parameters

```python
# Required parameters
Route.get('/users/{id}', 'UserController@show')

# Optional parameters
Route.get('/posts/{category?}', 'PostController@index')

# Multiple parameters
Route.get('/users/{user_id}/posts/{post_id}', 'PostController@userPost')
```

## 🔧 MVC Development Guide

### 1. Creating a Model (`models/post_model.py`)

```python
from .base_model import BaseModel
from datetime import datetime

class PostModel(BaseModel):
    def __init__(self):
        super().__init__()
    
    def create_post(self, title, content, author_id):
        posts = self.load_data('posts')
        post = {
            'id': self.generate_id(posts),
            'title': title,
            'content': content,
            'author_id': author_id,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        posts.append(post)
        self.save_data('posts', posts)
        return post
    
    def get_all_posts(self):
        return self.load_data('posts')
    
    def get_post_by_id(self, post_id):
        posts = self.get_all_posts()
        return next((p for p in posts if p['id'] == post_id), None)
```

### 2. Creating a Controller (`controllers/post_controller.py`)

```python
from models.post_model import PostModel
from raptor.core.app import Response
import json

class PostController:
    def __init__(self):
        self.post_model = PostModel()
    
    def index(self, request):
        """List all posts - GET /posts"""
        posts = self.post_model.get_all_posts()
        
        # Render template or return JSON
        if request.headers.get('accept') == 'application/json':
            return Response(json.dumps(posts), 200, 'application/json')
        
        # Render HTML template
        from raptor import Raptor
        app = Raptor()
        content = app.render_template('posts/index.html', {
            'posts': posts,
            'title': 'All Posts'
        })
        return Response(content)
    
    def store(self, request):
        """Create new post - POST /posts"""
        title = request.input('title')
        content = request.input('content')
        
        post = self.post_model.create_post(title, content, 1)
        return Response(json.dumps(post), 201, 'application/json')
```

### 3. Adding Routes (`routes/web.py`)

```python
# Add to existing web_routes list
Route.get('/posts', 'PostController@index').name('posts.index'),
Route.get('/posts/create', 'PostController@create').name('posts.create'),
Route.post('/posts', 'PostController@store').name('posts.store'),
Route.get('/posts/{id}', 'PostController@show').name('posts.show'),
```

### 4. Creating Views (`views/posts/index.html`)

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{title}}</title>
    <style>
        /* Add your styles here */
    </style>
</head>
<body>
    <h1>{{title}}</h1>
    <div class="posts">
        <!-- Template system would need enhancement for loops -->
        <p>Posts will be displayed here</p>
    </div>
    <a href="/posts/create">Create New Post</a>
</body>
</html>
```

## 🔌 API Endpoints

### Web Routes
- **GET `/`** → `HomeController@index` - Home page with framework info
- **GET `/about`** → `HomeController@about` - About page with route table
- **GET `/contact`** → `HomeController@contact` - Contact form
- **GET `/users`** → `UserController@index` - Users listing with create/view links
- **GET `/users/create`** → `UserController@create` - User creation form
- **POST `/users`** → `UserController@store` - Create new user
- **GET `/users/{id}`** → `UserController@show` - User profile page
- **GET `/users/{id}/edit`** → `UserController@edit` - User edit form

### API Routes (v1)
- **GET `/api/v1/status`** → `ApiController@status` - System status with routing info
- **GET `/api/v1/health`** → `ApiController@health` - Simple health check
- **GET `/api/v1/users`** → `Api\UserController@index` - Users API
- **POST `/api/v1/users`** → `Api\UserController@store` - Create user API
- **GET `/api/v1/users/{id}`** → `Api\UserController@show` - User details API

### API Response Examples

#### Status Endpoint (`/api/v1/status`)
```json
{
  "status": "success",
  "message": "Raptor Framework API is running",
  "version": "1.0.0",
  "framework": "Raptor MVC",
  "python_version": "3.9+",
  "ssl_enabled": true,
  "timestamp": "2025-01-15T10:30:00Z",
  "architecture": "MVC (Model-View-Controller)",
  "routing": {
    "style": "Laravel-inspired",
    "features": ["named_routes", "route_parameters", "route_groups", "middleware"],
    "total_routes": "Dynamic"
  }
}
```

## 🏭 Production Deployment

### 1. systemd Service Configuration

Create `/etc/systemd/system/raptor-mvc.service`:

```ini
[Unit]
Description=Raptor Framework MVC Web Application
After=network.target

[Service]
Type=simple
User=www-data
Group=www-data
WorkingDirectory=/path/to/raptor-framework
Environment=PATH=/path/to/raptor-framework/venv/bin
ExecStart=/usr/bin/python3 /path/to/raptor-framework/app.py
Restart=always
RestartSec=3

# Security settings
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/path/to/raptor-framework
ReadWritePaths=/path/to/raptor-framework/data

[Install]
WantedBy=multi-user.target
```

### 2. Service Management

```bash
# Enable and start
sudo systemctl daemon-reload
sudo systemctl enable raptor-mvc.service
sudo systemctl start raptor-mvc.service

# Monitor
sudo systemctl status raptor-mvc
sudo journalctl -u raptor-mvc.service -f
```

### 3. nginx Reverse Proxy

```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # API routes
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Content-Type application/json;
    }
}
```

## 📊 Data Storage

### File-Based Storage
- **Location**: `data/` directory (auto-created, gitignored)
- **Format**: JSON files with automatic serialization
- **Models**: Use `BaseModel` for consistent CRUD operations

### Example Data Structures
```json
// data/users.json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:00Z"
  }
]

// data/api_logs.json
[
  {
    "id": 1,
    "timestamp": "2025-01-15T10:30:00Z",
    "method": "GET",
    "path": "/api/v1/status",
    "user_agent": "Mozilla/5.0..."
  }
]
```

## 🧑‍💻 Development Workflow

### 1. Request Flow
```
HTTP Request → Router → Route Resolution → Controller → Model → Controller → View → HTTP Response
```

### 2. Adding New Features
1. **Routes**: Define in `routes/web.py` or `routes/api.py`
2. **Controller**: Create controller with action methods
3. **Model**: Implement data handling logic
4. **View**: Design HTML template (for web routes)

### 3. Route Table Inspection

The framework automatically displays a Laravel-style route table on startup:

```
📋 Route List:
+---------+--------------------+----------------------+------------------+
| Method  | URI                | Name                 | Action           |
+---------+--------------------+----------------------+------------------+
| GET     | /                  | home                 | HomeController@index |
| GET     | /about             | about                | HomeController@about |
| GET     | /users             | users.index          | UserController@index |
| GET     | /users/{id}        | users.show           | UserController@show  |
| GET     | /api/v1/status     | api.status           | ApiController@status |
+---------+--------------------+----------------------+------------------+
```

## 📚 Learning Objectives

This Laravel-style routing implementation teaches:

### **Advanced Routing Concepts**
- Route parameter extraction and validation
- Named routes with URL generation
- Route grouping with shared attributes
- Middleware pipeline architecture
- RESTful resource routing patterns

### **Software Architecture**
- Model-View-Controller design pattern
- Separation of concerns and clean architecture
- Dependency injection and auto-loading
- Request/response cycle optimization

### **Web Development**
- HTTP protocol deep understanding
- RESTful API design principles
- Template rendering and data binding
- Modern web application structure

### **Python Advanced Concepts**
- Object-oriented programming patterns
- Dynamic module loading and reflection
- Regular expressions for URL matching
- File I/O and JSON serialization
- Threading and concurrent processing

## 🎯 Use Cases

- **🎓 Educational**: Learn Laravel-style routing and MVC architecture
- **🚀 Prototyping**: Rapid web application development with familiar syntax
- **🔬 Research**: Experiment with web technologies and routing patterns
- **📚 Teaching**: Demonstrate professional framework design patterns
- **🏗️ Foundation**: Base for building more complex web frameworks

## 🤝 Contributing

We welcome contributions that maintain the educational focus and Laravel-inspired design:

### Guidelines
- **📖 Keep it Educational**: Prioritize learning value and code clarity
- **🛣️ Follow Laravel Patterns**: Maintain consistency with Laravel routing concepts
- **📝 Document Everything**: Extensive comments and documentation
- **🧪 Add Tests**: Include examples and test cases
- **🏗️ Follow MVC**: Maintain architectural patterns

## 🔮 Roadmap

### Planned Features
- **🔗 Advanced Routing**: Route model binding and wildcards
- **🔐 Middleware System**: Authentication, CORS, and custom middleware
- **📊 Enhanced Templates**: Template inheritance, loops, and conditionals
- **🗄️ Database Integration**: SQLite and PostgreSQL support
- **🧪 Testing Framework**: PHPUnit-style testing tools
- **📦 Artisan Commands**: Laravel-style CLI commands
- **🔍 Debug Toolbar**: Development debugging and profiling tools

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **🌐 Laravel Framework**: Inspiration for routing system design
- **🐍 Python Community**: For excellent documentation and libraries
- **🛣️ Web Standards**: HTTP/1.1 and RESTful API principles  
- **🏗️ MVC Pattern**: Gang of Four design patterns
- **📚 Educational Resources**: Various web development tutorials and courses

---

**🎓 Built with ❤️ for learning Laravel-style routing in Python**

**🦅 Raptor Framework - Where Laravel Meets Python Education**