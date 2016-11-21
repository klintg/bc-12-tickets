import cmd 

class EventsTick(cmd.Cmd):

    def do_event_create(self, *event):

        name = input("Event name: ").upper()
        venue = input("Event venue: ").upper()
        start_date = input("Event start date: YYYY, MM, DD(eg 2017, 02, 18): ")
        end_date = input("Event end date: YYYY, MM, DD(eg 2017, 02, 18): ")
        
        print(name, venue, start_date,">", end_date)

if __name__ == '__main__':
    EventsTick().cmdloop()