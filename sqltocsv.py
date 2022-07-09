import sqlite3
import pandas

con = sqlite3.connect('database.db')
cur = con.cursor()
df = pandas.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", con)
print(df)
# index=None to Remove 1st unecessary column
df.to_csv('database.csv', index=None)
