from flask import Blueprint, current_app, request

blueprint = Blueprint(name="projects", import_name=__name__, url_prefix="/projects")


@blueprint.route("/all", methods=["GET"])
def get_all_projects():
    client_id = request.args["client"]
    return current_app.config["clients"][client_id]["instance"].get_all_projects()
