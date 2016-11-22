import sqlite3
from datetime import datetime 

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('EventsTicker.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS events(ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, venue TEXT NOT NULL, start TEXT NOT NULL, end TEXT NOT NULL);''')

    def new_event(self, name, venue, start, end):

        with self.conn:
             self.cursor.execute("INSERT INTO events(name, venue, start, end) VALUES ('%s', '%s', '%s', '%s')" % (name, venue, datetime.strptime(start, '%d/%m/%Y %H:%M'), datetime.strptime(end, '%d/%m/%Y %H:%M')))
             self.conn.commit()