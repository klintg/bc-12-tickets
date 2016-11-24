import sqlite3
from datetime import datetime 
import click
from prettytable import PrettyTable 
from termcolor import cprint
import tabulate 

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('EventsTicker.db')
        self.conn.execute('pragma foreign_keys = on')
        self.cursor = self.conn.cursor()
        df = "valid"
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS events(event_id integer PRIMARY KEY AUTOINCREMENT, \
                name TEXT NOT NULL, venue TEXT NOT NULL, start TEXT NOT NULL, end TEXT NOT NULL);''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tickets(ticket_id integer PRIMARY KEY AUTOINCREMENT, \
                valid TEXT NOT NULL, email TEXT NOT NULL, ticket_event_id integer NOT NULL, FOREIGN KEY(ticket_event_id) REFERENCES events(event_id) ON DELETE CASCADE)''')

    # creating a new event 
    def new_event(self, name, venue, start, end):

        with self.conn:
             self.cursor.execute("INSERT INTO events(name, venue, start, end) VALUES ('%s', '%s', '%s', '%s')" % (name, venue, datetime.strptime(start, '%d/%m/%Y'), datetime.strptime(end, '%d/%m/%Y')))
             self.conn.commit()
    
    # deleting an event 
    def getrid(self, eventid):
        self.cursor.execute("DELETE FROM events WHERE event_id = (%d)" %(eventid))
        self.conn.commit()
    
    # fetching all events from the database
    def read_all_events(self, *args):
        x = PrettyTable()
        x.field_names = ["EventID", "Name", "Venue", "Start", "End"]

        self.cursor.execute("SELECT * FROM events")
        all =  self.cursor.fetchall()
        for row in all:
            x.add_row([row[0], row[1], row[2], row[3], row[4]])
        print(x)

    # updating the data.
    def edit_data(self, event_id, name, venue, start, end):    
        self.cursor.execute("UPDATE events SET name = '%s', venue = '%s', start ='%s', end = '%s' WHERE event_id = %s" % (name, venue, datetime.strptime(start, '%d/%m/%Y'), datetime.strptime(end, '%d/%m/%Y'), event_id))
        self.conn.commit()
    
    # creating tickets
    def create_tickets(self, valid, email, event_id):
        with self.conn:
             self.cursor.execute("INSERT INTO tickets(valid, email, ticket_event_id) VALUES ('%s', '%s', '%s')" % (valid, email, event_id))
             self.conn.commit()


    # fetching tickets of a particular event 
    def get_event_tickets(self, eventid):
        x = PrettyTable()
        x.field_names = ["Ticketid", "Valid", "Email", "Ticket_EventID"]

        self.cursor.execute("SELECT * FROM tickets WHERE ticket_event_id = (%d)" %(eventid))
        all_tickets = self.cursor.fetchall()
        for row in all_tickets:
            x.add_row([row[0], row[1], row[2], row[3]])
        print(x)


    def get_ticket(self, event_id):
        
        self.cursor.execute("SELECT * FROM events WHERE event_id = %d" % (event_id))
        email_ticket = self.cursor.fetchone()
        for row in email_ticket:
            print('{}, {}'.format(row[1], row[2]))



    # invalidating a ticket.
    def invalidate(self, valid, tickid):
        self.cursor.execute("UPDATE tickets set valid = '%s' WHERE ticket_id = '%s'" % (valid, tickid))
        self.cursor.execute("SELECT * FROM tickets WHERE ticket_id = '%s'" % (tickid))        
        for row in self.cursor.fetchall():
            click.echo('{}, {}, {}, {}'.format(row[0], row[1], row[2], row[3]))
        