from flask import Blueprint, render_template, request
from app.services.YFKeygenService import YFKeygenService

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/yfkeygen")
def yfkeygen():
    return render_template("yfkeygen.html")


@main.route("/yfkeygen/generate", methods=["POST"])
def yfkeygen_generate():
    key = YFKeygenService.generate_key()
    return f"""
    <div class="w-min mt-4 p-3 border rounded-lg flex items-center justify-start">
        <span id="generated-key">{key}</span>
        <button onclick="copyKey(this)"
            class="cursor-pointer ml-4 px-3 py-1 bg-green-600 text-white rounded-lg hover:bg-green-700 hover:scale-105 transition duration-75">
            Copy
        </button>
    </div>
    """


@main.route("/csvsplitter")
def csvsplitter():
    return render_template("csvsplitter.html")
