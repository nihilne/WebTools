from app.seeds.handler import seed
from app.seeds import menu
from app.models.menu import Menu

all_seeds = [
    (menu.seed_data, Menu),
]


def run_all():
    for data, model in all_seeds:
        seed(data, model)
