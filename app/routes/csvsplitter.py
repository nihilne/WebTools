from flask import (
    Blueprint,
    abort,
    render_template,
    request,
    send_file,
)

from app.services.csv_splitter_service import CsvSplitterService

bp = Blueprint("csvsplitter", __name__, url_prefix="/csvsplitter")


@bp.route("/")
def csvsplitter():
    return render_template("csvsplitter.html")


@bp.route("/upload", methods=["POST"])
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
