import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import calendar

def sort_events():
    def check_if_last_day_of_month(date1):
        import datetime
        import calendar
        #  calendar.monthrange return a tuple (weekday of first day of the
        #  month, number
        #  of days in month)
        last_day_of_month = calendar.monthrange(date1.year, date1.month)[1]
        # here i check if date is last day of month
        if date1 == datetime.date(date1.year, date1.month, last_day_of_month):
            return True
        return False

    print("Connecting to google sheet zapas")
    cred1 = ServiceAccountCredentials.from_json_keyfile_name(
        'E:\\Programowanie\\wayscript\\send-emails-282415-a9f0e1e1227d.json')

    gs1 = gspread.authorize(cred1)
    print("Authentication successful, downloading content from sheet2")
    zapas = gs1.open('Zapas1').sheet1
    wydarzenia = gs1.open('Wydarzenia').sheet1

    today = datetime.datetime.today()
    months = ['STYCZEŃ', 'LUTY', 'MARZEC', 'KWIECIEŃ', 'MAJ', 'CZERWIEC', 'LIPIEC', 'SIERPIEŃ', 'WRZESIEŃ',
              'PAŹDZIERNIK', 'LISTOPAD', 'GRUDZIEŃ']
    date = datetime.date(today.year, today.month, today.day)
    try:
        rows_zapas = zapas.get()
        d = 0
        events = []

        # start counting from today up to and including the last day of the month
        if today.month != 12:
            while today.day + d <= calendar.monthrange(date.year, date.month)[1]:
                for row in rows_zapas:
                    if str(today.day + d) in row:
                        if months[today.month - 1] in row:
                            if str(today.year) in row:  # make list of all events for this month in this year
                                if str(today.day + d) in row[3]:
                                    eventsa = ("PRZYJAZD DNIA", today.day + d, row[0], row[1], row[2], row[3],
                                               row[4], row[5])
                                    print("PRZYJAZD")
                                    print(row)
                                    events.append(eventsa)
                                if str(today.day + d) in row[4]:
                                    eventsb = ("WYJAZD DNIA", today.day + d, row[0], row[1], row[2], row[3],
                                               row[4], row[5])
                                    print("WYJAZD")
                                    print(row)
                                    events.append(eventsb)

                d += 1
            # check next month to see if there are new events
            d = 0
            while today.day + d <= calendar.monthrange(date.year, date.month)[1]:
                for row in rows_zapas:
                    if str(d) in row:
                        if months[today.month] in row:
                            if str(today.year) in row:  # make list of all events for this month in this year
                                if str(d) in row[3]:
                                    eventsa = ("PRZYJAZD DNIA", today.day + d, row[0], row[1], row[2], row[3],
                                               row[4], row[5])
                                    print("PRZYJAZD")
                                    print(row)
                                    events.append(eventsa)
                                if str(d) in row[4]:
                                    eventsb = ("WYJAZD DNIA", today.day + d, row[0], row[1], row[2], row[3],
                                               row[4], row[5])
                                    print("WYJAZD")
                                    print(row)
                                    events.append(eventsb)
                d += 1
        else:
            while today.day + d <= calendar.monthrange(date.year, date.month)[1]:
                for row in rows_zapas:
                    if str(today.day + d) in row:
                        if months[today.month - 1] in row:
                            if str(today.year) in row:  # make list of all events for this month in this year
                                if str(today.day + d) in row[3]:
                                    eventsa = ("PRZYJAZD DNIA", today.day + d, row[0], row[1], row[2], row[3],
                                               row[4], row[5])
                                    print("PRZYJAZD")
                                    print(row)
                                    events.append(eventsa)
                                if str(today.day + d) in row[4]:
                                    eventsb = ("WYJAZD DNIA", today.day + d, row[0], row[1], row[2], row[3],
                                               row[4], row[5])
                                    print("WYJAZD")
                                    print(row)
                                    events.append(eventsb)
                d += 1
            # check next month to see if there are new events
            d = 0
            while today.day + d <= calendar.monthrange(date.year, date.month)[1]:
                for row in rows_zapas:
                    if str(d) in row:
                        if months[0] in row:  # search for January events
                            if str(today.year + 1) in row:  # make list of all events from next year first month
                                if str(d) in row[3]:
                                    eventsa = (
                                    "PRZYJAZD DNIA", today.day + d, row[0], row[1], row[2], row[3], row[4], row[5])
                                    print("PRZYJAZD")
                                    print(row)
                                    events.append(eventsa)
                                if str(d) in row[4]:
                                    eventsb = (
                                    "WYJAZD DNIA", today.day + d, row[0], row[1], row[2], row[3], row[4], row[5])
                                    print("WYJAZD")
                                    print(row)
                                    events.append(eventsb)
                d += 1
        events.reverse()

        print("Clearing google sheet Wydarzenia")
        wydarzenia.clear()
        for item in events:
            print(item)
            wydarzenia.insert_row(item)

    except Exception as e:
        print("Błąd: ", e)




sort_events()
import schedule
import time

schedule.every().day.at("08:00").do(sort_events)
while True:
    schedule.run_pending()
    time.sleep(600)