#!/usr/bin/python3
"""adds the State object 'Louisiana' to the database hbtn_0e_6_usa"""

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

    # Insert Louisiana
    state = State(name='Louisiana')
    session.add(state)
    session.commit()

    # print id
    print(state.id)

    # Close the session
    session.close()
