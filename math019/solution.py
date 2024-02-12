"""solver.py"""
import datetime


def answer():
    """from olver"""
    return solver(datetime.date(1901, 1, 1), datetime.date(2000, 12, 31))


def leap_year(year):
    """solver"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def solver(start, end):
    """solver"""
    count = 0
    current_date = start
    current_day = start.day
    current_month = start.month
    current_year = start.year

    while current_date <= end:
        if current_day == 1 and current_date.weekday() == 6:
            count += 1
        days_in_month = (
            29
            if leap_year(current_year) and current_month == 2
            else 28
            if current_month == 2
            else 31
            if current_month in [1, 3, 5, 7, 8, 10, 12]
            else 30
        )

        current_day += 1
        if current_day > days_in_month:
            current_day = 1
            current_month += 1
            if current_month > 12:
                current_month = 1
                current_year += 1

        current_date = datetime.date(current_year, current_month, current_day)

    return count


if __name__ == "__main__":
    start_date = datetime.date(1901, 1, 1)
    end_date = datetime.date(2000, 12, 31)
    print(solver(start_date, end_date))
    print("answer of math019 = ", answer())
