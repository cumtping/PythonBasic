#!/usr/bin/python
# -*- coding: UTF-8 -*-
# http://www.runoob.com/python/python-100-examples.html
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))
print ('your input: ', year, "年", month, "月", day, "日")

is_leap_year = ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))
print ('is_leap_year = ', is_leap_year)

# Define array, use [] or (), what's the difference?
# There is only tuple and list in Python, but no array,
# tuple aa=tuple(1,2,3)； cann't be changed once created, cann't call append and pop,
# but it's more efficent than list; it's more suit to save constants;
# list can do what tuple cann't do.
if is_leap_year:
  days_in_months = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
else:
  days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

which_day_of_year = 0
if month == 1:
  which_day_of_year = day
else:
  for i in range(1, month):
    print ('i=', i, 'days_in_months[i-1]=', days_in_months[i-1])
    which_day_of_year += days_in_months[i-1]
  which_day_of_year += day

print ('which_day_of_year=', which_day_of_year)
  


