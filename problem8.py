# Solution to problem 8


import datetime
# Importing datetime module

weekday = datetime.datetime.today().weekday()

if weekday == 0:
    # Numbering the weekdays
    weekday_name = "Monday"
    # Then assigning names to the numbers.

elif weekday == 1:
    weekday_name = "Tuesday"
elif weekday == 2:
    weekday_name = "Wednesday"
elif weekday == 3:
    weekday_name = "Thursday"
elif weekday == 4:
    weekday_name = "Friday"
elif weekday == 5:
    weekday_name = "Saturday"
elif weekday == 6:
    weekend_name = "Sunday"
    print(weekday_name)


mnth = datetime.datetime.today().month

# Numbering the months (mnth), as the appear on DD/MM/YYYY
if mnth == 1:

    # Assigning names to the month number - (mnth given a month)
    month = "January"
elif mnth == 2:
    month = "February"
elif mnth == 3:
    month = "March"
elif mnth == 4:
    month = "April"
elif mnth == 5:
    month = "May"
elif mnth == 6:
    month = "June"
elif mnth == 7:
    month = "July"
elif mnth == 8:
    month = "August"
elif mnth == 9:
    month = "September"
elif mnth == 10:
    month = "October"
elif mnth == 11:
    month = "November"
elif mnth == 12:
    month = "December"
    
    print(month)

#Day's date

day = datetime.datetime.today().day

#Making string to ensure st,nd, rd or th is included at the end of the date

if day == 1 or day == 21 or day == 31:
    d_day = str(day) + "st"
elif day == 2 or day == 22:
    d_day = str(day) + "nd"
elif day == 3 or day == 23:
    d_day = str(day) + "rd"
else:
    d_day = str(day) + "th"
    
    print(d_day)


#Time in 12hr format.
current_hr = datetime.datetime.today().hour
current_min = datetime.datetime.today().minute

#Creating am/pm depending on time of day in 12hr format
if current_hr <=12:
    time = str(current_hr) + ":" + str(current_min) + "am"
else:
    time = str(current_hr - 12) + ":" + str(current_min) + "pm"
    print(time)


day_date_time = f"{weekday_name}, {month} {d_day} {datetime.datetime.today().year}, at {time}"

print(day_date_time)