#!/usr/bin/python3
"""script that lists all City objects from the database hbtn_0e_101_usa"""

import sys

from relationship_state import Base, State
from relationship_city import City
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
    cities = session.query(City).all()

    # Display results
    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
