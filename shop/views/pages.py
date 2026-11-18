from flask import Blueprint, current_app, render_template, request, session

bp = Blueprint("pages", __name__)


@bp.route("/")
def home():
    return render_template("home.html")


@bp.route("/hello")
def hello():
    name = request.args.get("name", "visitor")
    return "<h1>Hello " + name + "</h1>"


@bp.route("/login", methods=["POST"])
def login():
    if request.form.get("password") == current_app.config["ADMIN_PASSWORD"]:
        session["admin"] = True
        return {"ok": True}
    return {"ok": False}, 401
