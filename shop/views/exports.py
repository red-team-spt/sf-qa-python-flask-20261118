import os

from flask import Blueprint, current_app, request, send_file

bp = Blueprint("exports", __name__)


@bp.route("/download")
def download():
    name = request.args["file"]
    return send_file(os.path.join(current_app.config["EXPORT_DIR"], name))
