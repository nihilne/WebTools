from app.seeds import menu
from app.models.menu import Menu
from app.database import db

all_seeds = [
    (menu.seed_data, Menu),
]


def seed(data, model):
    if model.query.first():
        return False

    db.session.add_all(data)
    db.session.commit()
    return True


def run_all():
    results = []
    for data, model in all_seeds:
        success = seed(data, model)
        results.append((model, success))
    return results
