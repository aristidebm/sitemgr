import os


class Config:
    """This object stores database and ressources path configuration."""

    DATABASE_URI = (
        "sqlite:///" + os.path.dirname(os.path.abspath(__file__)) + "/storage/sqlite.db"
    )
