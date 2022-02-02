import datetime


def count_weeks(start_date: datetime.date, end_date: datetime.date) -> int:
    weeks = 1

    if start_date > end_date:
        raise Exception('Start date is greater than end date')

    # datetime.date object -> days number since 01.01.0001
    start_date_ord = start_date.toordinal()
    end_date_ord = end_date.toordinal()

    for date_ord in range(start_date_ord, end_date_ord+1):
        date = datetime.date.fromordinal(date_ord)
        if date.weekday() == 6:
            weeks += 1

    return weeks
