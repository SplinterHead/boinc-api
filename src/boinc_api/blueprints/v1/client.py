import json

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


@blueprint.route("/basicinfo", methods=["GET"])
def get_basic_info():
    client_id = request.args["client"]
    version = current_app.config["clients"][client_id]["instance"].get_client_version()
    host_info = current_app.config["clients"][client_id]["instance"].get_host_info()

    basic_host_info = {"host_info": {"os_name": host_info["host_info"]["os_name"]}}

    return version | basic_host_info


@blueprint.route("/state", methods=["GET"])
def get_client_state():
    client_id = request.args["client"]
    client_state = current_app.config["clients"][client_id][
        "instance"
    ].get_client_state()
    version = current_app.config["clients"][client_id]["instance"].get_client_version()

    client_state["client_state"].pop("core_client_major_version")
    client_state["client_state"].pop("core_client_minor_version")
    client_state["client_state"].pop("core_client_release")

    resp = client_state["client_state"] | version

    return resp
