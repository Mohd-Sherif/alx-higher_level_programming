#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


host = 'localhost'
port = 3306
dbUsr = sys.argv[1]
dbPass = sys.argv[2]
dbName = sys.argv[3]

db = MySQLdb.connect(host=host, port=port,
        user=dbUsr, passwd=dbPass, db=dbName)
cur = db.cursor()

query = \
        """
        SELECT c.id, c.name, s.name
        FROM cities as c
        INNER JOIN states as s ON s.id = c.state_id
        ORDER BY c.id;
        """
cur.execute(query)

res = cur.fetchall()
for row in res:
    print(row)

cur.close()
db.close()
