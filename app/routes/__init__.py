import importlib
import pkgutil
from flask import Flask


def register_blueprints(app: Flask):
    prefix = __name__ + "."
    for _, module_name, _ in pkgutil.iter_modules(__path__):
        module = importlib.import_module(prefix + module_name)
        if hasattr(module, "bp"):
            app.register_blueprint(module.bp)
            app.logger.debug(f"Registered blueprint: {module.bp.name}")
