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

   # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # If state with id = 2 exists, update its name to "New Mexico"
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State with id = 2 not found")
    
    # Close the session
    session.close()