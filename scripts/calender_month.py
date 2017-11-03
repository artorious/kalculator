#!/usr/bin/env python3
''' A Calender Month Program

Displays a calendar month for any given month between January 1800 and December 2099. 

Display Features:
    - The calender month 
    - The given the day of the week that the first day falls on  
    - The number of days in the month
'''



def calender_month_format():
    '''Displays a calendar month for any given month between January 1800 and December 2099'''
    # Program Initialization
    terminate = False # Control program termination
 
    # Program greeting
    print('=' * 80)
    print(format(' CALENDER MONTH ', '=^80'))
    print('=' * 80)
    print('This program will display a calender month between the years 1800 and 2099')
    print('-' * 80)

    while not terminate:
        
        try:
            # Get month(int) & year(int) - User Input 
            month = int(input('Enter month [1-12] or [-1] to Quit: '))

            if month == -1:
                terminate = True # Termintate program
            else:
                while month < 1 or month > 12:  # Confirm input is within range
                    month = int(input('INVALID INPUT - Enter month [1-12]: '))
                try:
                    year = int(input('Enter year 1800 - 2099 [YYYY]: '))

                    while year < 1800 or year > 2099:   # Confirm input is within range
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
                    
                    # Determine day_of_week for entered month & year
                    century_digits = year // 100    # extract first two digits of the year
                    year_digits = year % 100    # extract last two digits of the year
                    # Follow the day of the week algorithm appended in pseudocode
                    value = year_digits + (year_digits // 4)

                    if century_digits == 18:
                        value += 2
                    elif century_digits == 20:
                        value += 6

                    if month == 1 and not leap_year:
                        value += 1
                    elif month == 2:
                        if leap_year:
                            value += 3
                        else:
                            value += 4
                    elif month == 3 or month == 11:
                        value += 4
                    elif month == 5:
                        value += 2
                    elif month == 6:
                        value += 5
                    elif month == 8:
                        value += 3
                    elif month == 9 or month == 12:
                        value += 6
                    elif month == 10:
                        value += 1
                    
                    # Day value in the day of the week algorithm
                    # Only the day_of_week for the first day of any given month is needed
                    # all remaining days follow sequentially
                    day_of_week = (value + 1) % 7 # 1-Sun, 2-Mon, ......, 6-Fri, 0-Sat

                    # Determine  corresponding month_name
                    if month == 1:
                        month_name = 'January'
                    elif month == 2:
                        month_name = 'February'
                    elif month == 3:
                        month_name == 'March'
                    elif month == 4:
                        month_name = 'April'
                    elif month == 5:
                        month_name = 'May'
                    elif month == 6:
                        month_name = 'June'
                    elif month == 7:
                        month_name = 'July'
                    elif month == 8:
                        month_name = 'August'
                    elif month == 9:
                        month_name = 'September'
                    elif month == 10:
                        month_name = 'October'
                    elif month == 11:
                        month_name = 'November'
                    else:
                        month_name = 'December'

                    # Display calender_month

                    # Display month and year heading
                    print('\n {0} {1}'.format(month_name, year))

                    # Display rows of dates
                    if day_of_week == 0:
                        starting_col = 7
                    else:
                        starting_col = day_of_week

                    current_col = 1
                    column_width = 4
                    blank_char = ' '
                    blank_column = format(blank_char, str(column_width))

                    while current_col < starting_col:
                        print(blank_column, end='')
                        current_col += 1
                    
                    current_day = 1

                    while current_day <= num_days_in_month:
                        if current_day < 10:
                            print(format(blank_char, '3') + str(current_day), end='')
                        else:
                            print(format(blank_char, '2') + str(current_day), end='')
                        
                        if current_col < 7:
                            current_col += 1 
                        else:
                            current_col = 1
                            print()

                        current_day += 1
                    print('\n')

                except ValueError:
                    print('Please provide an integer')
        except ValueError:
            print('Please provide an integer')
        
        
        

if __name__ == '__main__':
    calender_month_format()