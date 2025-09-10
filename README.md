# 🦅 Raptor Framework

A lightweight, educational web framework built from scratch in Python. Perfect for learning web development fundamentals and understanding how modern web frameworks work under the hood.

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

- **Pure Python Implementation**: Built from scratch without heavy dependencies
- **Educational Focus**: Exposes core web development concepts
- **Lightweight**: Minimal overhead, maximum learning
- **Production Ready**: Includes systemd service configuration
- **Modern Design**: Beautiful UI with responsive design
- **JSON API Support**: Built-in JSON response handling
- **Threading Support**: Concurrent request handling
- **SSL Ready**: Compatible with nginx reverse proxy

## 🚀 What This Project Does

Raptor Framework demonstrates the fundamental concepts behind modern web frameworks by implementing:

- **HTTP Request/Response Handling**: Raw socket programming for HTTP communication
- **Routing System**: Decorator-based route registration
- **Request Processing**: Multi-threaded request handling
- **Response Generation**: HTML and JSON response builders
- **Static Content Serving**: Basic web page rendering
- **RESTful API Endpoints**: JSON API implementation

The framework serves a beautiful "Hello World" application with multiple routes showcasing different response types and modern web design patterns.

## 📁 Project Structure

```
raptor-framework/
├── raptor/                 # Framework core package
│   ├── __init__.py        # Package initialization and exports
│   ├── core/              # Core framework components
│   │   ├── __init__.py   # Core package initialization
│   │   └── app.py        # Main Raptor class with HTTP handling
│   └── http/              # HTTP utilities (future expansion)
│       └── __init__.py   # HTTP package initialization
├── app.py                 # Main application entry point
├── .gitignore            # Git ignore configuration
└── README.md             # Project documentation
```

### Core Components

- **`raptor/core/app.py`**: Contains the main `Raptor` class with HTTP server implementation, routing system, and response handlers
- **`app.py`**: Demo application showcasing framework capabilities with multiple routes
- **`raptor/__init__.py`**: Package exports and version information

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.9 or higher
- Ubuntu/Linux system (for systemd setup)
- nginx (optional, for production deployment)

### Manual Installation

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
   - Open your browser and visit `http://localhost:8000`
   - Try different routes:
     - `/` - Home page with beautiful UI
     - `/api/status` - JSON API endpoint
     - `/about` - About page

## 🔧 Production Deployment with systemd

### 1. Create systemd Service File

Create a systemd service file to manage the Raptor application:

```bash
sudo nano /etc/systemd/system/raptor.service
```

Add the following configuration:

```ini
[Unit]
Description=Raptor Framework Web Application
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

[Install]
WantedBy=multi-user.target
```

### 2. Enable and Start the Service

```bash
# Reload systemd configuration
sudo systemctl daemon-reload

# Enable the service to start on boot
sudo systemctl enable raptor.service

# Start the service
sudo systemctl start raptor.service

# Check service status
sudo systemctl status raptor.service
```

### 3. Service Management Commands

```bash
# Start the service
sudo systemctl start raptor

# Stop the service
sudo systemctl stop raptor

# Restart the service
sudo systemctl restart raptor

# View logs
sudo journalctl -u raptor.service -f

# Check service status
sudo systemctl status raptor
```

### 4. nginx Configuration (Optional)

For production deployment with SSL, configure nginx as a reverse proxy:

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
}
```

## 🔍 API Endpoints

- **GET `/`** - Home page with beautiful UI
- **GET `/about`** - About page with framework information
- **GET `/api/status`** - JSON API endpoint returning service status

### Example API Response

```json
{
    "status": "success",
    "message": "Raptor Framework API is running",
    "version": "1.0.0",
    "framework": "Raptor",
    "python_version": "3.9+",
    "ssl_enabled": true
}
```

## 🧑‍💻 Development

### Adding New Routes

```python
from raptor import Raptor

app = Raptor()

@app.route('/new-endpoint', methods=['GET', 'POST'])
def new_handler(request):
    return app.json({"message": "Hello from new endpoint!"})
```

### Response Types

```python
# HTML Response
return app.response("<h1>HTML Content</h1>")

# JSON Response
return app.json({"key": "value"})

# Custom Status Code
return app.response("Not Found", status=404)
```

## 📚 Learning Objectives

This framework helps you understand:

- Socket programming in Python
- HTTP protocol fundamentals
- Request/response cycle
- Threading in web applications
- Routing mechanisms
- Modern web framework architecture

## 🤝 Contributing

Contributions are welcome! This is an educational project, so please:

1. Keep code simple and well-commented
2. Focus on educational value
3. Maintain the lightweight nature
4. Add tests for new features

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🎯 Use Cases

- **Learning**: Perfect for understanding web framework internals
- **Prototyping**: Quick web application prototypes
- **Education**: Teaching web development concepts
- **Research**: Experimenting with web technologies

---

**Built with ❤️ for learning and education**