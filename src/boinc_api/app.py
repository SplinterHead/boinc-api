from flask import Flask

from .blueprints.api_versions import v1


def create_app():
    app = Flask(__name__)
    app.config.update({"clients": {}})
    app.register_blueprint(v1)
    return app
