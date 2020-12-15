import datetime
import secrets
from sqlalchemy import Column, String, Integer, TEXT, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from main import config

Base = declarative_base()  # gets the model base class to extends.


class Site(Base):
    __tablename__ = "site"
    id = Column(Integer, primary_key=True)
    tag = Column(
        String(20),
        unique=True,
        nullable=False,
        default=secrets.token_hex(10),
    )
    desc = Column(TEXT, nullable=True)
    url = Column(String, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.datetime.now())

    def update(self, other):
        if isinstance(other, Site):
            if other.tag:
                self.tag = other.tag
            if other.desc:
                self.desc = other.desc
            if other.url:
                self.url = other.url
            if other.date:
                self.date = other.date

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}{self.desc}{self.url}{self.date})"


engine = create_engine(config.Config.DATABASE_URI)  # create database connection
Base.metadata.create_all(engine)
