#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    tickets event_create <name> <start> <end> <venue>
    tickets event_delete <id>
    tickets event_list
    tickets edit <even_id> <new_name> <new_venue> <new_start> <new_end>
    tickets generate_ticket <fullname> <email> <event_id>


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


# docopt decorator 

def docopt_cmd(func):    
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
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
    intro = "Book a ticket!"
    prompt = 'tickets>>'

    

    # creating an event
    @docopt_cmd
    def do_event_create(self, args):
        """Usage: event_create <name> <start> <end> <venue>"""
        data.new_event(args['<name>'], args['<start>'], args['<end>'], args['<venue>'])

    
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
    def do_edit(self, *args):
        """Usage: edit <eventid> <new_name> <new_venue> <new_start> <new_end>"""
        # print(args)
        data.edit_data(int(eventid['<eventid>']), new_name['<new_name>'], new_venue['<new_venue>'], new_start_date['<new_start>'], new_end_date['<new_end>'])


    # sending tickets
    # @docopt_cmd
    def do_ticket_send(self, *args):        
        email = input("Please input your email")
        print(email)

    def do_ticket_generate(self, *args):
        """Usage: generate_ticket <fullname> <email> <event_id> """

        # fullname = input("Please Enter your full names: ")
        # email = input("Please Enter your Email: ")
        # event_id = int(input("Please Enter the Event_ID you would like to attend: "))
        print(args)

        # data = Database()
        # data.create_tickets(fullname, email, event_id)
        
        # if email == "":
        #     return self.do_ticket_send()
        
        # else:
        #     server = smtplib.SMTP('smtp.gmail.com', 587)
        #     server.starttls()
        #     server.login("clyntonn3@gmail.com", "themilgo36624")

        #     msg = "Looks like you will be attending "
        #     server.sendmail("clyntonn3@gmail.com", email, msg)
        #     server.quit()


    # user can input an event id and all the tickets for that event will be shown.
    def do_event_view(self, *args):
        """Usage: event_view <event_id>"""

        data.get_event_tickets(int(event_id['<event_id>']))
    

    def do_ticket_invalidate(self, tick_id):
        """Usage: ticket_invalidate <ticket_id>"""
        
        data.invalidate(int(tick_id))



if __name__ == '__main__':
    EventsTick().cmdloop()