#!#!/usr/bin/env python3
''' A Calender Year Program

Displays a calendar Year for any given Year between 1800 and 2099, inclusive. 

Display Features:
    - The calender Year 
    - The day of the week that the first day falls on  
    - The number of days in the Year
'''

# Init
calendar_year = []     # calendar_year = [ [ calendar_month ], [ calendar_month ], etc.] ]
calendar_month = []    # calendar_month = [ week_1, week_2, . . ., week_k ]

terminate = False   # Control program termination

# Program Greeting
print('=' * 120)
print(format(' CALENDER YEAR ', '=^120'))
print('=' * 120)
print(format('Displays a Calendar for any given year between 1800 and 2099', '^120'))
print('-' * 120)

while not terminate:    # Prompt for yrs until quit
    try:    # Get Year [YYYY] from user -  error-check input 
        year = int(input('Enter year [YYYY] ( -1 to Quit): '))

        while (year not in range(1800, 2100) and year != -1): # Check year is within appropriate range
            try:
                print(format(' Enter Year (1800-2099) OR Enter -1 to Quit. ', '~^120'))
                year = int(input('Enter year [YYYY] : '))
            
            except ValueError:
                print('INVALID input......Enter year [YYYY]')

        if year == -1:
            terminate = True # terminate program
        
        else:# Determine if leap year
            if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
                leap_year = True
            else:
                leap_year = False
            
            # Determine Day of week for 1st Jan of the yr - Follow the 1st day of the year algorithm  
            century_digits = year // 100    # extract first two digits of the year
            year_digits = year % 100     # extract last two digits of the year
            
            value = year_digits + (year_digits // 4)

            if century_digits == 18:
                value += 2
            elif century_digits == 20:
                value += 6

            if not leap_year:   # Leap yr check
                value += 1

            first_day_of_month = (value + 1) % 7    #  first day day of month for Jan 1

            print('Day of the week is : ', first_day_of_month)

    except ValueError:
        print('INVALID input......Enter year [YYYY]')






    # No. of days in each month (accounting for leap yrs)
    # Names of each of the 12 months for display
# Construct Calender year

# Display Calender year
