from flask import Blueprint, current_app, request

blueprint = Blueprint(name="notices", import_name=__name__, url_prefix="/notices")


@blueprint.route("/all", methods=["GET"])
def get_all_notices():
    client_id = request.args["client"]
    return current_app.config["clients"][client_id]["instance"].get_public_notices()
