from flask import Blueprint, current_app, request

blueprint = Blueprint(name="messages", import_name=__name__, url_prefix="/messages")


@blueprint.route("/all", methods=["GET"])
def get_all_messages():
    client_id = request.args["client"]
    return current_app.config["clients"][client_id]["instance"].get_messages()
