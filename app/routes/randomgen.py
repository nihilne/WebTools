from flask import Blueprint, render_template, request

from app.services.randomgen_service import RandomGenService

bp = Blueprint("randomgen", __name__, url_prefix="/randomgen")


@bp.route("/")
def randomgen():
    return render_template("randomgen.html")


@bp.route("/generate", methods=["POST"])
def randomgen_generate():
    mode = request.form.get("mode")
    match mode:
        case "sha":
            key = RandomGenService.generate_custom_sha1()
        case "uuid":
            key = RandomGenService.generate_uuidv4()
        case _:
            key = None

    return f"""
    <div class="w-min mt-4 p-3 border rounded-lg flex items-center justify-start">
        <span id="generated-key">{key}</span>
        <button type="button" onclick="copyKey(this)"
            class="cursor-pointer ml-4 px-3 py-1 bg-green-600 text-white rounded-lg hover:scale-105 transition duration-75">
            Copy
        </button>
    </div>
    """
