import sqlite3

conn = sqlite3.connect('database.db')

#conn.execute('DROP TABLE USER')
print("Database connection successful!!!")
conn.execute('CREATE TABLE USER (username TEXT,password TEXT)') 

conn.close()