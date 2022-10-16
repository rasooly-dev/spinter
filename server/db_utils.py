import sqlite3
import json
import os

class db_utils:

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "spinter.db")
        self.conn = sqlite3.connect(db_path)
        print("Opened database successfully")
    
    def query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def insert(self, criteria={}, questions={}, cloud_data={}, processed_analysis={}):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO interviews (criteria, questions, cloud_data, processed_analysis) VALUES (?, ?, ?, ?)''', (json.dumps(criteria), json.dumps(questions), json.dumps(cloud_data), json.dumps(processed_analysis)))
        self.conn.commit()
        return cursor.lastrowid
    
    def update(self, id, criteria, questions, cloud_data, processed_analysis):
        cursor = self.conn.cursor()
        cursor.execute('''UPDATE interviews SET criteria = ?, questions = ?, cloud_data = ?, processed_analysis = ? WHERE id = ?''', (criteria, questions, cloud_data, processed_analysis, id))
        self.conn.commit()
        return cursor.lastrowid
    
    def delete(self, id):
        cursor = self.conn.cursor()
        cursor.execute('''DELETE FROM interviews WHERE id = ?''', (id,))
        self.conn.commit()
        return cursor.lastrowid
    
    def __del__(self):
        self.conn.close()
        print("Closed database successfully")
