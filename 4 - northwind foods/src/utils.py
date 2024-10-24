import datetime
import calendar


def is_last_day_of_month(date: datetime.datetime) -> bool:
    last_day_of_month = calendar.monthrange(date.year, date.month)
    last_date_of_month = last_day_of_month[1]
    return date.day == last_date_of_month
