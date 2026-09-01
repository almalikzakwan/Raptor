from flask import session
from app.controllers.controller import Controller

class DashboardController(Controller):
    """
    Controller handling access to the protected user dashboard.
    """
    def index(self):
        """
        Render dashboard containing user profile details.
        """
        return self.render('dashboard.html', user=session.get('user'))
