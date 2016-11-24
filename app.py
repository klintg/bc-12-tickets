#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    tickets event_create <name> <start> <end> <venue>
    tickets event_delete  
    tickets event_list
    tickets edit <even_id> <new_name> <new_venue> <new_start> <new_end>
    tickets ticket_generate [<email>] <event_id>
    tickets quit
    tickets h


    tickets (-i | --interactive)
    tickets (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""


import cmd 
import ui 
import click 
import datetime 
import time
from db import Database
from docopt import docopt, DocoptExit
from sendemail import send_email
from datevalid import date_validate
from termcolor import colored
from ui import menu_table

# ui.introduction()
# ui.starter()


# docopt decorator 
def docopt_cmd(func):    
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('This is how to run the command')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn
 

#  database call
data = Database()

class EventsTick(cmd.Cmd):
    intro = "Create an event! Generate a ticket!"
    prompt = click.style("tickets>>", fg='green', bg='black', bold=True)
    

    # creating an event

    def do_event_create(self, args):
        try:
            name = input("Enter name of event: ")
            venue = input("Venue: ")
            start = input("Start Date dd/mm/yyyy: ")
            end = input("End Date dd/mm/yyyy: ")
            
            # date validation
            start1 = time.strptime(start, "%d/%m/%Y")
            end1 = time.strptime(end, "%d/%m/%Y")
            now = datetime.datetime.now().strftime("%d/%m/%Y")

            if now > start and now > end:
                print("You cannot input a past date")        
            elif start1 > end1:
                print("Your Start date can't be Greater than End date.")
            else:       
                data.new_event(name, venue, start, end)

        except:
            print(colored("Please insert the correct format"))
        
    
    # deleting an event
    @docopt_cmd
    def do_event_delete(self, event_id):
        """Usage: event_delete <id>"""

        try:
            data.getrid(int(event_id['<id>']))
            print("Event Deleted successfully")
        except:
            print(colored("Please insert an integer", "red"))



    # listing all events
    @docopt_cmd 
    def do_event_list(self, *args):
        """Usage: event_list"""

        print(data.read_all_events(*args))


    # editing an events
    def do_edit(self, args):

        # try:
        new_name = input("New Event: ")
        new_venue = input("New Venue: ")        
        eventid = input("Enter EventID To Update: ")
        new_start = input("New Start dd/mm/yyyy: ")
        new_end = input("New End dd/mm/yyyy: ")

        # validation
        # start1 = time.strptime(new_start, "%d/%m/%Y")
        # end1 = time.strptime(new_end, "%d/%m/%Y")
        # now = datetime.datetime.now().strftime("%d/%m/%Y")

        # if now > new_start and now > new_end:
        #     print("You cannot input a past date")        
        # elif start1 > end1:
        #     print("Your new date can't be Greater than End date.")
        # else:
        data.edit_data(eventid, new_name, new_venue, new_start, new_end)
        # except:
        #     print(colored("Wrong format: cannot edit event"))



    # sending tickets despite email input in ticket_generate    
    def do_ticket_send(self, *args):        
        # this should query for email and send the generated list.append
        email = input("Please provide the email: ")
        print(data.get_last_ticket())


    # generating ticket 
    def do_ticket_generate(self, *args):
        
        email = input("Enter your email: ")
        event_id = int(input("Enter the event: "))
        
        valid = True 
        data.create_tickets(valid, email, event_id)

        # if there is no email i run ticket_send.
        if email == "":
            return self.do_ticket_send()        
        else: 
            send_email(email, event_id)




    # user can input an event id and all the tickets for that event will be shown.
    @docopt_cmd
    def do_event_view(self, arg):
        """Usage: event_view <event_id>"""
        
        data.get_event_tickets(int(arg['<event_id>']))
    

    @docopt_cmd
    def do_ticket_invalidate(self, arg):
        """Usage: ticket_invalidate <ticket_id>"""
        valid = False
        # print(arg)
        data.invalidate(valid, int(arg['<ticket_id>']))
    

    # exiting the app
    @docopt_cmd
    def do_exit(self, args):
        """Usage: quit"""
        exit()
    
    @docopt_cmd
    def do_h(self, args):
        """Usage: h"""
        menu_table()



if __name__ == '__main__':
    EventsTick().cmdloop()