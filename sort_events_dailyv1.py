import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import calendar
import schedule
import time


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


def sort_events():


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
    number_of_days_in_month = calendar.monthrange(date.year, date.month)[1]
    try:
        print("*" * 80)
        print(date)
        print("SORT EVENTS FUNCTION")

        rows_zapas = zapas.get()
        d = 0
        events = []

        def check_arrival():
            if str(today.day + d) in row[3]:
                eventsa = (
                    "PRZYJAZD DNIA", today.day + d, row[0], row[5], row[1], row[2], row[3],
                    row[4], row[5])
                print("PRZYJAZD")
                print(row)
                if eventsa not in events:
                    events.append(eventsa)

        def check_departure():
            if str(today.day + d) in row[4]:
                eventsb = ("WYJAZD DNIA", today.day + d, row[0], row[5], row[1], row[2], row[3],
                           row[4], row[5])
                print("WYJAZD")
                print(row)
                if eventsb not in events:
                    events.append(eventsb)

        def check_arrival_overlap():
            if int(row[3]) > int(row[4]):
                eventsc = (
                    "PRZYJAZD DNIA", today.day + d, row[0], row[5], row[1], row[2], row[3],
                    row[4], row[5])
                print("PRZYJAZD z wyjazdem następnego miesąca")
                print(row)
                events.append(eventsc)
        # 1) Not December, not last day of the month
        if today.month != 12:
            print("Not December, not last day of the month")
            print("*" * 80)
            while today.day + d <= number_of_days_in_month:
                for row in rows_zapas:
                    if str(today.year) in row:  # check only this year events
                        if str(today.day + d) in row:
                            if months[today.month - 1] in row:
                                if int(row[3]) < int(row[4]):  # only if day of arrival is smaller
                                    # than departure, means no overlap
                                    check_arrival()
                                    check_departure()
                            if months[today.month] in row:  # make list of all events for next month with arrival in
                                #  previous
                                check_arrival_overlap()
                d += 1
            print(events)
        # 2) Not December, last day of the month

        # 3) December, not last day of the month
        else:
            pass
        # 4) December, last day of the month

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
    row_send_marzenka = []
    row_send_maria = []
    row_send_gabi = []
    row_new = ""
    try:
        rows_wydarzenia = wydarzenia.get()
        if today.month != 12:  # requirement that the actual month is not December
            if today.day is not calendar.monthrange(today.year, today.month)[1]:  # funtion works only if day in not
                # last day of the month
                print("*" * 80)
                print("SEND MAIL")
                print("NOT December and NOT last day of the month")
                print("*" * 80)
                for row in rows_wydarzenia:
                    if int(row[6]) < int(row[7]):
                        if int(today.day + 1) == int(row[7]):  # requirement of departure tomorrow
                            if months[today.month - 1] in row:
                                if 'WYJAZD DNIA' in row:
                                    print(row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                    if 'HM2' in row_new or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row \
                                            or 'HSII' in row:
                                        row_send_ela.append(row_new)
                                    row_send_lidia.append(row_new)
                                    row_send_mariusz.append(row_new)
                                    if 'SMREKOWA' in row:
                                        row_send_marzenka.append(row_new)
                                    if 'CICHA' in row or 'CLASSIC' in row or 'KASPROWICZA' in row \
                                            or 'GÓRSKI' in row or 'SŁONECZNY' in row or 'KĄCIK' in row or 'GIEWONT' in \
                                            row:
                                        row_send_maria.append(row_new)
                                    if 'POMORSKA' in row:
                                        row_send_gabi.append(row_new)

                        if int(today.day + 1) == int(row[6]):  # requirement of arrival tomorrow
                            if months[today.month - 1] in row:
                                if 'PRZYJAZD DNIA' in row:
                                    print(row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                    if 'HM2' in row_new or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row \
                                            or 'HSII' in row:
                                        row_send_ela.append(row_new)
                                    row_send_mariusz.append(row_new)
                                    if 'SMREKOWA' in row:
                                        row_send_marzenka.append(row_new)
                                    if 'CICHA' in row or 'CLASSIC' in row or 'KASPROWICZA' in row \
                                            or 'GÓRSKI' in row or 'SŁONECZNY' in row or 'KĄCIK' in row or 'GIEWONT' in \
                                            row:
                                        row_send_maria.append(row_new)

                        if int(today.day) == int(row[7]):  # requirement of todays departure to release preauthorization
                            if months[today.month - 1] in row:
                                if 'WYJAZD DNIA' in row:
                                    print("Odblokuj kaucję: ", row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " " + \
                                              "Odblokuj kaucję "
                                    row_send_mariusz.append(row_new)

                    if int(row[6]) > int(row[7]):   # same if arrival was last month but this month tomorrow they leave
                        if int(today.day + 1) == int(row[7]):  # requirement of departure tomorrow
                            if months[today.month - 1] in row:
                                if 'WYJAZD DNIA' in row:
                                    print(row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                    if 'HM2' in row_new or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row \
                                            or 'HSII' in row:
                                        row_send_ela.append(row_new)
                                    row_send_lidia.append(row_new)
                                    row_send_mariusz.append(row_new)
                                    if 'SMREKOWA' in row:
                                        row_send_marzenka.append(row_new)
                                    if 'CICHA' in row or 'CLASSIC' in row or 'KASPROWICZA' in row \
                                            or 'GÓRSKI' in row or 'SŁONECZNY' in row or 'KĄCIK' in row or 'GIEWONT' in \
                                            row:
                                        row_send_maria.append(row_new)
                                    if 'POMORSKA' in row:
                                        row_send_gabi.append(row_new)

                    #  now check for arrivals this month with departure next month
                    if months[today.month] in row:
                        if int(row[6]) > int(row[7]):
                            if int(today.day + 1) == int(row[7]):
                                if 'PRZYJAZD DNIA' in row:
                                    print(row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[
                                        5] + " "
                                    if 'HM2' in row_new or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row \
                                            or 'HSII' in row:
                                        row_send_ela.append(row_new)
                                    row_send_lidia.append(row_new)
                                    row_send_mariusz.append(row_new)
                                    if 'SMREKOWA' in row:
                                        row_send_marzenka.append(row_new)
                                    if 'CICHA' in row or 'CLASSIC' in row or 'KASPROWICZA' in row \
                                            or 'GÓRSKI' in row or 'SŁONECZNY' in row or 'KĄCIK' in row or 'GIEWONT' in \
                                            row:
                                        row_send_maria.append(row_new)
                                    if 'POMORSKA' in row:
                                        row_send_gabi.append(row_new)

            else:  # also the same but if today is the last day of the month  #todo add the same arrivals with
                # todo departure next month for this condition
                for row in rows_wydarzenia:
                    if int(row[6]) > int(row[7]):
                        if '1' == str(row[7]):  # requirement of departure tomorrow
                            if months[today.month] in row:
                                if 'WYJAZD DNIA' in row:
                                    print(row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                    print("Nowy", row_new)
                                    if 'HM2' in row or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row \
                                            or 'HSII' in row:
                                        row_send_ela.append(row_new)
                                    row_send_lidia.append(row_new)
                                    row_send_mariusz.append(row_new)
                                    print("Test", row_send_mariusz)
                                    if 'SMREKOWA' in row:
                                        row_send_marzenka.append(row_new)
                                    if 'CICHA' in row or 'CLASSIC' in row or 'KASPROWICZA' in row \
                                            or 'GÓRSKI' in row or 'SŁONECZNY' in row or 'KĄCIK' in row or 'GIEWONT' in \
                                            row:
                                        row_send_maria.append(row_new)
                                    if 'POMORSKA' in row:
                                        row_send_gabi.append(row_new)

                        if '1' == str(row[6]):  # requirement of arrival tomorrow
                            if months[today.month] in row:
                                if 'PRZYJAZD DNIA' in row:
                                    print(row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                    if 'HM2' in row or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row \
                                            or 'HSII' in row:
                                        row_send_ela.append(row_new)
                                    row_send_mariusz.append(row_new)
                                    if 'SMREKOWA' in row:
                                        row_send_marzenka.append(row_new)
                                    if 'CICHA' in row or 'CLASSIC' in row or 'KASPROWICZA' in row \
                                            or 'GÓRSKI' in row or 'SŁONECZNY' in row or 'KĄCIK' in row or 'GIEWONT' in \
                                            row:
                                        row_send_maria.append(row_new)

                        if int(today.day) == int(row[7]):  # requirement of todays departure to release preauthorization
                            if months[today.month - 1] in row:
                                if 'WYJAZD DNIA' in row:
                                    print("Odblokuj kaucję: ", row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " " + \
                                              "Odblokuj kaucję "
                                    row_send_mariusz.append(row_new)
        else:  # if the actual month is December
            if today.day is not calendar.monthrange(today.year, today.month)[1]:  # funtion works only if day in not
                # last day of the month
                for row in rows_wydarzenia:
                    if int(row[6]) < int(row[7]):
                        if int(today.day + 1) == int(row[7]):  # requirement of departure tomorrow
                            if months[today.month - 1] in row:
                                if 'WYJAZD DNIA' in row:
                                    print(row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                    if 'HM2' in row or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row \
                                            or 'HSII' in row:
                                        row_send_ela.append(row_new)
                                    row_send_lidia.append(row_new)
                                    row_send_mariusz.append(row_new)
                                    if 'SMREKOWA' in row:
                                        row_send_marzenka.append(row_new)
                                    if 'CICHA' in row or 'CLASSIC' in row or 'KASPROWICZA' in row \
                                            or 'GÓRSKI' in row or 'SŁONECZNY' in row or 'KĄCIK' in row or 'GIEWONT' in \
                                            row:
                                        row_send_maria.append(row_new)
                                    if 'POMORSKA' in row:
                                        row_send_gabi.append(row_new)

                        if int(today.day + 1) == int(row[6]):  # requirement of arrival tomorrow
                            if months[today.month - 1] in row:
                                if 'PRZYJAZD DNIA' in row:
                                    print(row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " "
                                    if 'HM2' in row or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row \
                                            or 'HSII' in row:
                                        row_send_ela.append(row_new)
                                    row_send_mariusz.append(row_new)
                                    if 'SMREKOWA' in row:
                                        row_send_marzenka.append(row_new)
                                    if 'CICHA' in row or 'CLASSIC' in row or 'KASPROWICZA' in row \
                                            or 'GÓRSKI' in row or 'SŁONECZNY' in row or 'KĄCIK' in row or 'GIEWONT' in \
                                            row:
                                        row_send_maria.append(row_new)
                        if int(today.day) == int(row[7]):  # requirement of todays departure to release preauthorization
                            if months[today.month - 1] in row:
                                if 'WYJAZD DNIA' in row:
                                    print("Odblokuj kaucję: ", row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " " + \
                                              "Odblokuj kaucję "
                                    row_send_mariusz.append(row_new)
            else:  # also the same but if today is the last day of the month
                for row in rows_wydarzenia:
                    if int(row[6]) < int(row[7]):
                        if '1' == str(row[7]):  # requirement of departure tomorrow
                            if months[0] in row:  # search for events in January
                                if str(today.year + 1) in row:  # of the next year
                                    if 'WYJAZD DNIA' in row:
                                        print(row)
                                        row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[
                                            5] + " "
                                        if 'HM2' in row or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' in row \
                                                or 'HSII' in row:
                                            row_send_ela.append(row_new)
                                        row_send_lidia.append(row_new)
                                        row_send_mariusz.append(row_new)
                                        if 'SMREKOWA' in row:
                                            row_send_marzenka.append(row_new)
                                        if 'CICHA' in row or 'CLASSIC' in row or 'KASPROWICZA' in row \
                                                or 'GÓRSKI' in row or 'SŁONECZNY' in row or 'KĄCIK' in row or 'GIEWONT' in \
                                                row:
                                            row_send_maria.append(row_new)
                                        if 'POMORSKA' in row:
                                            row_send_gabi.append(row_new)

                        if '1' == str(row[6]):  # requirement of arrival tomorrow
                            if months[0] in row:  # search for events in January
                                if str(today.year + 1) in row:  # of the next year
                                    if 'PRZYJAZD DNIA' in row:
                                        print(row)
                                        row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[
                                            5] + " "
                                        if 'HM2' in row or 'HONEYMOON' in row or 'MO' in row or 'CS' in row or 'HS' \
                                                in row or 'HSII' in row:
                                            row_send_ela.append(row_new)
                                        row_send_mariusz.append(row_new)
                                        if 'SMREKOWA' in row:
                                            row_send_marzenka.append(row_new)
                                        if 'CICHA' in row or 'CLASSIC' in row or 'KASPROWICZA' in row \
                                                or 'GÓRSKI' in row or 'SŁONECZNY' in row or 'KĄCIK' in row or 'GIEWONT' in \
                                                row:
                                            row_send_maria.append(row_new)
                        if int(today.day) == int(row[7]):  # requirement of todays departure to release preauthorization
                            if months[today.month - 1] in row:
                                if 'WYJAZD DNIA' in row:
                                    print("Odblokuj kaucję: ", row)
                                    row_new = row[0] + " " + row[1] + " " + row[2] + " " + row[3] + " " + row[5] + " " + \
                                              "Odblokuj kaucję "
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
        if row_send_marzenka:
            TestAI.sendmailgoogle(row_send_marzenka, "gomolka.adam@gmail.com")
            (print("Wysłano mail do Marzenki"))
        if row_send_maria:
            TestAI.sendmailgoogle(row_send_maria, "mbabunia@gmail.com")
            (print("Wysłano mail do Marii"))
        if row_send_gabi:
            TestAI.sendmailgoogle(row_send_gabi, "gabi2901g@gmail.com")
            (print("Wysłano mail do Gabi"))

    except Exception as e:
        print("Błąd ", e)


print("Uruchamiam procesy załadowania wydarzeń o 07:40 / 19:40 oraz wysłania maili o 20:00")
schedule.every().day.at("07:40").do(sort_events)
schedule.every().day.at("19:40").do(sort_events)
schedule.every().day.at("20:00").do(google_send_email)
sort_events()
# google_send_email()
while True:
    schedule.run_pending()
    time.sleep(600)
