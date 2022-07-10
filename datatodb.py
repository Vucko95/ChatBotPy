import sqlite3
from fpdf import FPDF

con = sqlite3.connect('database.db')
cur = con.cursor()
new_rows = [
    ('25.25.25.25', 'a.b.c', 100),
    ('255.255.255.25', 'a.b.c', 200)
]
cur.executemany("INSERT INTO 'ips' VALUES(?,?,?)", new_rows)
con.commit()
cur.execute("SELECT * FROM 'ips'")
print(cur.fetchall())
