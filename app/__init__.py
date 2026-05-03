import secrets

from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_session import Session
from werkzeug.exceptions import NotFound, HTTPException
from .routes import register_blueprints

load_dotenv()


def create_app(config_class="app.config.Config"):
    app = Flask(__name__)
    app.secret_key = os.environ["APP_KEY"]
    app.config.from_object(config_class)
    register_blueprints(app=app)
    Session(app=app)

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
            "nav_items": app.config["NAV_ITEMS"],
            "app_version": app.config["APP_VERSION"],
        }

    return app
