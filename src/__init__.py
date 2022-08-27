from flask import Flask
from .routes.conteo import conteo
from .routes.biblioteca import biblioteca_routes
from .routes.views import views
from .routes.task import task

from flask_cors import CORS



def create_app():
    app = Flask(__name__,instance_relative_config=False)
    CORS(app)
    """ with app.app_context():
        from .dash import init_dashboard

        app = init_dashboard(app) """
    
    app.register_blueprint(biblioteca_routes, url_prefix='/biblioteca')
    app.register_blueprint(task, url_prefix='/task')
    app.register_blueprint(conteo, url_prefix='/conteo')
    app.register_blueprint(views)

    return app
