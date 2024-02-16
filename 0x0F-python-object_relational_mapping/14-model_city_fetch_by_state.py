#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

import sys

from model_city import City
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

    # Query all City objects and sort them by id in ascending order
    rows = session.query(City, State).join(State).order_by(City.id).all()

    # Display results
    for city, state in rows:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    # Close the session
    session.close()
