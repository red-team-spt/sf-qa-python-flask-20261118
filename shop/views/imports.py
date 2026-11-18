import yaml
from flask import Blueprint, request

bp = Blueprint("imports", __name__)


@bp.route("/catalog", methods=["POST"])
def import_catalog():
    document = yaml.load(request.get_data(), Loader=yaml.Loader)
    items = document.get("items", [])
    return {"imported": len(items)}


@bp.route("/prices", methods=["POST"])
def import_prices():
    document = yaml.safe_load(request.get_data())
    return {"prices": len(document.get("prices", []))}
