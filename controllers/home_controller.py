from models.page_model import PageModel
from raptor.core.app import Response

class HomeController:
    def __init__(self):
        self.page_model = PageModel()
    
    def index(self, request):
        """Home page - GET /"""
        try:
            home_data = self.page_model.get_home_data()
            
            # Add Laravel-style routing info
            home_data.update({
                'routing_features': [
                    'Laravel-style route declarations',
                    'Named routes with URL generation',
                    'Route parameters and groups',
                    'Middleware support',
                    'RESTful resource routing'
                ]
            })
            
            from raptor import Raptor
            app = Raptor()
            content = app.render_template('home.html', home_data)
            
            return Response(content)
        except Exception as e:
            return Response(f"Error loading home page: {str(e)}", 500)
    
    def about(self, request):
        """About page - GET /about"""
        try:
            about_data = self.page_model.get_about_data()
            
            return Response(f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>About - Raptor Framework</title>
                <style>
                    body {{ font-family: Arial, sans-serif; padding: 40px; 
                           background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                           color: white; min-height: 100vh; }}
                    .container {{ max-width: 800px; margin: 0 auto; 
                                background: rgba(255,255,255,0.1); padding: 40px; 
                                border-radius: 15px; backdrop-filter: blur(10px); }}
                    .feature {{ margin: 15px 0; padding: 10px; 
                              background: rgba(255,255,255,0.1); border-radius: 5px; }}
                    a {{ color: white; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🦅 About Raptor Framework</h1>
                    <p>{about_data['description'][0]}</p>
                    
                    <h3>🛣️ Laravel-style Routing Features:</h3>
                    <div class="feature">✅ Separate route files (web.py, api.py)</div>
                    <div class="feature">✅ Named routes: Route::get('/users', 'UserController@index')->name('users.index')</div>
                    <div class="feature">✅ Route parameters: /users/{{id}}</div>
                    <div class="feature">✅ Route groups with prefix and middleware</div>
                    <div class="feature">✅ URL generation from route names</div>
                    <div class="feature">✅ RESTful resource routing</div>
                    
                    <p><a href="/">← Back to Home</a> | <a href="/api/status">API Status</a></p>
                </div>
            </body>
            </html>
            """)
        except Exception as e:
            return Response(f"Error loading about page: {str(e)}", 500)
    
    def contact(self, request):
        """Contact page - GET /contact"""
        return Response(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Contact - Raptor Framework</title>
            <style>
                body {{ font-family: Arial, sans-serif; padding: 40px; 
                       background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                       color: white; min-height: 100vh; }}
                .container {{ max-width: 600px; margin: 0 auto; 
                            background: rgba(255,255,255,0.1); padding: 40px; 
                            border-radius: 15px; backdrop-filter: blur(10px); }}
                input, textarea {{ width: 100%; padding: 10px; margin: 10px 0; 
                                  border: none; border-radius: 5px; }}
                button {{ background: #4CAF50; color: white; padding: 12px 24px; 
                         border: none; border-radius: 5px; cursor: pointer; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>📞 Contact Us</h1>
                <p>Get in touch with the Raptor Framework team!</p>
                
                <form action="/contact" method="POST">
                    <input type="text" name="name" placeholder="Your Name" required>
                    <input type="email" name="email" placeholder="Your Email" required>
                    <textarea name="message" rows="5" placeholder="Your Message" required></textarea>
                    <button type="submit">Send Message</button>
                </form>
                
                <p><a href="/">← Back to Home</a></p>
            </div>
        </body>
        </html>
        """)