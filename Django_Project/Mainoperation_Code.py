# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 18:08:58 2025

@author: Deepa
"""

import calendar
from datetime import datetime


def calculate_days(sdate, edate):
    d1 = datetime.strptime(sdate,"%Y-%m-%d")
    d2 = datetime.strptime(edate,"%Y-%m-%d")
    return abs(d2-d1).days

# def month1_days(y,m):
    
#     days = calendar.monthrange(y,m)[1]
#     return days


# #user input
# year1= int(input("Enter the year:"))
# month1= int(input("Enter the month:"))


# result1 = month1_days(year1,month1)
# month_name1 = calendar.month_name[month1]  # converts  → month
# print(f'Number of days in {month_name1} of {year1}:',result1)



# def month2_days(y,m):
    
#     days = calendar.monthrange(y,m)[1]
#     return days

# #user input
# year2= int(input("Enter the year:"))
# month2= int(input("Enter the month:"))

# result2 = month2_days(year2,month2)
# month_name2 = calendar.month_name[month2]  # converts  → month
# print(f'Number of days in {month_name2} of {year2}:',result2)


# print(f'Number of days between {month_name1} & {month_name2} is:', result1 + result2)
