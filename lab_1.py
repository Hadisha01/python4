from datetime import date
import datetime

import calendar


current_datetime = datetime.datetime.now()
print("a)current date and time:",current_datetime)


# date object of today's date
today = date.today() 

print("b)Current year:", today.year)
print("c)Current month:", today.month)
print("d)week day number",current_datetime.strftime("%W"))
print("e)weekday of the week:",calendar.day_name[current_datetime.weekday()])
print("f)day of the year:", current_datetime.strftime("%j"))
print("g)day of month:", current_datetime.strftime("%d"))
print("h)day of week:", current_datetime.isoweekday())

