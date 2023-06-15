from flask import Blueprint

from .v1.client import blueprint as client_blueprint
from .v1.clients import blueprint as clients_blueprint
from .v1.projects import blueprint as projects_blueprint

v1 = Blueprint(name="v1", import_name=__name__, url_prefix="/v1")

v1.register_blueprint(client_blueprint)
v1.register_blueprint(clients_blueprint)
v1.register_blueprint(projects_blueprint)
