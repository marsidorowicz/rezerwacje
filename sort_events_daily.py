import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import calendar
import schedule
import time


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

    print("Uruchamiam proces sortowania wydarzeń dla Arkuszy Google...")
    print(datetime.datetime.now())
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
        # 1 when it is not December and not last day of the month
        # start counting from today up to and including the last day of the month
        if today.month != 12:
            while today.day + d <= calendar.monthrange(date.year, date.month)[1]:
                for row in rows_zapas:
                    if str(today.day + d) in row:
                        if months[today.month - 1] in row:
                            if str(today.year) in row:  # make list of all events for this month in this year
                                if str(today.day + d) in row[3]:
                                    if row[3] < row[4]:
                                        eventsa = ("PRZYJAZD DNIA", today.day + d, row[0], row[5], row[1], row[2], row[3],
                                                   row[4], row[5])
                                        print("PRZYJAZD")
                                        print(row)
                                        events.append(eventsa)
                                if str(today.day + d) in row[4]:
                                    eventsb = ("WYJAZD DNIA", today.day + d, row[0], row[5], row[1], row[2], row[3],
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
                                    if row[3] < row[4]:
                                        eventsa = ("PRZYJAZD DNIA", today.day + d, row[0], row[5], row[1], row[2], row[3],
                                                   row[4], row[5])
                                        print("PRZYJAZD")
                                        print(row)
                                        events.append(eventsa)
                                if str(d) in row[4]:
                                    eventsb = ("WYJAZD DNIA", today.day + d, row[0], row[5], row[1], row[2], row[3],
                                               row[4], row[5])
                                    print("WYJAZD")
                                    print(row)
                                    events.append(eventsb)
                d += 1
        else:  # if December and not last day of the month
            while today.day + d <= calendar.monthrange(date.year, date.month)[1]:
                for row in rows_zapas:
                    if str(today.day + d) in row:
                        if months[today.month - 1] in row:
                            if str(today.year) in row:  # make list of all events for this month in this year
                                if str(today.day + d) in row[3]:
                                    if row[3] < row[4]:
                                        eventsa = ("PRZYJAZD DNIA", today.day + d, row[0], row[5], row[1], row[2], row[3],
                                                   row[4], row[5])
                                        print("PRZYJAZD")
                                        print(row)
                                        events.append(eventsa)
                                if str(today.day + d) in row[4]:
                                    eventsb = ("WYJAZD DNIA", today.day + d, row[0], row[5], row[1], row[2], row[3],
                                               row[4], row[5])
                                    print("WYJAZD")
                                    print(row)
                                    events.append(eventsb)
                d += 1
            # check next month to see if there are new events including new year first month
            d = 0
            while today.day + d <= calendar.monthrange(date.year, date.month)[1]:
                for row in rows_zapas:
                    if str(d) in row:
                        if months[0] in row:  # search for January events
                            if str(today.year + 1) in row:  # make list of all events from next year first month
                                if str(d) in row[3]:
                                    if row[3] < row[4]:
                                        eventsa = (
                                            "PRZYJAZD DNIA", today.day + d, row[0], row[5], row[1], row[2], row[3],
                                            row[4], row[5])
                                        print("PRZYJAZD")
                                        print(row)
                                        events.append(eventsa)
                                if str(d) in row[4]:
                                    eventsb = (
                                        "WYJAZD DNIA", today.day + d, row[0], row[5], row[1], row[2], row[3],
                                        row[4], row[5])
                                    print("WYJAZD")
                                    print(row)
                                    events.append(eventsb)
                d += 1
        events.reverse()  # To have it uploaded in reversed order in google sheet

        print("Clearing google sheet Wydarzenia")
        wydarzenia.clear()
        for item in events:
            print(item)
            wydarzenia.insert_row(item)

    except Exception as e:
        print("Błąd: ", e)


def google_send_email(message="123", to="marsidorowicz@gmail.com"):

    """
    # this module check if there are events meeting requirements and if yes it sends email with it
    :param message: message to be sent, allowed multiple elements in str as a list, then it splits them, and
    makes an email to have it line by line, not in one line
    :param to: email address in "example@gmail.com"
    :return:
    """

    import TestAI

    print("Uruchamiam proces wysyłania maili...")
    print(datetime.datetime.now())
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
    date2 = datetime.date(today.year, today.month, today.day)
    row_send_lidia = []
    row_send_mariusz = []
    row_send_ela = []
    row_new = ""
    try:
        rows_wydarzenia = wydarzenia.get()
        if today.month != 12:   # requirement that the actual month is not December
            if today.day is not calendar.monthrange(today.year, today.month)[1]:  # funtion works only if day in not
                # last day of the month
                for row in rows_wydarzenia:
                    if str(today.day + 1) == str(row[7]):  # requirement of departure tomorrow
                        if months[today.month - 1] in row:
                            if 'WYJAZD DNIA' in row:
                                print(row)
                                row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                if 'HM2' in row_new or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row\
                                        or 'HSII' in row:
                                    row_send_ela.append(row_new)
                                row_send_lidia.append(row_new)
                                row_send_mariusz.append(row_new)

                    if str(today.day + 1) == str(row[6]):  # requirement of arrival tomorrow
                        if months[today.month - 1] in row:
                            if 'PRZYJAZD DNIA' in row:
                                print(row)
                                row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                if 'HM2' in row_new or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row\
                                        or 'HSII' in row:
                                    row_send_ela.append(row_new)
                                row_send_mariusz.append(row_new)
            else:   # also the same but if today is the last day of the month
                for row in rows_wydarzenia:
                    if '1' == str(row[7]):  # requirement of departure tomorrow
                        if months[today.month] in row:
                            if 'WYJAZD DNIA' in row:
                                print(row)
                                row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                print("Nowy", row_new)
                                if 'HM2' in row or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row\
                                        or 'HSII' in row:
                                    row_send_ela.append(row_new)
                                row_send_lidia.append(row_new)
                                row_send_mariusz.append(row_new)
                                print("Test", row_send_mariusz)

                    if '1' == str(row[6]):  # requirement of arrival tomorrow
                        if months[today.month] in row:
                            if 'PRZYJAZD DNIA' in row:
                                print(row)
                                row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                if 'HM2' in row or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row\
                                        or 'HSII' in row:
                                    row_send_ela.append(row_new)
                                row_send_mariusz.append(row_new)
        else:   # if the actual month is December
            if today.day is not calendar.monthrange(today.year, today.month)[1]:  # funtion works only if day in not
                # last day of the month
                for row in rows_wydarzenia:
                    if str(today.day + 1) == str(row[7]):  # requirement of departure tomorrow
                        if months[today.month - 1] in row:
                            if 'WYJAZD DNIA' in row:
                                print(row)
                                row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                if 'HM2' in row or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row\
                                        or 'HSII' in row:
                                    row_send_ela.append(row_new)
                                row_send_lidia.append(row_new)
                                row_send_mariusz.append(row_new)

                    if str(today.day + 1) == str(row[6]):  # requirement of arrival tomorrow
                        if months[today.month - 1] in row:
                            if 'PRZYJAZD DNIA' in row:
                                print(row)
                                row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                if 'HM2' in row or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row\
                                        or 'HSII' in row:
                                    row_send_ela.append(row_new)
                                row_send_mariusz.append(row_new)
            else:  # also the same but if today is the last day of the month
                for row in rows_wydarzenia:
                    if '1' == str(row[7]):  # requirement of departure tomorrow
                        if months[0] in row:    # search for events in January
                            if str(today.year+1) in row:    # of the next year
                                if 'WYJAZD DNIA' in row:
                                    print(row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                    if 'HM2' in row or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row \
                                            or 'HSII' in row:
                                        row_send_ela.append(row_new)
                                    row_send_lidia.append(row_new)
                                    row_send_mariusz.append(row_new)

                    if '1' == str(row[6]):  # requirement of arrival tomorrow
                        if months[0] in row:    # search for events in January
                            if str(today.year + 1) in row:  # of the next year
                                if 'PRZYJAZD DNIA' in row:
                                    print(row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                    if 'HM2' in row or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row \
                                            or 'HSII' in row:
                                        row_send_ela.append(row_new)
                                    row_send_mariusz.append(row_new)

        if row_send_mariusz:
            TestAI.sendmailgoogle(row_send_mariusz, "apartamentymsc@gmail.com")
            print("Wysłano mail do Mariusza")
        if row_send_ela:
            TestAI.sendmailgoogle(row_send_ela, "elkaiwan@wp.pl")
            print("Wysłano mail do Eli")
        if row_send_lidia:
            love = "Kocham Cię"
            row_send_lidia.append(love)
            TestAI.sendmailgoogle(row_send_lidia, "lidiasidorowicz@gmail.com")
            (print("Wysłano mail do Lidii"))

    except Exception as e:
        print("Błąd ", e)


print("Uruchamiam procesy załadowania wydarzeń o 8:00/18:40 oraz wysłania maili o 19:00")
schedule.every().day.at("08:00").do(sort_events)
schedule.every().day.at("18:40").do(sort_events)
schedule.every().day.at("19:00").do(google_send_email)
print("Test sending")
google_send_email()

while True:
    schedule.run_pending()
    time.sleep(600)