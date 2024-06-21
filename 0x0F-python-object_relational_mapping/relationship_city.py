#!/usr/bin/python3
"""Module City Class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Define City Class"""
    __tablename__ = 'cities'

    id = Column(
            Integer,
            autoincrement=True,
            nullable=False,
            primary_key=True
        )
    name = Column(
            String(128),
            nullable=False
        )
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False
        )
