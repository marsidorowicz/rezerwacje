event1 = {'summary': 'SIENKIEWICZA', 'start': 'Sun, 05 Jul 2020 20:13:00 +0200', 'end': 'Wed, 15 Jul 2020 20:13:00 +0200', 'description': '', 'location': '', 'attendees': []}
event2 = {'summary': 'KĄCIK', 'start': 'Mon, 06 Jul 2020', 'end': 'Tue, 07 Jul 2020', 'description': '', 'location': '', 'attendees': []}

def read_event(event):

    name = event['summary']
    beginning = event['start']
    end = event['end']
    print("Apartament: {}, przyjazd: {}, wyjazd: {}".format(name, beginning, end))

read_event(event1)
read_event(event2)