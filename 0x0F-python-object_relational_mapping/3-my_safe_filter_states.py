#!/usr/bin/python3
'''script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.'''

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
                         db=db_name,
                         port=port)

    cursor = db.cursor()
    query = """SELECT * FROM states
            WHERE BINARY name = %s ORDER BY id ASC"""

    cursor.execute(query, (search_param,))
    data = cursor.fetchall()

    for row in data:
        print(row)

    db.close()
