from flask import Blueprint, render_template, request

from app.services.vatcalc_service import VatCalcService

bp = Blueprint("vatcalc", __name__, url_prefix="/vatcalc")


@bp.route("/")
def index():
    return render_template("vatcalc.html")


@bp.route("/calculate", methods=["POST"])
def vatcalc_calculate():
    amount = float(request.form.get("amount", 0))
    rate = float(request.form.get("rate", 0))
    mode = request.form.get("mode")
    result = VatCalcService.calculate_vat(amount, rate, mode)
    return f"<p>Result: {result}</p>"
