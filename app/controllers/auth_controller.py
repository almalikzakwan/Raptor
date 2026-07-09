from flask import request, session, flash
from app.controllers.controller import Controller
from app.models.user import User

class AuthController(Controller):
    """
    Controller handling user authentication (login, credentials check, logout).
    """
    def show_login(self):
        """
        Display the login view if user is not already authenticated.
        """
        if 'user' in session:
            return self.redirect('dashboard')
        return self.render('login.html')

    def login(self):
        """
        Validate login credentials against MySQL database.
        """
        username = request.form.get('username')
        password = request.form.get('password')
        next_url = request.form.get('next') or request.args.get('next') or ''

        # Query the user from the database
        user = User.query.filter_by(username=username).first()

        # Check if user exists and password hash matches
        if user and user.check_password(password):
            # Store essential user data in session
            session['user'] = {
                'id': user.id,
                'username': user.username,
                'name': user.name
            }
            flash("Successfully logged in!", "success")
            return self.redirect_to_url(next_url if next_url else '/dashboard')
        else:
            flash("Invalid username or password.", "error")
            return self.redirect('login', next=next_url)

    def logout(self):
        """
        Clear user session and log out.
        """
        session.pop('user', None)
        flash("You have been logged out.", "info")
        return self.redirect('home')
