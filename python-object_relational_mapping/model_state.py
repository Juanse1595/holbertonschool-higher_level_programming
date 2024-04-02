#!/usr/bin/python3
"""State model to abstract state table"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class that represents table states
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name =  Column(String(128), nullable=False)
