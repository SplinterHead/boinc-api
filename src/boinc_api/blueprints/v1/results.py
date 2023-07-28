from flask import Blueprint, current_app, request

blueprint = Blueprint(name="results", import_name=__name__, url_prefix="/results")


@blueprint.route("/all", methods=["GET"])
def get_all_results():
    client_id = request.args["client"]
    return current_app.config["clients"][client_id]["instance"].get_results()
