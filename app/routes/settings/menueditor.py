from flask import Blueprint, render_template, request

from app.database import db
from app.models.menu import Menu

bp = Blueprint("settings_menueditor", __name__, url_prefix="/settings/menueditor")


@bp.route("/")
def index():
    menu_items = Menu.get_enabled()
    return render_template("settings/menueditor.html", menu_items=menu_items)


@bp.post("/reorder")
def reorder():
    order = request.form.get("order")
    if not order:
        return "Missing order", 400
    for position, item_id in enumerate(order.split(",")):
        menu_item = db.session.get(Menu, int(item_id))
        if menu_item:
            menu_item.position = position
    db.session.commit()
    return "", 204
