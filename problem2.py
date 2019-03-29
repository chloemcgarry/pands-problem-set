#Solution to Problem 2

import datetime
#Imported date/time

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

if weekday == 2 or weekday == 4:
    print ("Today begins with the letter T")
else:
    print("Today doesn't begin with the letter T")

if datetime.datetime.today().weekday() == 2 or datetime.datetime.today().weekday() == 4:
#If the day is either Tuesday or Thursday then it will print that "Today begins with the letter T"

    print ("Today begins with the letter T")
    
else:
    print("Today doesn't begin with the letter T")
#Else is used if the day is not either a Tuesday or a Thursday