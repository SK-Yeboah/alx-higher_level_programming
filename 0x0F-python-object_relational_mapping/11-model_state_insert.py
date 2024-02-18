#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv)  != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)
    
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Database connection string
    db_connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(db_connection.format(username, password, database), pool_pre_ping=True)

    # Create a sessionmaker
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new State object
    new_state = State(name='Louisiana')

    # Add the new State object to the session
    session.add(new_state)

    # Commit the session to save changes to the database
    session.commit()

    # Print the new state's ID
    print(new_state.id)

    # Close the session
    session.close()
