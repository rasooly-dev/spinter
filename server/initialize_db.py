import sqlite3
import os

# Create the database
conn = sqlite3.connect('spinter.db')
print("Opened database successfully")

# Create the table
conn.execute('''CREATE TABLE interviews
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            criteria JSON NOT NULL,
            questions JSON NOT NULL,
            cloud_data JSON NOT NULL,
            processed_analysis JSON NOT NULL
            );''')
print("Table created successfully")

print("database.db created successfully")

conn.close()
