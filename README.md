# 🦅 Raptor Framework

A lightweight, educational Python web framework built from scratch with SSL support and production deployment capabilities.

## 🚀 What is Raptor Framework?

Raptor is a custom Python web framework designed for educational purposes and real-world applications. Built entirely from scratch without heavy dependencies, it exposes the core concepts that power modern web frameworks, making it perfect for:

- **Learning web development fundamentals** - Understand how web frameworks work under the hood
- **Educational projects** - Teach HTTP protocols, routing, and web server concepts
- **Rapid prototyping** - Quick development of web applications and APIs
- **Production deployments** - SSL-ready with nginx reverse proxy support

### ✨ Key Features

- 🔧 **Built from scratch** - No Flask, Django, or FastAPI dependencies
- 🌐 **HTTP/HTTPS support** - SSL/TLS encryption with Let's Encrypt integration
- 🔀 **Flexible routing** - Decorator-based route definitions with parameter support
- 📡 **RESTful APIs** - JSON response handling and API endpoints
- 🎨 **Custom templates** - HTML templating system for dynamic content
- 🔒 **Production ready** - Systemd service, nginx reverse proxy, security headers
- 🐧 **Ubuntu deployment** - Complete deployment automation scripts
- 📊 **Lightweight** - Minimal resource footprint and fast response times

## 🏃‍♂️ Quick Start

### Prerequisites
- Python 3.8+
- Ubuntu 20.04+ (for production deployment)
- Domain name (optional, for SSL)

### Running the Application

1. **Clone and setup:**
   ```bash
   git clone <repository-url>
   cd Raptor
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Start the development server:**
   ```bash
   python app.py
   ```

3. **Access your application:**
   - Development: `http://localhost:8000`
   - With domain: `https://raptor.test` (after nginx setup)

### Available Endpoints

- **`/`** - Main page with "Hello, World!" and framework information
- **`/api/status`** - JSON API endpoint returning system status
- **`/about`** - Information about the Raptor Framework

## 🏗️ Project Structure

```
Raptor/
├── 📄 app.py                      # Main application entry point
├── 📄 requirements.txt            # Python dependencies
├── 📄 README.md                   # This file
├── 📁 raptor/                     # Core framework directory
│   ├── 📄 __init__.py
│   ├── 📁 core/                   # Framework core components
│   │   ├── 📄 __init__.py
│   │   └── 📄 app.py              # Main Raptor class and HTTP server
│   ├── 📁 http/                   # HTTP handling
│   │   ├── 📄 __init__.py
│   │   ├── 📄 request.py          # HTTP request parsing
│   │   └── 📄 response.py         # HTTP response generation
│   ├── 📁 routing/                # URL routing system
│   │   ├── 📄 __init__.py
│   │   └── 📄 router.py           # Route matching and parameters
│   └── 📁 utils/                  # Utility functions
│       ├── 📄 __init__.py
│       └── 📄 helpers.py          # Helper functions and utilities
├── 📁 static/                     # Static files (CSS, JS, images)
│   ├── 📁 css/
│   │   └── 📄 main.css
│   ├── 📁 js/
│   │   └── 📄 main.js
│   └── 📁 images/
├── 📁 templates/                  # HTML templates
│   ├── 📄 base.html
│   ├── 📄 home.html
│   └── 📄 about.html
├── 📁 config/                     # Configuration files
│   ├── 📄 __init__.py
│   ├── 📄 settings.py             # Application settings
│   └── 📁 nginx/
│       └── 📄 raptor.test.conf    # Nginx configuration template
├── 📁 scripts/                    # Deployment and setup scripts
│   ├── 📄 setup.sh                # Initial setup script
│   ├── 📄 deploy.sh               # Production deployment
│   └── 📄 ssl_setup.sh            # SSL certificate setup
├── 📁 tests/                      # Test suite
│   ├── 📄 __init__.py
│   ├── 📄 test_app.py             # Application tests
│   └── 📄 test_framework.py       # Framework core tests
├── 📁 docs/                       # Documentation
│   ├── 📄 installation.md
│   ├── 📄 deployment.md
│   └── 📄 api.md
└── 📁 logs/                       # Application logs
    └── 📄 .gitkeep
```

### 🧩 Framework Architecture

#### Core Components

- **`raptor/core/app.py`** - The main `Raptor` class that handles HTTP requests, routing, and responses
- **`raptor/http/`** - HTTP request/response handling with support for headers, parameters, and JSON
- **`raptor/routing/`** - URL routing system with decorator support and parameter extraction
- **`raptor/utils/`** - Utility functions for configuration, logging, and helper methods

#### Application Layer

- **`app.py`** - Your application code using the Raptor framework
- **`config/settings.py`** - Centralized configuration management
- **`static/`** - CSS, JavaScript, and image assets
- **`templates/`** - HTML templates for dynamic content generation

#### Deployment & Operations

- **`scripts/`** - Automation scripts for setup, deployment, and SSL configuration
- **`config/nginx/`** - Nginx reverse proxy configuration
- **`tests/`** - Comprehensive test suite for both framework and application
- **`docs/`** - Complete documentation for installation, deployment, and API usage

## 🎯 Use Cases

### Educational
- **Web Development Courses** - Teach students how web frameworks work internally
- **Computer Science Projects** - Understand HTTP protocols, socket programming, and web servers
- **Python Advanced Topics** - Learn about decorators, context managers, and object-oriented design

### Development
- **Rapid Prototyping** - Quickly build and test web application ideas
- **Microservices** - Create lightweight API services
- **IoT Projects** - Simple web interfaces for embedded systems
- **Learning Tools** - Build educational web applications and dashboards

### Production
- **Small to Medium Applications** - Deploy production-ready web applications
- **API Services** - RESTful APIs with JSON responses
- **Static Site Generation** - Dynamic content with static file serving
- **Legacy System Integration** - Bridge old systems with modern web interfaces

## 🛠️ Development

### Running Tests
```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=raptor --cov-report=html
```

### Code Structure
The framework follows clean architecture principles:
- **Separation of concerns** - Clear boundaries between HTTP, routing, and application logic
- **Modular design** - Each component can be used independently
- **Extensible** - Easy to add new features and middleware
- **Testable** - Comprehensive test coverage with mocking support

## 🔧 Configuration

The framework uses environment-based configuration:

```python
# config/settings.py
APP_ENV = 'development'  # development, production
DEBUG = True
HOST = '127.0.0.1'
PORT = 8000
DOMAIN = 'raptor.test'
SSL_ENABLED = False
```

## 📈 Performance

Raptor Framework is designed for:
- **Low memory footprint** - Minimal resource usage
- **Fast startup** - Quick application initialization
- **Efficient routing** - O(1) route matching for most cases
- **Concurrent handling** - Multi-threaded request processing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with educational goals in mind
- Inspired by modern web frameworks like Flask and FastAPI
- Designed for learning and real-world application

---

**🦅 Raptor Framework** - *Fast, Educational, Production-Ready*

Made with ❤️ for developers who want to understand how web frameworks work under the hood.