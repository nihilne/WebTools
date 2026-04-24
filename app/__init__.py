from flask import Flask
from app.routes import all_blueprints

__version__ = "v1.0"

NAV_ITEMS = [
    {"name": "YetiForce Key Generator", "endpoint": "main.yfkeygen"},
    {"name": "CSV File Splitter", "endpoint": "main.csvsplitter"},
]


def create_app():
    app = Flask(__name__)
    for bp in all_blueprints:
        app.register_blueprint(bp)

    @app.context_processor
    def inject_context():
        return {
            "nav_items": NAV_ITEMS,
            "app_version": __version__,
        }

    return app
