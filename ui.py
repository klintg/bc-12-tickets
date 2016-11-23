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


def menu_table():
    time.sleep(2)
    table = [[],
             [],
             [],
             [],
             [],
             []]

    headers = ["", "", "", ""]
    click.secho(tabulate(table, headers, tablefmt="grid"),
                fg='blue', bold=True)
    time.sleep(8)
    click.clear()
    introduction()


def help():
    click.clear()
    click.secho('~' * 50, fg='yellow')
    click.secho('~' * 50, fg='yellow')
    click.secho('EVENTWISE.', bold=True, fg='yellow')
    click.secho('Definition of terms.', fg='blue', bold=True)
    def_terms = """
    """
    click.secho(def_terms, fg='yellow')
    click.secho('~' * 50, fg='yellow')
    click.secho('~' * 50, fg='yellow')