import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    pasword= Column(String(16), nullable=False, unique=True)
    

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id=Column(Integer, primary_key=True)
    Description_text=Column(String(500),nullable=False)
    pelicula_id=Column(Integer, ForeignKey('Favoritos.id'))
    pelicula=relationship(Favoritos)

class personajes(Base):
    __tablename__="personajes"
    id=Column(Integer, primary_key=True)
    Description_text=Column(String(500),nullable=False)
    pelicula_id=Column(Integer, ForeignKey('Favoritos.id'))
    pelicula=relationship(Favoritos)


class Favoritos(Base):
    __tablename__="Favoritos"
    id=Column(Integer, primary_key=True)
    user_from_id=Column(Integer, ForeignKey('User.id'))
    user_from=relationship(User)
    user_to_id=Column(Integer, ForeignKey('User.id'))
    user_to=relationship(User)
    Favoritos_pelicula_id=Column(Integer, ForeignKey('User.id'))
    Favoritos_pelicula=relationship(User)
    Favoritos_personajes_id=Column(Integer, ForeignKey('User.id'))
    Favoritos_personajes=relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')