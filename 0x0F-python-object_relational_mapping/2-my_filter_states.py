#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys


if __name__ == '__main__':
    host = 'localhost'
    port = 3306
    dbUsr = sys.argv[1]
    dbPass = sys.argv[2]
    dbName = sys.argv[3]
    stateNameSearched = sys.argv[4]

    db = MySQLdb.connect(
            host=host,
            port=port,
            user=dbUsr,
            passwd=dbPass,
            db=dbName
        )
    cur = db.cursor()

    query = \
        """
        SELECT *
        FROM states
        WHERE name
        LIKE '{}'
        ORDER BY id;
        """.format(stateNameSearched)

    cur.execute(query)

    res = cur.fetchall()

    for row in res:
        print(row)

    cur.close()
    db.close()
