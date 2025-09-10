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
            
            # Get all available routes from web routes
            routes_html = ""
            total_routes = 0
            
            try:
                from routes.web import all_web_routes
                
                routes_html = self._generate_routes_table(all_web_routes)
                total_routes = len(all_web_routes)
                
            except ImportError:
                routes_html = "<tr><td colspan='4'>No routes found</td></tr>"
                total_routes = 0
            
            # Add routes info to template data
            about_data['routes_table'] = routes_html
            about_data['total_routes'] = total_routes
            
            from raptor import Raptor
            app = Raptor()
            content = app.render_template('about.html', about_data)
            
            return Response(content)
        except Exception as e:
            return Response(f"Error loading about page: {str(e)}", 500)
    
    def _generate_routes_table(self, routes):
        """Generate HTML table rows for routes"""
        html = ""
        
        for route in routes:
            method = route.method
            path = route.path
            name = route.route_name or 'unnamed'
            action = route.action
            
            # Get method badge class
            method_class = self._get_method_class(method)
            
            html += f"""
                <tr>
                    <td><span class="method-badge {method_class}">{method}</span></td>
                    <td><code class="route-path">{path}</code></td>
                    <td><span class="route-name">{name}</span></td>
                    <td>{action}</td>
                </tr>
            """
        
        return html
    
    def _get_method_class(self, method):
        """Get CSS class for HTTP method"""
        method_lower = method.lower()
        if method_lower == 'get':
            return 'method-get'
        elif method_lower == 'post':
            return 'method-post'
        elif method_lower == 'put':
            return 'method-put'
        elif method_lower == 'delete':
            return 'method-delete'
        else:
            return 'method-get'
    
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