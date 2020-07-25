import pathlib

BASE_DIR = pathlib.Path(__file__).parent


class Config:
    DEBUG = True
    ENV = 'development'
#    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(BASE_DIR / "data" / "db.sqlite3")
    SQLALCHEMY_DATABASE_URI = "postgresql://blog:1@localhost:5432/blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '@#$%^UTYRDsfghj^%'
