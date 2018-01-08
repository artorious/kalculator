#!/usr/bin/env python3
""" A calendar Year Program
    
Displays a calendar Year for any given Year between 1800 and 2099, 
inclusive. 
Display:
    + The calendar Year 
    + The day of the week that the first day falls on  
    + The number of days in the Year
"""
# TODO: Add initial implementation of calendar year program

def get_year():
    """ () -> int
    
    Returns an integer value between 1800-2099, inclusive, or -1 
    """
    valid_input = False
    while not valid_input:
        try:
            year = int(input('Enter year [YYYY] (-1 to Quit): '))
            while (year < 1800 or year > 2099) and year != -1:
                print('Year must be between 1800 and 2099')
                year = int(input('Enter year: '))
            else:
                valid_input = True
        except ValueError as verr:
            print('Ooops...Enter year [YYYY] - {0}'.format(verr))
            continue # Promt for valid Input again
    return year
    
def check_leap_year(year):
    """ (int) -> bool

    Returns True if provided <year> a leap year, otherwise, returns False
    """
    try:
        if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 ==0)):
            leap_year = True
        else:
            leap_year = False
        return leap_year
    except Exception as err:
        print('Ooops...Expected Integers - {0}'.format(err))
        raise Exception
# Determine Day of week for 1st Jan of the yr 
# See Readme for Pseudocode Reference 
def day_of_week_jan1(year, leap_year):
    """ (int, bool) -> int

    Returns the day of the week for January 1 of provided <year>, between 
    1800 and 2099. <leap_year> is True/False. 
    """
    try:
        # Init
        century_digits = year // 100    # extract first two digits of the year
        year_digits = year % 100     # extract last two digits of the year            
        value = year_digits + (year_digits // 4)
        if century_digits == 18:
            value += 2
        elif century_digits == 20:
            value += 6
        if not leap_year:   # Adjust for leap yrs
            value += 1

        # first day day of month for Jan 1.(the days of the week for all remaining dates simply follow)
        return (value + 1) % 7    

    except Exception as err:
        print('Ooops...Bad Input - {0}'.format(err))
        raise Exception

def get_num_days_in_month(month_num, leap_year):
    """ (int, bool) -> int
    
    Returns the number of days in a given month 
    <month_num> in the range 1-12, inclusive. <leap_year> is True/False. 
    """
    # Init
    num_days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if (month_num == 2) and leap_year:
        num_days = 29
    else:
        num_days = num_days_in_month[month_num - 1]
    return num_days

# Align weeks for display
def construct_cal_month(month_num, first_day, num_days_in_month):
    """ (int, int, int) -> list

    Formats and returns calendar month for display on screen.
    <month_num> in range 1-12  
    <first_day_of_month> in range 0-6 (1-Sun, 2-Mon, ...., 0-Sat) 
    <num_days_in_month> in range 1-31
    
    Returns a list of strings of the form,
    [month_name, week1, week2, week3, week4, week5, week6]
    """
    # Init
    empty_str = ''
    blank_col = format(' ', '3')
    blank_week = format(' ', '21')
    month_names = ('January', 'February', 'March',
                    'April', 'May', 'June',
                    'July', 'August', 'September', 
                    'October', 'November', 'December')
    calendar_month = [' {0:<20}'.format(month_names[month_num - 1])]
    current_day = 1
    current_col = 1
    calendar_week = ''
    
    # Init starting column
    if first_day == 0:
        starting_col = 7
    else:
        starting_col = first_day
    # Add any needed leading spaces for first week of the month
    while current_col < starting_col:
        calendar_week = calendar_week + blank_col
        current_col += 1
    # Construct month for proper number of days
    while current_day <= num_days_in_month:
        # Store day of month in fiels of length 3
        calendar_week = calendar_week + format(str(current_day), '>3')
        # Append new week to month if at the end of week
        if current_col == 7:
            calendar_month = calendar_month + [calendar_week]
            calendar_week = empty_str
            current_col = 1
        else:
            current_col += 1
        current_day += 1
    # If there is a final week, append to constructed month
    if calendar_week != empty_str:
        calendar_month = calendar_month + [calendar_week]
    return calendar_month

# Iterate once for each of the 12 months, calling construct_cal_month() and 
# append each to list of lists
def construct_cal_year(year):
    """ (int) -> list
    
    Formats and returns calendar for dispaly on screen for the <year> in 
    range 1800-2099, inclusive. 
    
    Returns a list of strings of form,
    [year, month1, month2, month3, ...., month12]
    """
    # Init
    leap_year = check_leap_year(year)
    first_day_of_month = day_of_week_jan1(year, leap_year)
    calendar_year = [year]
    # Construct calendar from twelve constructed months
    for month_num in range(1, 13):
        num_days_in_month = get_num_days_in_month(month_num, leap_year)
        calendar_year. append(
            construct_cal_month(
                month_num, first_day_of_month, num_days_in_month))
        first_day_of_month = (first_day_of_month + num_days_in_month) % 7
    return calendar_year

# Display calendar year structure in four rows of months, three months across
def dispaly_calendar(calendar_year):
    """ (list) -> str

    Displays the provided <calendar_year> on he screen three months across.
    <calendar_year> being a list of twelve sublists of the form,
    [month_name, week1, week2, ...]
    """
    month_separator = format(' ', '8')
    blank_week = format(' ', '21')
    # dispaly year
    print('\n', calendar_year[0])
    # display months three across
    for month_index in [1, 4, 7, 10]:
        # Init
        week = 1
        lines_to_print = True
        while lines_to_print:
            # Init
            lines_to_print = False
            # print weeks of months side-by-side
            for a_col in range(month_index, month_index + 3):
                if week <= len(calendar_year[a_col]):
                    week_dates = calendar_year[a_col][week - 1]
                    print(week_dates + blank_week[len(week_dates) :], end='')
                    lines_to_print = True
                else:
                    print(blank_week, end='')
                print(month_separator, end='')
            # move to the next line
            print()
            week +=1 # Increament week


def main():
    """ Display Calender """
    terminate = False # Control program termination
    print('Display a calendar Year for any given Year between 1800 and 2099')

    while not terminate: # Continue to display calendar years until -1 entered
        year = get_year() # User Input

        if year == -1: # Exit 
            terminate = True
        else:
            calendar_year = construct_cal_year(year)
            dispaly_calendar(calendar_year)    

if __name__ == '__main__':
    main()

