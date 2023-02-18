"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

days_per_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
day_of_the_week = 1
sundays_on_the_first = 0


for year in range(1900, 2001):
    leap_year = False

    if year % 4 == 0:
        leap_year = True

        if year % 100 == 0:
            leap_year = False

            if year % 400 == 0:
                leap_year = True

    if leap_year:
        days_per_month[2] = 29

    else:
        days_per_month[2] = 28

    for month in days_per_month:
        for day in range(1, days_per_month[month] + 1):
            if day == 1 and day_of_the_week == 7 and year != 1900:
                sundays_on_the_first += 1

            day_of_the_week += 1

            if day_of_the_week == 8:
                day_of_the_week = 1

print(sundays_on_the_first)
