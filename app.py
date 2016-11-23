import cmd 
from db import Database
import smtplib

class EventsTick(cmd.Cmd):

    # creating an event
    def do_event_create(self, *event):

        name = input("Event name: ").upper()
        venue = input("Event venue: ").upper()
        start_date = input("Event start date: DD, MM, YYYY(eg 12/01/2015 16:25): ")
        end_date = input("Event end date: DD, MM, YYYY(eg 12/01/2015 16:25): ")
        
        # print(name, venue, start_date,">", end_date)

        data = Database()
        data.new_event(name, venue, start_date, end_date)

    
    # deleting an event
    def do_event_delete(self, event_id):
        # event_id = int(input("Please enter the event ID to: "))

        data = Database()
        data.getrid(int(event_id))

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
    def do_ticket_send(self, *args):
        email = input("Please input your email")
        print(email)

    def do_ticket_generate(self, *args):
        fullname = input("Please Enter your full names: ")
        email = input("Please Enter your Email: ")
        event_id = int(input("Please Enter the Event_ID you would like to attend: "))
        data = Database()
        data.create_tickets(fullname, email, event_id)
        
        if email == "":
            return self.do_ticket_send()
        
        else:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("clyntonn3@gmail.com", "themilgo36624")

            msg = "Looks like you will be attending "
            server.sendmail("clyntonn3@gmail.com", email, msg)
            server.quit()


    # user can input an event id and all the tickets for that event will be shown.
    def do_event_view(self, *args):
        event_id = int(input("Please Enter the Event_Id to see the tickets: "))
        print("This are all the tickets for this event.")

        data = Database()
        data.get_event_tickets(event_id)


if __name__ == '__main__':
    EventsTick().cmdloop()