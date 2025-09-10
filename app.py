#!/usr/bin/env python3
from raptor import Raptor

# Create application instance
app = Raptor()

@app.route('/')
def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Raptor Framework - Hello World</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 0; 
                padding: 40px; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .container {
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
            }
            h1 { 
                color: #fff; 
                font-size: 3em;
                margin-bottom: 20px;
            }
            .raptor { 
                font-size: 4em; 
                margin: 20px 0;
            }
            p { 
                font-size: 1.2em; 
                margin: 10px 0;
            }
            .links {
                margin-top: 30px;
            }
            .links a {
                color: #fff;
                text-decoration: none;
                margin: 0 15px;
                padding: 10px 20px;
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-radius: 5px;
                transition: all 0.3s ease;
            }
            .links a:hover {
                background: rgba(255, 255, 255, 0.2);
                transform: translateY(-2px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="raptor">🦅</div>
            <h1>Hello, World!</h1>
            <p>Welcome to the Raptor Framework</p>
            <p>A lightweight, educational web framework built from scratch in Python</p>
            <div class="links">
                <a href="/api/status">API Status</a>
                <a href="/about">About</a>
            </div>
        </div>
    </body>
    </html>
    """
    return app.response(html)

@app.route('/api/status')
def api_status(request):
    return app.json({
        "status": "success",
        "message": "Raptor Framework API is running",
        "version": "1.0.0",
        "framework": "Raptor",
        "python_version": "3.9+",
        "ssl_enabled": True
    })

@app.route('/about')
def about(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About - Raptor Framework</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 0; 
                padding: 40px; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                min-height: 100vh;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
            }
            h1 { 
                color: #fff; 
                text-align: center;
                font-size: 2.5em;
                margin-bottom: 30px;
            }
            p { 
                font-size: 1.1em; 
                line-height: 1.6;
                margin: 15px 0;
            }
            .back-link {
                display: inline-block;
                margin-top: 30px;
                color: #fff;
                text-decoration: none;
                padding: 10px 20px;
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-radius: 5px;
                transition: all 0.3s ease;
            }
            .back-link:hover {
                background: rgba(255, 255, 255, 0.2);
                transform: translateY(-2px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🦅 About Raptor Framework</h1>
            <p>
                Raptor is a lightweight, educational web framework built from scratch in Python. 
                Perfect for learning web development fundamentals and Python advanced concepts.
            </p>
            <p>
                This framework is designed as a learning-focused tool that teaches you the inner 
                workings of web development while providing a solid foundation for building real applications.
            </p>
            <p>
                Built from the ground up without heavy dependencies, it exposes the core concepts 
                that power modern web frameworks, making it an excellent choice for understanding 
                how web applications work under the hood.
            </p>
            <a href="/" class="back-link">← Back to Home</a>
        </div>
    </body>
    </html>
    """
    return app.response(html)

if __name__ == '__main__':
    print("🦅 Starting Raptor Framework Application")
    print("Features:")
    print("  • Hello World on main page")
    print("  • Custom routes (/api/status, /about)")
    print("  • SSL ready with nginx")
    print("  • Ubuntu deployment ready")
    
    # Run on all interfaces for production deployment
    app.run(host='0.0.0.0', port=8000)