from app.controllers.controller import Controller

class HomeController(Controller):
    """
    Controller handling default homepage/landing page logic.
    """
    def index(self):
        """
        Render the main homepage view.
        """
        return self.render('home.html')
