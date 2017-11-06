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
        else:
            pass

    except ValueError:
        print('INVALID input......Enter year [YYYY]')



# Determine if leap year

# Determine Day of week for 1st Jan of the yr
    # No. of days in each month (accounting for leap yrs)
    # Names of each of the 12 months for display
# Construct Calender year

# Display Calender year
