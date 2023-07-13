import sqlite3 as sq
import re
import sys

db = r''

conn = sq.connect(db)
c = conn.cursor()
#c.execute("SELECT id, url, title FROM urls WHERE id > 1000")
c.execute("SELECT title FROM urls WHERE id < 1000")
rows = c.fetchall()

for row in rows:
    sys.stdout = open("HTRY.txt", "w")
    print(row)
    sys.stdout.close()

