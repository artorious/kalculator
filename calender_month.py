#!/usr/bin/env python3
''' A Calender Month Program

Displays a calendar month for any given month between January 1800 and December 2099. 

Features:
    - The calender month 
    - The given the day of the week that the first day falls on  
    - The number of days in the month
'''

# Program Initialization
terminate = False # Control program termination

# Program greeting
print('=' * 80)
print(format(' CALENDER MONTH ', '=^80'))
print('=' * 80)
print('This program will display a calender month between the years 1800 and 2099')
print('-' * 80)

while not terminate:
    # Get month(int) & year(int) - User Input 
    month = int(input('Enter month [1-12] or [-1] to Quit: '))
    
    if month == -1:
        terminate = True # Termintate program
    else:
        while month < 1 or month > 12:  # Simple input error-checking
            month = int(input('INVALID INPUT - Enter month [1-12]: '))
        
        year = int(input('Enter year [YYYY]: '))

        while year < 1800 or year > 2099:   # Simple input error-checking
            year = int(input('INVALID - Enter year [YYYY]: '))
        
        # Determine if entered year is leap_year(bool)
        if (year % 4 == 0) and (not(year % 100 == 0) or (year % 400 == 0)):
            leap_year = True
        else:
            leap_year = False

        # Determine num_days_in_month(int) entered
        if month in (1, 3, 5, 7, 8, 10, 12):
            num_days_in_month = 31
        elif month in (4, 6, 9, 11):
            num_days_in_month = 30
        elif leap_year: # February
            num_days_in_month = 29
        else:
            num_days_in_month = 28
        
        print('\n{0}, {1} has {2} days.'.format(month, year, num_days_in_month))
# Test for leap (temp Code)
        if leap_year:
            print('{0} is a Leap Year.'.format(year))
        else:
            print('{0} is NOT a Leap Year.'.format(year))

# TODO: Determine day_of_week for entered month & year

# TODO: Display calender_month
