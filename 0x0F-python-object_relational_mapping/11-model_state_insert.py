#!/usr/bin/python3
"""Adds the State object "Louisiana" to the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract MySQL username, password, and database name from command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Database connection string
    db_connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(db_connection.format(username, password, database), pool_pre_ping=True)

    # Create session maker
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the State object to the session and commit the changes
    session.add(new_state)
    session.commit()

    # Print the ID of the newly created State object
    print(new_state.id)

    # Close the session
    session.close()
