from flask import Blueprint, render_template, request

from app.services.jsonformatter_service import JsonFormatterService

bp = Blueprint("jsonformatter", __name__, url_prefix="/jsonformatter")


@bp.route("/")
def index():
    return render_template("jsonformatter.html")


@bp.route("/format", methods=["POST"])
def jsonformatter_format():
    json_str = request.form.get("json_str")
    indentation = request.form.get("indentation", 2)

    if not json_str:
        return '<div class="text-red-600 mt-4">No input provided.</div>'

    if not indentation:
        return '<div class="text-red-600">Indentation is required.</div>'

    return JsonFormatterService.format_json(json_str, int(indentation))
