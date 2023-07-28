from flask import Blueprint, current_app, request

blueprint = Blueprint(name="projects", import_name=__name__, url_prefix="/projects")


@blueprint.route("/all", methods=["GET"])
def get_all_projects():
    client_id = request.args["client"]
    return current_app.config["clients"][client_id]["instance"].get_all_projects()


@blueprint.route("/attached", methods=["GET"])
def get_attached_projects():
    client_id = request.args["client"]
    return current_app.config["clients"][client_id]["instance"].get_project_status()


@blueprint.route("/attach", methods=["POST"])
def attach_to_project():
    client_id = request.args["client"]
    req_json = request.json

    return current_app.config["clients"][client_id]["instance"].attach_project(
        name=req_json["name"],
        url=req_json["url"],
        key=req_json["key"],
    )


@blueprint.route("/suspend", methods=["POST"])
def suspend_project():
    client_id = request.args["client"]
    req_json = request.json

    return current_app.config["clients"][client_id]["instance"].suspend_project(
        url=req_json["url"],
    )


@blueprint.route("/resume", methods=["POST"])
def resume_project():
    client_id = request.args["client"]
    req_json = request.json

    return current_app.config["clients"][client_id]["instance"].resume_project(
        url=req_json["url"],
    )


@blueprint.route("/reset", methods=["POST"])
def reset_project():
    client_id = request.args["client"]
    req_json = request.json

    return current_app.config["clients"][client_id]["instance"].reset_project(
        url=req_json["url"],
    )


@blueprint.route("/update", methods=["POST"])
def update_project():
    client_id = request.args["client"]
    req_json = request.json

    return current_app.config["clients"][client_id]["instance"].update_project(
        url=req_json["url"],
    )


@blueprint.route("/detach", methods=["POST"])
def detach_project():
    client_id = request.args["client"]
    req_json = request.json

    return current_app.config["clients"][client_id]["instance"].detach_project(
        url=req_json["url"],
    )
