from flask import session
from app.controllers.controller import Controller

class ProfileController(Controller):
    """
    Controller handling default profile page logic.
    """
    def index(self):
        """
        Render the profile view.
        """
        return self.render('profile.html', user=session.get('user'))
