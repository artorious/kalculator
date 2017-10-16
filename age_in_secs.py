#!/usr/bin/env python3
'''Age in Seconds. 

A Simple script that approximates a person's age in seconds.
The program works for dates of birth from January 1, 1900 to the present.
'''

import datetime

print("=" * 78)
print(format(' AGE IN SECONDS ', '=^78'))
print("=" * 78)
print('Compute the approximate age in seconds of person based on a \
provided \ndate of birth.\n\nOnly ages for dates of birth from 1900 \
and after can be computed\n')
print("=" * 78)

# Get month, day, year of birth
# TODO: Error Checking
month_birth = int(input('Enter month born [1-12]: '))
day_birth = int(input('Enter day born [1-31]: '))
year_birth = int(input('Enter month born [YYYY]: '))

# Get current month, day, year
# TODO: Error Checking
current_month = datetime.date.today().month
current_day = datetime.date.today().day
current_year = datetime.date.today().year

# Determine number of seconds in a day, avaerage month & average year
# TODO: Error Checking
numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day
# NOTE: Add an extra day while doing a 4yr avg to account for leap yr
avg_numsecs_year = ((numsecs_year * 4) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12

# Test output
print('Number of Seconds per Day {0:,}'.format(numsecs_day))
print('Average Seconds per month {0:,}'.format(avg_numsecs_month))
print('Average Seconds per year {0:,}'.format(avg_numsecs_year))

# TODO: Stage 3:
#     - Calculate approximate age in seconds
#     - Display Results - Person's age in seconds