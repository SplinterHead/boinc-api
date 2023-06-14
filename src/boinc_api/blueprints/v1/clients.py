import uuid

from flask import Blueprint, current_app, request

blueprint = Blueprint(name="clients", import_name=__name__, url_prefix="/clients")


@blueprint.route("/add", methods=["POST"])
def add_client():
    client_data = request.json
    client_uuid = str(uuid.uuid4())
    current_app.config["clients"][client_uuid] = client_data

    return {"client_id": client_uuid}


@blueprint.route("/getall", methods=["GET"])
def get_all_clients():
    return [
        {"id": client_id, "name": client["name"], "hostname": client["hostname"]}
        for client_id, client in current_app.config["clients"].items()
    ]
