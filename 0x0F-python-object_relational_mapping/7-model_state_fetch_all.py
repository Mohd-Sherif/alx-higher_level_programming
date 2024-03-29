#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    dbUsr, dbPass, dbName = sys.argv[1:]

    # Connect to MySQL server
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(dbUsr, dbPass, dbName),
            pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and sort them by id in ascending order
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print('{}: {}'.format(state.id, state.name))

    # Close the session
    session.close()
