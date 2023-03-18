#!/usr/bin/python3

'''
Contains a MySQLdb script that performs read operations on a database
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    ''' Selects records from a database '''
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db_location = 'localhost'
    port = 3306

    db = MySQLdb.connect(db_location, username, password, db_name, port)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")
    data = cursor.fetchall()

    for row in data:
        print(row)

    db.close()
