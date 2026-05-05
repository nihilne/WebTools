# type: ignore

from app.models.menu import Menu

seed_data = [
    Menu(
        name="Random Generator",
        endpoint="randomgen.randomgen",
        position=1,
        enabled=True,
    ),
    Menu(
        name="CSV File Splitter",
        endpoint="csvsplitter.csvsplitter",
        position=2,
        enabled=True,
    ),
    Menu(
        name="VAT Calculator",
        endpoint="vatcalc.vatcalc",
        position=3,
        enabled=True,
    ),
]
