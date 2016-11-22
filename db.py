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

    def getrid(self, event_id):
        self.cursor.execute("DELETE FROM events WHERE ID = (%d)" %(event_id))
        self.conn.commit()
    
    def read_all_events(self, *events):
        self.cursor.execute("SELECT * FROM events")
        all =  self.cursor.fetchall()
        for row in all:
            print('{}, {}, {}, {}, {}'.format(row[0], row[1], row[2], row[3], row[4]))

    def edit_data(self, event_id, name, venue, start, end):
        # self.cursor.execute("SELECT *FROM events WHERE ID = (%d)" %(event_id))
        # spec = self.cursor.fetchone()
        # print(spec)

        # updating the data.

        self.cursor.execute("UPDATE events SET name = '%s', venue = '%s', start ='%s', end = '%s' WHERE ID = %s" % (name, venue, datetime.strptime(start, '%d/%m/%Y %H:%M'), datetime.strptime(end, '%d/%m/%Y %H:%M'), event_id))
        self.conn.commit()