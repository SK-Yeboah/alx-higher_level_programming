#!/usr/bin/python3
"""Adds the State “California” with the City “San Francisco”
to the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create metadata and drop/create tables
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State and City
    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)

    # Add new State and City to session
    session.add(new_state)
    session.add(new_city)

    # Commit changes and close session
    session.commit()
    session.close()
