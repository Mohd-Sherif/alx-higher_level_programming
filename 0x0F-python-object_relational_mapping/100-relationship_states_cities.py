#!/usr/bin/python3
"""
script that creates the State 'California' with the City 'San Francisco'
from the database hbtn_0e_100_usa
"""

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

    # Create the State "California"
    california = State(name="California")
    session.add(california)
    # Flush to ensure that the new state is added to the database
    session.flush()

    # Create the City "San Francisco" and associate it with the State "California"
    san_francisco = City(name="San Francisco", state_id=california.id)
    session.add(san_francisco)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
