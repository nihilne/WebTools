import os

from cachelib.file import FileSystemCache

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    APP_VERSION = "v1.3.1"

    NAV_ITEMS = [
        {"name": "Random Generator", "endpoint": "randomgen.randomgen"},
        {"name": "CSV File Splitter", "endpoint": "csvsplitter.csvsplitter"},
        {"name": "VAT Calculator", "endpoint": "vatcalc.vatcalc"},
    ]

    SESSION_TYPE = "cachelib"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_CACHELIB = FileSystemCache(
        cache_dir=os.path.join(BASE_DIR, "flask_session"),
        threshold=500,
        default_timeout=3600,
    )

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://{user}:{password}@{host}:{port}/{db}".format(
            user="webtools_user",
            password=os.environ["DB_USER_PASSWORD"],
            host="db",
            port="3306",
            db="webtools",
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
