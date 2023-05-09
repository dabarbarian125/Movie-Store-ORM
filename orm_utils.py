#/usr/bin/python3

from sqlalchemy import create_engine, Column, String, Integer, Float, Table, ForeignKey, DateTime
from sqlalchemy.orm import mapper, sessionmaker, relationship, backref, Bundle
from sqlalchemy.orm import lazyload, joinedload
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:////home/runner/Movie-Store-ORM/sqlite-sakila.db')
# global Base
Base = declarative_base(engine)
# global metadata
metadata = Base.metadata
Session = sessionmaker(bind=engine)
# global session
session = Session()

# global conn 
conn = engine.connect()

class Film_Actor(Base):
  __tablename__ = 'film_actor'
  __table_args__ = {'extend_existing': True}
  actor_id = Column("actor_id", Integer, ForeignKey('actor.actor_id'), primary_key = True)
  film_id = Column("film_id", Integer, ForeignKey('film.film_id'), primary_key = True)
  last_update = Column(DateTime, nullable=False)
  
class Film(Base):
  __tablename__ = 'film'
  __table_args__ = {'extend_existing': True}
  film_id = Column(Integer, primary_key=True)
  title = Column(String(255), nullable=False)
  description = Column(String, nullable=True)
  release_year = Column(String(4), nullable=True)
  language_id = Column(Integer, ForeignKey('language.language_id'), nullable=False)
  original_language_id = Column(Integer, ForeignKey('language.language_id'), nullable=True)
  rental_duration = Column(Integer, nullable=False)
  rental_rate = Column(Integer, nullable=False)
  length = Column(Integer, nullable=True)
  replacement_cost = Column(Float, nullable=False)
  rating = Column(String(10), nullable=True)
  special_features = Column(String(100), nullable=True)
  last_update = Column(DateTime, nullable=False)
  actors = relationship(
        "Film",
        secondary='film_actor',
        backref=backref("actor",  lazy='joined'))
  categories = relationship(
        "Film",
        secondary='film_category',
        backref=backref("category",  lazy='joined'))
  language = relationship('Language', foreign_keys=[language_id])

class Actor(Base):
  __tablename__ = 'actor'
  __table_args__ = {'extend_existing': True}
  actor_id = Column(Integer, primary_key=True)
  first_name = Column(String(255), nullable=False)
  last_name = Column(String(255), nullable=False)
  last_update = Column(DateTime, nullable=False)
  films = relationship(
        "Actor",
        secondary='film_actor',
        backref=backref("film",  lazy='joined'))

class Film_Category(Base):
  __tablename__ = 'film_category'
  __table_args__ = {'extend_existing': True}
  film_id = Column("film_id", Integer, ForeignKey('film.film_id'), primary_key = True)
  category_id = Column("category_id", Integer, ForeignKey('category.category_id'), primary_key = True)
  last_update = Column(DateTime, nullable=False)

class Category(Base):
  __tablename__ = 'category'
  __table_args__ = {'extend_existing': True}
  category_id = Column(Integer, primary_key=True)
  name = Column(String(25), nullable=False)
  last_update = Column(DateTime, nullable=False)
  films = relationship(
        "Category",
        secondary='film_category',
        backref=backref("film",  lazy='joined'))



class Language(Base):
  __tablename__ = 'language'
  __table_args__ = {'extend_existing': True}
  language_id = Column(Integer, primary_key=True)
  name = Column(String(20), nullable=False)
  last_update = Column(DateTime, nullable=False)
  


def initialize():
  

  Base.metadata.create_all(engine)

  

  return session, conn, metadata