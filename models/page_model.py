from .base_model import BaseModel

class PageModel(BaseModel):
    def __init__(self):
        super().__init__()
    
    def get_home_data(self):
        """Get data for home page"""
        return {
            "title": "Raptor Framework - MVC Edition",
            "subtitle": "A lightweight, educational web framework with MVC architecture",
            "version": "1.0.0",
            "features": [
                "Pure Python Implementation",
                "MVC Architecture",
                "Educational Focus",
                "Production Ready",
                "Modern Design",
                "JSON API Support"
            ]
        }
    
    def get_about_data(self):
        """Get data for about page"""
        return {
            "title": "About Raptor Framework",
            "description": [
                "Raptor is a lightweight, educational web framework built from scratch in Python with MVC architecture.",
                "Perfect for learning web development fundamentals and Python advanced concepts.",
                "This framework now follows the Model-View-Controller pattern, separating concerns and improving maintainability."
            ]
        }