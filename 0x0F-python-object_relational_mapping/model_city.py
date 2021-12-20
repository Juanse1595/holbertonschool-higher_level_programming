#!/usr/bin/python3
'''model_state module'''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base



class City(Base):
    '''Defines the City class'''
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
