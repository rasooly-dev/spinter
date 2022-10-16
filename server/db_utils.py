import sqlite3

class db_utils:

    def __init__(self):
        self.conn = sqlite3.connect('spinter.db')
        print("Opened database successfully")
    
    def query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def insert(self, criteria={}, questions={}, cloud_data={}, processed_analysis={}):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO interviews (criteria, questions, cloud_data, processed_analysis) VALUES (?, ?, ?, ?)''', (criteria, questions, cloud_data, processed_analysis))
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
