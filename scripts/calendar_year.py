#!/usr/bin/env python3

        
def calendar():
    ''' A Calender Year Program
    Displays a calendar Year for any given Year between 1800 and 2099, inclusive. 

    Display Features:
        - The calender Year 
        - The day of the week that the first day falls on  
        - The number of days in the Year
    '''

    # Init
    calendar_year = []     # calendar_year = [ [ calendar_month ], [ calendar_month ], etc.] ]
    days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) # TODO: handle Feb for leap
    month_names = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 
                    'August', 'September', 'October', 'November', 'December')
    month_separator = format(' ', '8')
    blank_week = format(' ', '21')
    blank_col = format(' ', '3')

    terminate = False   # Control program termination

    # Program Greeting
    print('=' * 120)
    print(format(' CALENDER YEAR ', '=^120'))
    print('=' * 120)
    print(format('Displays a Calendar for any given year between 1800 and 2099', 
    '^120'))
    print('-' * 120)

    while not terminate:    # Prompt for yrs until quit
        try:    # Get Year [YYYY] from user -  error-check input 
            year = int(input('Enter year [YYYY] ( -1 to Quit): '))

            while (year not in range(1800, 2100) and year != -1): # Check year is within appropriate range
                try:
                    print(format(' Enter Year (1800-2099) OR Enter -1 to Quit. ',
                    '~^120'))
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

                #  first day day of month for Jan 1. the days of the week for all remaining dates simply follow.
                first_day_of_current_month = (value + 1) % 7    
                
                # Construct calender for all 12 months
                for month_num in range(12):
                    month_name = month_names[month_num]

                    # Init for new month
                    current_day = 1
                    if first_day_of_current_month == 0:     # Saturday
                        starting_col = 7 
                    else:
                        starting_col = first_day_of_current_month
                    # Re-assign
                    current_col = 1
                    calendar_month = []    # calendar_month = [ week_1, week_2, . . ., week_k ]
                    calendar_week = ''

                    # Add any needed leading space for the first week of month
                    while current_col < starting_col:
                        calendar_week += blank_col
                        current_col += 1
                    
                    # Store month as separate weeks
                    if (month_name == 'February') and leap_year:
                        num_days_this_month = 29
                    else:
                        num_days_this_month = days_in_month[month_num]
                    
                    while current_day <= num_days_this_month:
                        # Store day of month in field of length 3
                        calendar_week += format(str(current_day), '>3')     # append each date with auto-alignment

                        # Check if at the last column of the week after each append
                        if current_col == 7:
                            calendar_month += [calendar_week] # Append a week string
                            calendar_week = '' # Re-init
                            current_col = 1 # Reset
                        else:
                            current_col += 1
                        
                        # increament current day
                        current_day += 1
                    
                    # fill out final row of month with needed blanks
                    calendar_week += blank_week[0:(7-current_col+1) * 3]
                    calendar_month += [calendar_week]

                    # reset values for next month
                    first_day_of_current_month = current_col
                    calendar_year += [calendar_month]
                    calendar_month = []

                # Display Calender year
                print('\n', year, '\n') # Display the year

                # Each row of months starts with Jan, Apr, Jul or Oct
                # Thus when month_num is 0, months 0-2 (Jan-Mar) are displayed
                # When month_num is 3, months 3-5 (Apr-Jun) are dispalyed, and so forth
                for month_num in [0, 3, 6, 9]:
                    
                    # Display 3 months in each row (E.g Jan, Feb, and Mar). Each is displayed left-justified in a field width of 19. 
                    # A leading blank character is appended to the formatting string to align with the first column of numbers displayed for each month. The print(. . ., end = '') form of print is used, which prevents the cursor from moving to the next line. Thus, the months can be displayed side-by-side. 
                    # Variable month_separator contains the appropriate number of blank spaces (initialized at the top of the program) to provide the required amount of padding between the months.
                    for i in range(month_num, month_num + 3):
                        print(' ' + format(month_names[i], '19'), month_separator, end=' ')
                    print('\n')

                    # Display each week of months on separate lines
                    # Init
                    week = 0 # keep count of number of weeks displayed
                    lines_to_print = True

                    while lines_to_print:
                        lines_to_print = False # Init

                        # another week to display for the first month in row?
                        for k in range(month_num, month_num + 3):
                            if week < len(calendar_year[k]):
                                print(calendar_year[k][week], end='')
                                lines_to_print = True
                            else:
                                print(blank_week, end='')
                            
                            print(month_separator, end='')
                        # move to the next screen line
                        print()

                        # Increament week
                        week += 1

        except ValueError:
            print('INVALID input......Enter year [YYYY]')

if __name__ == '__main__':
    calendar()

