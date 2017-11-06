#!#!/usr/bin/env python3
''' A Calender Year Program

Displays a calendar Year for any given Year between 1800 and 2099, iclusive. 

Display Features:
    - The calender Year 
    - The day of the week that the first day falls on  
    - The number of days in the Year
'''
# Problem Analysis
########################
# TODO: Algotrithm to compute the 1st day of a given month for yrs 1800-2099
# Only the day of the week for Jan 1st of the given yr is required - the rest 
# of the days follow from knowing the n0. of days in each month (Inc. Feb 4 Leap yrs)

# TODO: Data structure to store info. allowing for the months to be dispalyed 3-across
# Lists???


# Program Design:
#################
# TODO: Program Requirements
# Request the user to enter a four-digit year to display, with appropriate input error checking

# TODO: Data Description
# The program needs to represent:
   
    # Year entered
    # Whether the year is LEAP yr or not
    # Day of the week for 1st Jan of the yr
    # No. of days in each month (accounting for leap yrs)
    # Names of each of the 12 months for display

# use nested lists for representing the calendar year. 
# The list will start out as an empty list and will be built incrementally as each new calendar month is computed. 
    
    # calendar_year = [ [ calendar_month ], [ calendar_month ], etc.] ]
    # calendar_month = [ week_1, week_2, . . ., week_k ]
        
        # Each month is represented as a list of four to six strings, 
        # with each string storing a week of the month to be displayed (or a blank line for alignment purposes).
        # The strings are formatted to contain all the spaces needed for proper alignment when displayed.
        # For example, since the first week of May 2015 begins on a Friday, the string value for this week would be,
            
            # MAY 2015
            # Sun Mon Tues Wed Thur Fri Sat
            # '                       1  2'  <-- The String


