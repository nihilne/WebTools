# type: ignore

from app.models.menu import Menu

seed_data = [
    Menu(
        name="Generators",
        endpoint="randomgen.index",
        position=0,
        enabled=True,
    ),
    Menu(
        name="CSV Row Splitter",
        endpoint="csvsplitter.index",
        position=1,
        enabled=True,
    ),
    Menu(
        name="VAT Calculator",
        endpoint="vatcalc.index",
        position=2,
        enabled=True,
    ),
    Menu(
        name="JSON Formatter",
        endpoint="jsonformatter.index",
        position=3,
        enabled=True,
    ),
]
