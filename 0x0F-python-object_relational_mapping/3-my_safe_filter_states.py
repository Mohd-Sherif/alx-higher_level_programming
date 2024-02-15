#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
But this time, it is safe from MySQL injections!
"""

import MySQLdb
import sys


host = 'localhost'
port = 3306
dbUsr = sys.argv[1]
dbPass = sys.argv[2]
dbName = sys.argv[3]
stateNameSearched = sys.argv[4]

db = MySQLdb.connect(host=host, port=port,
        user=dbUsr, passwd=dbPass, db=dbName)
cur = db.cursor()

query = \
        """
        SELECT *
        FROM states
        WHERE name=%s
        ORDER BY id;
        """
cur.execute(query, (stateNameSearched,))

res = cur.fetchall()

for row in res:
    print(row)

cur.close()
db.close()
