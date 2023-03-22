from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    ForeignKey,
    Text,
    Table
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


articles_hashtags = Table(
    "articles_hashtags",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("articles.id")),
    Column("hashtag_id", Integer, ForeignKey("hashtags.id"))
)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(50))
    lastname = Column(String(50))
    nickname = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.now)

    articles = relationship("Articles", back_populates="author")

    def __repr__(self):
        return f"Author({self.nickname})"


class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)

    articles = relationship(
        "Articles",
        secondary=articles_hashtags,
        back_populates="hashtags"
    )

    def __repr__(self):
        return f"Hashtag({self.name})"


class Articles(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(70), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="articles")
    hashtags = relationship(
        "Hashtag",
        secondary=articles_hashtags,
        back_populates="articles"
    )

    def __repr__(self):
        return f"Article({self.title})"
