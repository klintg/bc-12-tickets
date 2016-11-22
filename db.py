import sqlite3
from datetime import datetime 

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('EventsTicker.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS events(event_id integer PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, venue TEXT NOT NULL, start TEXT NOT NULL, end TEXT NOT NULL);''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tickets(ticket_id integer PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL, ticket_event_id integer NOT NULL, FOREIGN KEY(ticket_event_id) REFERENCES events(event_id))''')
        
    def new_event(self, name, venue, start, end):

        with self.conn:
             self.cursor.execute("INSERT INTO events(name, venue, start, end) VALUES ('%s', '%s', '%s', '%s')" % (name, venue, datetime.strptime(start, '%d/%m/%Y %H:%M'), datetime.strptime(end, '%d/%m/%Y %H:%M')))
             self.conn.commit()

    def getrid(self, event_id):
        self.cursor.execute("DELETE FROM events WHERE event_id = (%d)" %(event_id))
        self.conn.commit()
    
    def read_all_events(self, *events):
        self.cursor.execute("SELECT * FROM events")
        all =  self.cursor.fetchall()
        for row in all:
            print('{}, {}, {}, {}, {}'.format(row[0], row[1], row[2], row[3], row[4]))

    def edit_data(self, event_id, name, venue, start, end):
        # updating the data.
        self.cursor.execute("UPDATE events SET name = '%s', venue = '%s', start ='%s', end = '%s' WHERE event_id = %s" % (name, venue, datetime.strptime(start, '%d/%m/%Y %H:%M'), datetime.strptime(end, '%d/%m/%Y %H:%M'), event_id))
        self.conn.commit()
    
    def create_tickets(self, fullname, email, id):
        with self.conn:
             self.cursor.execute("INSERT INTO tickets(name, email, ticket_event_id) VALUES ('%s', '%s', '%s')" % (fullname, email, id))
             self.conn.commit()