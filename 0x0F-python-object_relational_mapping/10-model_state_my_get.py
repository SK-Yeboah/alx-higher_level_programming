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

    # Query State objects containing the letter 'a'
    state = session.query(State).filter(State.name == state_name).first()

    # Display the result
    if state:
        print(state.id)
    else:
        print("Not found")
        
    #Close the session
    session.close()
