from flask import Blueprint, render_template

bp = Blueprint("settings_main", __name__, url_prefix="/settings")


@bp.route("/")
def index():
    available_settings = [
        {
            "name": "Menu Editor",
            "endpoint": "settings_menueditor.index",
        }
    ]
    return render_template(
        "settings/index.html",
        available_settings=available_settings,
    )
