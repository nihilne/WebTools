from sqlalchemy import select
from sqlalchemy.orm import Mapped, mapped_column
from app.database import db


class Menu(db.Model):
    __tablename__ = "menu"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(80), unique=True)
    endpoint: Mapped[str] = mapped_column(db.String(120), unique=True)
    position: Mapped[int] = mapped_column()
    enabled: Mapped[bool] = mapped_column()

    @classmethod
    def get_enabled(cls):
        return (
            db.session.execute(select(cls).where(cls.enabled).order_by(cls.position))
            .scalars()
            .all()
        )
