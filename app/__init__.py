from flask import Flask, render_template
from app.routes import all_blueprints
from werkzeug.exceptions import BadRequest, NotFound

__version__ = "v1.1.1"

NAV_ITEMS = [
    {"name": "YetiForce Key Generator", "endpoint": "main.yfkeygen"},
    {"name": "CSV File Splitter", "endpoint": "main.csvsplitter"},
    {"name": "VAT Calculator", "endpoint": "main.vatcalc"},
]


def create_app():
    app = Flask(__name__)
    for bp in all_blueprints:
        app.register_blueprint(bp)

    @app.errorhandler(BadRequest)
    def handle_bad_requests(error):
        return render_template("errors/400.html", error=error), 400

    @app.errorhandler(NotFound)
    def handle_not_found(error):
        return render_template("errors/404.html"), 404

    @app.context_processor
    def inject_context():
        return {
            "nav_items": NAV_ITEMS,
            "app_version": __version__,
        }

    return app
