import click 
import sys 
import time 
from colorama import init 
from termcolor import cprint 
from pyfiglet import figlet_format 
from tabulate import tabulate 




def introduction():
    click.secho('-' * 80, fg='white')
    click.secho('*' * 80, fg='blue')
    click.secho('=' * 80, fg='white')
    init(strip=not sys.stdout.isatty()) 
    cprint(figlet_format('EVENTWISE', font='big'), 'yellow')
    click.secho('*' * 80, fg='white')
    click.secho('=' * 80, fg='blue')
    click.secho('*' * 80, fg='white')



def starter():
    click.clear()
    introduction()
    click.secho('' * 75)
    click.secho('' * 75)

    menu_table()

def intro():
    click.secho(
        """

    +++++++++++++++++++++++++++EVENTWISER+++++++++++++++++++++++++++++++++++
    eventwiser app is a console app that can be used to create events,
    delete events, list events, edit events and generate tickets for events

    ------------------------------------------------------------------------ 

                    You can always type help to get assistance

    ***************************WELCOME**************************************

        """, bold=True, fg='green')


def menu_table():
    time.sleep(2)
    table = [["event_create", "create an event"],
             ["event_delete", "deletes an event from the id you provide"],
             ["event_list", "lists all events"],
             ["edit", "edits an event"],
             ["ticket_generate", "generates a ticket"],
             ["quit", "exiting the application"]]

    headers = ["COMMANDS","DESCRIPTION"]
    click.secho(tabulate(table, headers, tablefmt="grid"),
                fg='green', bold=True)
    time.sleep(10)
    click.clear()
    introduction()
