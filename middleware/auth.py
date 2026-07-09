from flask import session, redirect, url_for, flash, request

class Authenticate:
    def handle(self):
        # Check if session exist.
        if 'user' not in session:
            flash("Please log in first to access this page.", "warning")
            # Send to login with 'next' parameter to redirect back after login.
            return redirect(url_for('login', next=request.url))
        return None
