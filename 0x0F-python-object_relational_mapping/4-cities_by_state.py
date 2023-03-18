#!/usr/bin/python3
'''script that lists all cities from the database hbtn_0e_4_usa'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db_location = 'localhost'
    port = 3306

    db = MySQLdb.connect(host=db_location,
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=port)

    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities, states WHERE cities.state_id = states.id
                    ORDER BY cities.id""")

    data = cursor.fetchall()

    for row in data:
        print(row)

    db.close()
