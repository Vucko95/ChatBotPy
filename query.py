import sqlite3


import sqlite3

# DB Connection
con = sqlite3.connect('database.db')
cur = con.cursor()
# We get a list of tuples
cur.execute("SELECT * FROM 'ips' ORDER BY asn")
fulltable = cur.fetchall()
# print(fulltable)
# wiht FOR Loop we can iterate over a list and see only tuples
for row in fulltable:
    print(row)
