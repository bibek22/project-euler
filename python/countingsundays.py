leap = False


def month_days(n):
    if n in (4, 6, 9, 11):
        return 30
    elif n == 2:
        # print main.year
        if leap:
            return 29
        else:
            return 28
    else:
        return 31


def map_days(day, n):
    shift = n % 7
    return (day + shift) % 7


def main():
    year = 1901
    day = 2  # start was on Monday
    sundays = 0
    global leap
    while year < 2000:
        for month in range(1, 13):  # for each months
            day = map_days(day, month_days(month))
            true = bool(day == 1)
            if true:
                sundays += 1
            if year == 2000:
                print day
        year += 1
        leap = 0
        if year % 4 == 0:  # consideration for leap year
            leap = 1

    return sundays


print main()
