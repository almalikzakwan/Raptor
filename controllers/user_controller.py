from models.user_model import UserModel
from raptor.core.app import Response
import json

class UserController:
    def __init__(self):
        self.user_model = UserModel()
    
    def index(self, request):
        """List all users - GET /users"""
        try:
            users = self.user_model.get_all_users()
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Users - Raptor Framework</title>
                <style>
                    body {{ font-family: Arial, sans-serif; padding: 20px; 
                           background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                           color: white; min-height: 100vh; }}
                    .container {{ max-width: 800px; margin: 0 auto; 
                                background: rgba(255,255,255,0.1); padding: 30px; 
                                border-radius: 15px; backdrop-filter: blur(10px); }}
                    .user-card {{ background: rgba(255,255,255,0.1); margin: 10px 0; 
                                padding: 15px; border-radius: 8px; }}
                    .btn {{ display: inline-block; padding: 8px 16px; margin: 5px; 
                           background: rgba(255,255,255,0.2); color: white; 
                           text-decoration: none; border-radius: 4px; }}
                    .btn:hover {{ background: rgba(255,255,255,0.3); }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>👥 Users ({len(users)} total)</h1>
                    
                    <a href="/users/create" class="btn">➕ Create New User</a>
                    
                    <div class="users-list">
            """
            
            for user in users:
                html += f"""
                        <div class="user-card">
                            <h3>{user.get('name', 'Unknown')}</h3>
                            <p>📧 {user.get('email', 'No email')}</p>
                            <p>🆔 ID: {user.get('id')}</p>
                            <a href="/users/{user.get('id')}" class="btn">👁️ View</a>
                            <a href="/users/{user.get('id')}/edit" class="btn">✏️ Edit</a>
                        </div>
                """
            
            if not users:
                html += "<p>No users found. <a href='/users/create'>Create the first user</a></p>"
            
            html += """
                    </div>
                    <p><a href="/">← Back to Home</a></p>
                </div>
            </body>
            </html>
            """
            
            return Response(html)
        except Exception as e:
            return Response(f"Error loading users: {str(e)}", 500)
    
    def create(self, request):
        """Show create user form - GET /users/create"""
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Create User - Raptor Framework</title>
            <style>
                body { font-family: Arial, sans-serif; padding: 20px; 
                       background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                       color: white; min-height: 100vh; }
                .container { max-width: 600px; margin: 0 auto; 
                           background: rgba(255,255,255,0.1); padding: 30px; 
                           border-radius: 15px; backdrop-filter: blur(10px); }
                input { width: 100%; padding: 12px; margin: 10px 0; 
                       border: none; border-radius: 5px; }
                button { background: #4CAF50; color: white; padding: 12px 24px; 
                        border: none; border-radius: 5px; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>➕ Create New User</h1>
                
                <form action="/users" method="POST">
                    <input type="text" name="name" placeholder="Full Name" required>
                    <input type="email" name="email" placeholder="Email Address" required>
                    <button type="submit">Create User</button>
                </form>
                
                <p><a href="/users">← Back to Users</a></p>
            </div>
        </body>
        </html>
        """
        return Response(html)
    
    def store(self, request):
        """Store new user - POST /users"""
        try:
            # In a real app, you'd parse POST data from request.body
            # For now, we'll create a dummy user
            name = request.input('name', 'New User')
            email = request.input('email', 'user@example.com')
            
            user = self.user_model.create_user(name, email)
            
            # Redirect to user detail (in real app, you'd handle redirects properly)
            return Response(f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta http-equiv="refresh" content="2;url=/users/{user['id']}">
                <title>User Created</title>
                <style>
                    body {{ text-align: center; padding: 50px; 
                           background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                           color: white; font-family: Arial; }}
                </style>
            </head>
            <body>
                <h1>✅ User Created Successfully!</h1>
                <p>Redirecting to user profile...</p>
                <p><a href="/users/{user['id']}">Click here if not redirected</a></p>
            </body>
            </html>
            """)
        except Exception as e:
            return Response(f"Error creating user: {str(e)}", 500)
    
    def show(self, request):
        """Show specific user - GET /users/{id}"""
        try:
            user_id = int(request.params.get('id', 0))
            user = self.user_model.get_user_by_id(user_id)
            
            if not user:
                return Response("User not found", 404)
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>User: {user['name']} - Raptor Framework</title>
                <style>
                    body {{ font-family: Arial, sans-serif; padding: 20px; 
                           background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                           color: white; min-height: 100vh; }}
                    .container {{ max-width: 600px; margin: 0 auto; 
                                background: rgba(255,255,255,0.1); padding: 30px; 
                                border-radius: 15px; backdrop-filter: blur(10px); }}
                    .user-info {{ background: rgba(255,255,255,0.1); padding: 20px; 
                                border-radius: 8px; margin: 20px 0; }}
                    .btn {{ display: inline-block; padding: 8px 16px; margin: 5px; 
                           background: rgba(255,255,255,0.2); color: white; 
                           text-decoration: none; border-radius: 4px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>👤 User Profile</h1>
                    
                    <div class="user-info">
                        <h2>{user['name']}</h2>
                        <p><strong>📧 Email:</strong> {user['email']}</p>
                        <p><strong>🆔 ID:</strong> {user['id']}</p>
                        <p><strong>📅 Created:</strong> {user.get('created_at', 'Unknown')}</p>
                    </div>
                    
                    <a href="/users/{user['id']}/edit" class="btn">✏️ Edit User</a>
                    <a href="/users" class="btn">📋 All Users</a>
                    <a href="/" class="btn">🏠 Home</a>
                </div>
            </body>
            </html>
            """
            
            return Response(html)
        except Exception as e:
            return Response(f"Error loading user: {str(e)}", 500)
    
    def edit(self, request):
        """Show edit user form - GET /users/{id}/edit"""
        try:
            user_id = int(request.params.get('id', 0))
            user = self.user_model.get_user_by_id(user_id)
            
            if not user:
                return Response("User not found", 404)
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Edit User: {user['name']} - Raptor Framework</title>
                <style>
                    body {{ font-family: Arial, sans-serif; padding: 20px; 
                           background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                           color: white; min-height: 100vh; }}
                    .container {{ max-width: 600px; margin: 0 auto; 
                                background: rgba(255,255,255,0.1); padding: 30px; 
                                border-radius: 15px; backdrop-filter: blur(10px); }}
                    input {{ width: 100%; padding: 12px; margin: 10px 0; 
                           border: none; border-radius: 5px; }}
                    button {{ background: #4CAF50; color: white; padding: 12px 24px; 
                            border: none; border-radius: 5px; cursor: pointer; margin: 5px; }}
                    .delete-btn {{ background: #f44336; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>✏️ Edit User</h1>
                    
                    <form action="/users/{user['id']}" method="PUT">
                        <input type="text" name="name" value="{user['name']}" required>
                        <input type="email" name="email" value="{user['email']}" required>
                        <button type="submit">Update User</button>
                    </form>
                    
                    <form action="/users/{user['id']}" method="DELETE" style="margin-top: 20px;">
                        <button type="submit" class="delete-btn" onclick="return confirm('Are you sure?')">
                            🗑️ Delete User
                        </button>
                    </form>
                    
                    <p>
                        <a href="/users/{user['id']}">← Back to User</a> | 
                        <a href="/users">All Users</a>
                    </p>
                </div>
            </body>
            </html>
            """
            
            return Response(html)
        except Exception as e:
            return Response(f"Error loading edit form: {str(e)}", 500)
    
    def update(self, request):
        """Update user - PUT /users/{id}"""
        # Implementation would handle form data parsing
        user_id = request.params.get('id')
        return Response(f"User {user_id} updated successfully! (Implementation pending)")
    
    def destroy(self, request):
        """Delete user - DELETE /users/{id}"""
        # Implementation would handle user deletion
        user_id = request.params.get('id')
        return Response(f"User {user_id} deleted successfully! (Implementation pending)")