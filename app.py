#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    tickets event_create <name> <start> <end> <venue>
    tickets event_delete <id>
    tickets event_list
    tickets edit <even_id> <new_name> <new_venue> <new_start> <new_end>
    tickets ticket_generate [<email>] <event_id>
    tickets quit


    tickets (-i | --interactive)
    tickets (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""


import cmd 
from db import Database
from docopt import docopt, DocoptExit
# import sendemail.py
import ui 
import click 
# from tabulate import tabulate 

ui.introduction()
ui.starter()


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
    @docopt_cmd
    def do_event_create(self, args):
        """Usage: event_create <name> <venue> <start> <end> """
        data.new_event(args['<name>'], args['<venue>'], args['<start>'], args['<end>'])

    
    # deleting an event
    @docopt_cmd
    def do_event_delete(self, event_id):
        """Usage: event_delete <id>"""
        
        data.getrid(int(event_id['<id>']))


    # listing all events
    @docopt_cmd 
    def do_event_list(self, *args):
        """Usage: event_list"""

        print(data.read_all_events(*args))


    # editing an events
    @docopt_cmd
    def do_edit(self, args):
        """Usage: edit <eventid> <new_name> <new_venue> <new_start> <new_end>"""
        
        data.edit_data(args['<new_name>'], args['<new_venue>'], args['<new_start>'], args['<new_end>'], int(args['<eventid>']),)


    # sending tickets despite email input in ticket_generate
    
    def do_ticket_send(self, *args):        
        # this should query for email and send the generated list.append
        print("Please provide the email")



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
    
    @docopt_cmd
    def do_quit(self, args):
        """Usage: quit"""
        exit()


if __name__ == '__main__':
    EventsTick().cmdloop()