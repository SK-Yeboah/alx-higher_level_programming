#!/usr/bin/python3
"""Script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object
    new_state = State(name="California")

    # Add the State object to the session
    session.add(new_state)

    # Commit the transaction
    session.commit()

    # Create a new City object linked to the State
    new_city = City(name="San Francisco", state=new_state)

    # Add the City object to the session
    session.add(new_city)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()