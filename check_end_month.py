import datetime
import calendar


def check_if_last_day_of_month(date):

    #  calendar.monthrange return a tuple (weekday of first day of the
    #  month, number
    #  of days in month)
    last_day_of_month = calendar.monthrange(date.year, date.month)[1]
    # here i check if date is last day of month
    print(last_day_of_month)
    if date == datetime.date(date.year, date.month, last_day_of_month):
        return True
    return False


date = datetime.date(2020, 2, 8)
print(check_if_last_day_of_month(date))
