#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


host = 'localhost'
port = 3306
dbUsr = sys.argv[1]
dbPass = sys.argv[2]
dbName = sys.argv[3]
stateName = sys.argv[4]

db = MySQLdb.connect(host=host, port=port,
        user=dbUsr, passwd=dbPass, db=dbName)
cur = db.cursor()

query = \
        """
        SELECT c.id, c.name, s.name
        FROM cities as c
        INNER JOIN states as s ON s.id = c.state_id
        WHERE s.name
        LIKE '{}'
        ORDER BY c.id;
        """.format(stateName)
cur.execute(query)

res = cur.fetchall()
cities = ', '.join(row[1] for row in res)
print(cities)

cur.close()
db.close()
