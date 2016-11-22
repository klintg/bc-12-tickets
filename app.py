import cmd 
from db import Database

class EventsTick(cmd.Cmd):

    # creating an event
    def do_event_create(self, *event):

        name = input("Event name: ").upper()
        venue = input("Event venue: ").upper()
        start_date = input("Event start date: YYYY, MM, DD(eg 12/01/2015 16:25): ")
        end_date = input("Event end date: YYYY, MM, DD(eg 12/01/2015 16:25): ")
        
        # print(name, venue, start_date,">", end_date)

        data = Database()
        data.new_event(name, venue, start_date, end_date)

    
    # deleting an event
    def do_event_delete(self, *event):
        event_id = int(input("Please enter the event ID to: "))
        data = Database()
        data.getrid(event_id)

    # listing all events 
    def do_event_list(self, *events):
        data = Database()
        data.read_all_events(events)

    def do_edit(self, *args):
        event_id = int(input("Please enter the event ID to be edited: "))
        new_name = input("New Event name: ").upper()
        new_venue = input("New Event venue: ").upper()
        new_start_date = input("Event start date: YYYY, MM, DD(eg 12/01/2015 16:25): ")
        new_end_date = input("Event end date: YYYY, MM, DD(eg 12/01/2015 16:25): ")

        data = Database()
        data.edit_data(event_id, new_name, new_venue, new_start_date, new_end_date)



if __name__ == '__main__':
    EventsTick().cmdloop()