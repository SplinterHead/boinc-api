from flask import Flask
from flask_cors import CORS

from .blueprints.api_versions import v1


def create_app():
    app = Flask(__name__)
    app.config.update({"clients": {}})
    app.register_blueprint(v1)
    CORS(app)

    return app
