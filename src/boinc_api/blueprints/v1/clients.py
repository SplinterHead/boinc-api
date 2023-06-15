import uuid

from boinc_client import Boinc
from boinc_client.clients.rpc_client import RpcClient
from flask import Blueprint, current_app, request

blueprint = Blueprint(name="clients", import_name=__name__, url_prefix="/clients")


def _create_client(client_params: dict) -> Boinc:
    rpc = RpcClient(
        hostname=client_params["hostname"],
        port=client_params["port"],
        password=client_params["password"],
    )
    rpc.authenticate()
    return Boinc(rpc_client=rpc)


@blueprint.route("/add", methods=["POST"])
def add_client():
    client_data = request.json
    client_data.update({"instance": _create_client(client_data)})
    client_uuid = str(uuid.uuid4())
    current_app.config["clients"][client_uuid] = client_data

    return {"client_id": client_uuid}


@blueprint.route("/getall", methods=["GET"])
def get_all_clients():
    return [
        {"id": client_id, "name": client["name"], "hostname": client["hostname"]}
        for client_id, client in current_app.config["clients"].items()
    ]
