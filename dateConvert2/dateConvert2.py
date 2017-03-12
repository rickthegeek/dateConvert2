#Project: CIS 177 WEEK 8 PROJECT
#Project Location: projects\cis177\dateConvert2
#File: dateConvert2.py
#Purpose: Accept a user-entered numeric form date (07/14/1977),
#         then convert the entry to the long form date (14-July-1977)
#Revision: 1.0 / 12 MAR 2017
#Created: 12 MAR 2017
#Author: Rick Miller <rick@rickthegeek.com>

def month_convert(month_str):
    # This function will convert the digits in the given string to the month it represents
    # Note: using a dict to store the months, and using the int() function to convert the string to number
    # because the user might enter 7/14/1977, or 07/14/1977
    monthNum = int(month_str)
    months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    return months[monthNum]

# Get the input from the user
user_input = input('Please enter the date in the form MM/DD/YYYY (Example: 04/01/2013) -> ')
# now, break up the input into the month, day, and year
[user_month, user_day, user_year] = user_input.split('/')
# Now, we can join up the string to return, doing the month_convert in the process
joiner = '-' # put a dash between the day, month, and year
# Also, we are converting from string to int then back to string to change a day entry of 07 to 7
pieces = (str(int(user_day)), month_convert(user_month), user_year) # put the pieces in a sequence for the join function
output_string = joiner.join(pieces) # ...and join them
#finally, print the string!
print(user_input, 'converted to long form is:',output_string)
