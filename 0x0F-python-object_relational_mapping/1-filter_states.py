#!/usr/bin/python3
''' lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa '''


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

    cursor.execute("""SELECT * FROM states WHERE
                    name LIKE BINARY 'N%' ORDER BY states.id ASC""")

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
