from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    ForeignKey,
    Text
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(50))
    lastname = Column(String(50))
    nickname = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"User({self.nickname})"


class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"Hashtag({self.name})"


class Articles(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(70), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)
    author_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Article({self.title})"
