#!/usr/bin/python3
import sys
import MySQLdb

if __name__== "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    """Connecting To MySQL Server"""
    try:   
        db = MySQLdb.connect(host="localhost", user =username, passwd=password, db = database, port=33306)
    except MySQLdb.Error as e:
        print("Error connecting to the MySQL:{}".format(e))

    """Creating  A Cursor Object"""
    cursor = db.cursor()

    """Query To Find All States from hbtn_0e_0_use"""
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"

    """Executing The Query"""
    try:
        cursor.execute(query, (state_name,))
    except MySQLdb.Error as e:
        print("Error executing query: {}".format())
        db.close()
        sys.exit(1)

    """Fetch All And Display The Result"""
    result = cursor.fetchall()
    for row in result:
        print(row)

    """Close the cursor and database connection"""
    cursor.close()
    db.close()