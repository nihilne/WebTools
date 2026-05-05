from app.database import db


def seed(data, model):
    if model.query.first():
        return
    db.session.add_all(data)
    db.session.commit()
