from flask import Flask
from .routes.biblioteca import biblioteca_routes
from .routes.views import views
from .routes.task import task
from .routes.ml_model import ml_model
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    CORS(app)

    app.register_blueprint(biblioteca_routes, url_prefix='/biblioteca')
    app.register_blueprint(task, url_prefix='/task')
    app.register_blueprint(ml_model, url_prefix='/model')
    app.register_blueprint(views)

    return app
