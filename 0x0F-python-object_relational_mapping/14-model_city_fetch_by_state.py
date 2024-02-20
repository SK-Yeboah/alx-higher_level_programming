#!/usr/bin/python3
"""Script to print all City objects from the database hbtn_0e_14_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    # Query all City objects and join with State to get the state name
    cities = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()

    # Print the results
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
