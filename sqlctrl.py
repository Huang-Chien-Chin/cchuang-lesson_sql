import sqlite3

conn = sqlite3.connect('DevOps.db')
curson = conn.cursor()
curson.execute("SELECT * FROM product_info")
records = curson.fetchall()
print (records)