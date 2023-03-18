#!/usr/bin/python3
'''script that takes in the name of a state as an
argument and lists all cities of that state, using
the database hbtn_0e_4_usa'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db_location = 'localhost'
    port = 3306
    search_param = argv[4]

    db = MySQLdb.connect(host=db_location,
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=port)

    cursor = db.cursor()

    query = """SELECT cities.name FROM states
            INNER JOIN cities ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id ASC"""

    cursor.execute(query, (search_param,))
    data = cursor.fetchall()

    # Create list with items and join them with ", "
    print(", ".join([city[0] for city in data]))

    db.close()
