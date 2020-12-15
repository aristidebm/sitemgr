import click

# from main import config
# from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from main.src.backend.model import Site, engine
from main.src.backend.exceptions import TakenTagError, TagNotFoundError
from main.src.ui.types import Url, Tag, DateTime


DBsession = sessionmaker(bind=engine)
session = DBsession()


def add_handler(tag: Tag, description: str, url: Url, date: DateTime) -> None:
    site = Site(tag=tag, desc=description, url=url, date=date)
    try:
        session.add(site)
        session.commit()
    except IntegrityError as it:
        raise TakenTagError()
    except SQLAlchemyError as sql_ex:
        print(sql_ex)


def rm_handler(tag):
    try:
        site = session.query(Site).filter_by(tag=tag).first()
        if not site:
            raise TagNotFoundError()
        else:
            session.delete(site)
            session.commit()
    except SQLAlchemyError as e:
        click.echo(e)


def update_handler():
    pass
