#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

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
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;")
res = cur.fetchall()
for row in res:
    print(row)

cur.close()
db.close()
