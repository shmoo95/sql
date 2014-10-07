# Create a SQLite3 database and table

#import the SQLite3 lib
import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)
	""")

conn.close()