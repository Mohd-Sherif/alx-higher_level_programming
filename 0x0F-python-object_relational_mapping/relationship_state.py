#!/usr/bin/python3
"""Module State Class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Define State Class"""
    __tablename__ = 'states'

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
    cities = relationship("City", cascade="all, delete-orphan", backref="state")
