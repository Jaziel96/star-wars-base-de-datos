import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    pasword= Column(String(16), nullable=False, unique=True)
    fav_personajes = relationship('fav_personajes', backref='user', lazy=True)
    fav_planetas = relationship('fav_planetas', backref='user', lazy=True)
    


class planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id=Column(Integer, primary_key=True)
    Description_text=Column(String(500),nullable=False)
    planeta_id=Column(Integer, ForeignKey('fav_planetas.id'))
    fav_planetas = relationship('fav_planetas', backref='user', lazy=True)

class personajes(Base):
    __tablename__="personajes"
    id=Column(Integer, primary_key=True)
    Description_text=Column(String(500),nullable=False)
    pelicula_id=Column(Integer, ForeignKey('fav_personajes.id'))
    fav_personajes = relationship('fav_personajes', backref='user', lazy=True)


class fav_planetas(Base):
    __tablename__ = 'fav_planetas'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planetas.id'))

class fav_personajes(Base):
    __tablename__ = 'fav_personajes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    personajes_id = Column(Integer, ForeignKey('personajes.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')