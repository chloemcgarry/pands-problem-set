#Solution to problem 8


import datetime

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

if mnth == 1:
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
                            elif == 8:
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


day = datetime.datetime.today().day

if d_day == 1 or d_day == 21 or d_day == 31:
    d_day = str(d_day) + "st"
    elif d_day == 2 or d_day == 22:
        d_day = str(d_day) + "nd"
        elif d_day == 3 or d_day = 23:
            d_day = str(d_day) + "rd"
            else:
                d_day = str(d_day) + "th"

                print(d_day)


current_hr = datetime.datetime.today().hour
current_min = datetime.datetime.today().minute

if current_hr <=12:
    time = str(current_hr) + ":" + str(current_min) + "am"
    else:
        time = str(current hr - 12) + ":" + str(current_min) + "pm"

        print(time)


day_date_time = f"{weekday_name}, {month} {d_day} {datetime.datetime.today().year}, at {time}"

print(day_date_time)