# 12. Write a Python program to print the calendar
# of a given month and year.
# Note : Use 'calendar' module.

import calendar

v_month = input("Enter month: ")
v_year = input("Enter year: ")

print(calendar.month(int(v_year), int(v_month)))
