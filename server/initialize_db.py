import sqlite3
import os

# Create the database
conn = sqlite3.connect('spinter.db')
print("Opened database successfully")

# Create the table
conn.execute('''CREATE TABLE interviews
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            criteria TEXT,
            questions TEXT,
            cloud_data TEXT,
            processed_analysis TEXT
            );''')
print("Table created successfully")

print("database.db created successfully")

conn.close()
