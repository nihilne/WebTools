from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest, NotFound

from app import config
from app.routes import all_blueprints


def create_app():
    app = Flask(__name__)
    for bp in all_blueprints:
        app.register_blueprint(bp)

    @app.errorhandler(BadRequest)
    def handle_bad_requests(error):
        return render_template("errors/400.html", error=error), 400

    @app.errorhandler(NotFound)
    def handle_not_found(error):
        if request.headers.get("HX-Request"):
            return (
                "<div class='text-red-500'>404 Not Found: This does not exist!?</div>",
                404,
            )
        return render_template("errors/404.html"), 404

    @app.context_processor
    def inject_context():
        return {
            "nav_items": config.NAV_ITEMS,
            "app_version": config.__version__,
        }

    return app
