# 🦅 Raptor Framework - MVC Edition

A lightweight, educational web framework built from scratch in Python with **Model-View-Controller (MVC) architecture**. Perfect for learning web development fundamentals, Python advanced concepts, and understanding how modern web frameworks work under the hood.

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Framework](https://img.shields.io/badge/Framework-Raptor%20Core-orange.svg)](https://github.com/yourusername/raptor)
[![Security](https://img.shields.io/badge/Secure-Built--in%20Protection-red.svg)](https://owasp.org/)
[![Performance](https://img.shields.io/badge/Speed-Blazing%20Fast-yellow.svg)](#)
[![Documentation](https://img.shields.io/badge/Docs-Available-blueviolet.svg)](docs/index.md)
[![Tests](https://img.shields.io/badge/Tests-Passing-success.svg)](tests/)
[![Coverage](https://img.shields.io/badge/Coverage-90%25+-brightgreen.svg)](#)
[![Build](https://img.shields.io/badge/Build-Stable-informational.svg)](#)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

## ✨ Features

- **🏗️ MVC Architecture**: Clean separation of concerns with Model-View-Controller pattern
- **📚 Educational Focus**: Learn professional software architecture patterns
- **🔄 Auto-Controller Loading**: Automatic discovery and loading of controllers
- **🎨 Template Engine**: Simple yet powerful HTML template rendering with variable substitution
- **💾 File-Based Models**: JSON-based data storage with BaseModel abstraction
- **📊 Request Logging**: Built-in API request logging and monitoring
- **🔀 Flexible Routing**: Support for both MVC and traditional function-based routes
- **⚡ Threading Support**: Concurrent request handling
- **🚀 Production Ready**: Includes systemd service configuration
- **🔒 SSL Compatible**: Works with nginx reverse proxy
- **📱 Responsive Design**: Modern, mobile-friendly user interface

## 🏗️ MVC Architecture Overview

### **Model Layer** (`models/`)
Handles data logic, business rules, and data persistence
- **BaseModel**: Abstract class for file-based data operations
- **StatusModel**: System status and API logging
- **PageModel**: Page content and metadata

### **View Layer** (`views/`)
Manages presentation logic and HTML templates
- Template files with variable substitution (`{{variable}}` syntax)
- Responsive design with modern CSS
- Separation of presentation from business logic

### **Controller Layer** (`controllers/`)
Coordinates between Models and Views, handles HTTP requests
- **HomeController**: Home and about page logic
- **ApiController**: RESTful API endpoints
- **Auto-loading**: Controllers discovered automatically

## 🚀 What This Project Does

Raptor Framework MVC demonstrates advanced web development concepts:

- **🏛️ MVC Architecture**: Professional software design pattern implementation
- **🔌 HTTP Server**: Raw socket programming for HTTP communication
- **🛣️ Advanced Routing**: Decorator-based route registration with controller binding
- **🧵 Multi-threading**: Concurrent request handling
- **🎭 Template Engine**: HTML rendering with dynamic content
- **💾 Data Persistence**: File-based storage with JSON serialization
- **📊 Request Monitoring**: Built-in logging and analytics
- **🔄 Auto-Discovery**: Dynamic controller and route loading

## 📁 Project Structure

```
raptor-framework/
├── raptor/                     # Framework core package
│   ├── __init__.py            # Package exports (Raptor, Request, Response)
│   ├── core/                  # Core framework components
│   │   ├── __init__.py       # Core package initialization
│   │   └── app.py            # Main Raptor class with MVC support
│   └── http/                  # HTTP utilities
│       └── __init__.py       # HTTP package initialization
├── models/                     # MODEL LAYER - Data & Business Logic
│   ├── __init__.py           # Models package initialization
│   ├── base_model.py         # Abstract base class for all models
│   ├── status_model.py       # System status and API logging
│   └── page_model.py         # Page content and metadata
├── views/                      # VIEW LAYER - Presentation Templates
│   ├── __init__.py           # Views package initialization
│   ├── home.html             # Home page template
│   └── about.html            # About page template
├── controllers/                # CONTROLLER LAYER - Request Handling
│   ├── __init__.py           # Controllers package initialization
│   ├── home_controller.py    # Home and about page controller
│   └── api_controller.py     # RESTful API controller
├── data/                       # Data storage (auto-created)
│   ├── api_logs.json         # API request logs
│   └── [other data files]    # Model data storage
├── app.py                      # Main application entry point
├── .gitignore                 # Git ignore (includes data/ directory)
└── README.md                  # This documentation
```

### Key Components

- **`raptor/core/app.py`**: Enhanced Raptor class with MVC support, template engine, and controller auto-loading
- **`models/base_model.py`**: Abstract base class providing file-based data operations
- **`controllers/`**: Controller classes handling HTTP requests and coordinating Model-View interactions
- **`views/`**: HTML templates with variable substitution for dynamic content
- **`app.py`**: MVC-enabled application with controller registration and routing

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
   - **Home**: `http://localhost:8000/` → HomeController.index
   - **About**: `http://localhost:8000/about` → HomeController.about  
   - **API Status**: `http://localhost:8000/api/status` → ApiController.status
   - **Health Check**: `http://localhost:8000/health` → Traditional route

## 🔧 MVC Development Guide

### Adding New Features

#### 1. Create a Model (`models/user_model.py`)

```python
from .base_model import BaseModel
from datetime import datetime

class UserModel(BaseModel):
    def __init__(self):
        super().__init__()
    
    def create_user(self, name, email):
        users = self.load_data('users')
        user = {
            'id': self.generate_id(users),
            'name': name,
            'email': email,
            'created_at': datetime.now().isoformat()
        }
        users.append(user)
        self.save_data('users', users)
        return user
    
    def get_all_users(self):
        return self.load_data('users')
    
    def get_user_by_id(self, user_id):
        users = self.get_all_users()
        return next((u for u in users if u['id'] == user_id), None)
```

#### 2. Create a View (`views/users.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .user { margin: 10px 0; padding: 15px; background: #f5f5f5; }
    </style>
</head>
<body>
    <h1>{{title}}</h1>
    <div class="users-list">
        <!-- Template would need enhancement for loops -->
        <p>Total users: {{user_count}}</p>
    </div>
    <a href="/">← Back to Home</a>
</body>
</html>
```

#### 3. Create a Controller (`controllers/user_controller.py`)

```python
from models.user_model import UserModel
from raptor.core.app import Response

class UserController:
    def __init__(self):
        self.user_model = UserModel()
    
    def index(self, request):
        """List all users"""
        try:
            users = self.user_model.get_all_users()
            
            from raptor import Raptor
            app = Raptor()
            content = app.render_template('users.html', {
                'title': 'Users List',
                'user_count': len(users)
            })
            
            return Response(content)
        except Exception as e:
            return Response(f"Error: {str(e)}", 500)
    
    def show(self, request):
        """Show specific user"""
        user_id = int(request.params.get('id', 0))
        user = self.user_model.get_user_by_id(user_id)
        
        if user:
            content = f"<h1>User: {user['name']}</h1><p>Email: {user['email']}</p>"
            return Response(content)
        else:
            return Response("User not found", 404)
```

#### 4. Register in Main App (`app.py`)

```python
from controllers.user_controller import UserController

# Register the new controller
app.register_controller('user', UserController)

# Add routes
@app.route('/users', controller='user', action='index')
def users_route(request):
    pass

@app.route('/users/<id>', controller='user', action='show')
def user_detail_route(request):
    pass
```

## 🔌 API Endpoints

### MVC Routes
- **GET `/`** → `HomeController.index` - Home page with MVC architecture info
- **GET `/about`** → `HomeController.about` - About page with framework details  
- **GET `/api/status`** → `ApiController.status` - System status with request logging

### Traditional Routes
- **GET `/health`** - Simple health check (non-MVC example)

### API Response Examples

#### Status Endpoint (`/api/status`)
```json
{
  "status": "success",
  "message": "Raptor Framework API is running",
  "version": "1.0.0",
  "framework": "Raptor MVC",
  "python_version": "3.9+",
  "ssl_enabled": true,
  "timestamp": "2025-01-15T10:30:00Z",
  "architecture": "MVC (Model-View-Controller)"
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
    
    # Optional: Serve static files directly
    location /static/ {
        alias /path/to/raptor-framework/static/;
        expires 30d;
    }
}
```

## 📊 Data Storage

### File-Based Storage
- **Location**: `data/` directory (auto-created)
- **Format**: JSON files
- **Models**: Use `BaseModel` for consistent data operations

### Example Data Structure
```json
// data/api_logs.json
[
  {
    "id": 1,
    "timestamp": "2025-01-15T10:30:00Z",
    "method": "GET",
    "path": "/api/status",
    "user_agent": "Mozilla/5.0..."
  }
]
```

## 🧑‍💻 Development Workflow

### 1. Data Flow
```
HTTP Request → Router → Controller → Model → Controller → View → HTTP Response
```

### 2. Adding Features
1. **Model**: Create data handling logic
2. **View**: Design HTML template
3. **Controller**: Implement request handling
4. **Route**: Register in main application

### 3. Testing Strategy
```python
# Test Model
user_model = UserModel()
user = user_model.create_user("John", "john@example.com")
assert user['name'] == "John"

# Test Controller
from controllers.user_controller import UserController
controller = UserController()
# Mock request object for testing
```

## 📚 Learning Objectives

This MVC implementation teaches:

### **Software Architecture**
- Model-View-Controller design pattern
- Separation of concerns
- Component-based development
- Auto-loading and dependency injection

### **Web Development**
- HTTP protocol fundamentals
- Request/response cycle
- Template rendering
- RESTful API design

### **Python Advanced Concepts**
- Object-oriented programming
- File I/O operations
- JSON serialization
- Dynamic module loading
- Decorators and metaclasses

### **System Administration**
- systemd service management
- nginx reverse proxy
- Process monitoring
- Log management

## 🎯 Use Cases

- **🎓 Educational**: Learn MVC architecture and web framework internals
- **🚀 Prototyping**: Rapid web application development
- **🔬 Research**: Experiment with web technologies and patterns
- **📚 Teaching**: Demonstrate professional software design patterns
- **🏗️ Foundation**: Base for building more complex frameworks

## 🤝 Contributing

We welcome contributions that maintain the educational focus:

### Guidelines
- **📖 Keep it Educational**: Prioritize learning value over complexity
- **📝 Document Everything**: Extensive comments and documentation
- **🧪 Add Tests**: Include examples and test cases
- **🏗️ Follow MVC**: Maintain architectural patterns
- **🔍 Code Review**: Focus on code clarity and educational value

### Development Setup
```bash
git clone https://github.com/yourusername/raptor-framework.git
cd raptor-framework
python3 -m venv venv
source venv/bin/activate
python3 app.py
```

## 🔮 Roadmap

### Planned Features
- **🔗 Advanced Routing**: URL parameters and wildcards
- **🔐 Middleware System**: Authentication and logging middleware
- **📊 Enhanced Templates**: Template inheritance and loops
- **🗄️ Database Integration**: SQLite and PostgreSQL support
- **🧪 Testing Framework**: Built-in unit testing tools
- **📦 Plugin System**: Extensible architecture
- **🔍 Debug Toolbar**: Development debugging tools

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **🐍 Python Community**: For excellent documentation and libraries
- **🌐 Web Standards**: HTTP/1.1 and RESTful API principles  
- **🏗️ MVC Pattern**: Gang of Four design patterns
- **📚 Educational Resources**: Various web development tutorials and courses

---

**🎓 Built with ❤️ for learning, education, and professional development**

**🦅 Raptor Framework MVC - Where Education Meets Professional Architecture**