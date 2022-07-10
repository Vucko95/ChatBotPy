import sqlite3
from fpdf import FPDF

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('PRAGMA table_info(ips)')
columns = cur.fetchall()
# print(columns)

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

for column in columns:
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100, h=30, txt=column[1], border=1)
pdf.ln()
cur.execute("SELECT * FROM 'IPS'")
rows = cur.fetchall()
for row in rows:
    print(row)
    for element in row:
        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=30, txt=str(element), border=1)
        print(element)
    pdf.ln()
    # print(rows)

pdf.output('output.pdf')
