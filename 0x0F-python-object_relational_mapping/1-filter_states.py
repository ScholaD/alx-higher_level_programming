#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from
the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <dbname>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    query = 'SELECT * FROM states WHERE name LIKE BINARY "N%" \
            ORDER BY id;'

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    cursor = db.cursor()
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
