from flask import Blueprint, render_template, request, send_file, abort

from app.services.yf_keygen_service import YFKeygenService
from app.services.csv_splitter_service import CsvSplitterService
from app.services.vat_calc import VatCalc

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


@main.route("/csvsplitter/upload", methods=["POST"])
def csvsplitter_upload():
    file = request.files.get("file")
    has_header = request.form.get("has_header") == "1"
    chunk_size = int(request.form.get("chunk_size", 50))

    if not file:
        abort(400, "No file provided.")

    if not CsvSplitterService.allowed_file(file.filename):
        abort(400, "Invalid file type.")

    processed_file = CsvSplitterService.split_file_to_zip(file, chunk_size, has_header)
    response = send_file(
        processed_file,
        mimetype="application/zip",
        as_attachment=True,
        download_name="csv_files.zip",
    )
    response.headers["HX-Trigger"] = "downloadReady"
    return response


@main.route("/vatcalc")
def vatcalc():
    return render_template("vatcalc.html")


@main.route("/vatcalc/calculate", methods=["POST"])
def vatcalc_calculate():
    amount = float(request.form.get("amount", 0))
    rate = float(request.form.get("rate", 0))
    mode = request.form.get("mode")
    result = VatCalc.calculate_vat(amount, rate, mode)
    return f"<p>Result: {result}</p>"
