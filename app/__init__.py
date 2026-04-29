from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest, NotFound

from app import config
from app.routes import all_blueprints


def create_app():
    app = Flask(__name__)
    for bp in all_blueprints:
        app.register_blueprint(bp)

    @app.errorhandler(NotFound)
    def handle_not_found(error):
        if request.headers.get("HX-Request"):
            return "<div class='text-red-500'>404 Not Found</div>", 404

        return render_template("errors/404.html", error=error), 404

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        if 400 <= error.code < 500:
            return render_template("errors/4xx.html", error=error), error.code

        return error

    @app.context_processor
    def inject_context():
        return {
            "nav_items": config.NAV_ITEMS,
            "app_version": config.__version__,
        }

    return app
