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

# Test Output
print('\nThe date of birth read is: ', month_birth, day_birth, year_birth)
print('The current date read is: ', current_month, current_day, current_year)

# TODO: Stage 2:
#     - Calculate number of seconds in average   month, year and day.



# TODO: Stage 3:
#     - Calculate approximate age in seconds
#     - Display Results - Person's age in seconds