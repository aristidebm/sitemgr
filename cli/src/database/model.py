import os
import sys
from sqlalchemy import Column, Integer, String, TEXT, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import secrets
import datetime
from cli import DATABASE_URI

Base = declarative_base()


class Site(Base):
    __tablename__ = "site"
    id = Column(Integer, primary_key=True)
    tag = Column(String(10), nullable=False, unique=True, default=secrets.token_hex(5))
    description = Column(
        TEXT,
        nullable=True,
    )
    url = Column(
        String,
        nullable=False,
    )
    date = Column(Date, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.description}, {self.url}, {self.date})"


engine = create_engine("sqlite:///" + DATABASE_URI)
Base.metadata.create_all(engine)
