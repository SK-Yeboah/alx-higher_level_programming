#!/usr/bin/python3
"""Module containing the definition of the State Class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""Creating an instance of the declaratiive_base"""
Base = declarative_base()

"""Define the state class"""
class State(Base):
    """Class representing a state"""
    __tablename = 'state'
    id = Column(Integer, primary_key = True, nullable=True, autoincrement=True)
    name = Column(String(128), nullable=False)