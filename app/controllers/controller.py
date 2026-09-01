from flask import render_template, redirect, url_for

class Controller:
    """
    Base controller class providing standard rendering and redirect helpers.
    """
    def render(self, template_name, **context):
        """
        Render a view template.
        """
        return render_template(template_name, **context)

    def redirect(self, endpoint, **values):
        """
        Redirect to a named route endpoint.
        """
        return redirect(url_for(endpoint, **values))

    def redirect_to_url(self, url):
        """
        Redirect to a raw URL string.
        """
        return redirect(url)
