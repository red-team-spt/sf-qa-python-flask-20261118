from flask import Flask

from shop.views import pages, imports, exports


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("../config.py")
    app.register_blueprint(pages.bp)
    app.register_blueprint(imports.bp, url_prefix="/import")
    app.register_blueprint(exports.bp, url_prefix="/export")
    return app
