from flask import Blueprint, current_app, request

blueprint = Blueprint(name="client", import_name=__name__, url_prefix="/client")


@blueprint.route("/version", methods=["GET"])
def get_client_version():
    client_id = request.args["client"]
    return current_app.config["clients"][client_id]["instance"].get_client_version()


@blueprint.route("/info", methods=["GET"])
def get_host_info():
    client_id = request.args["client"]
    return current_app.config["clients"][client_id]["instance"].get_host_info()
