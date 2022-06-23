from flask import Flask
from .routes.biblioteca import biblioteca_routes
from .routes.views import views

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(biblioteca_routes, url_prefix='/biblioteca')
    app.register_blueprint(views)

    return app



