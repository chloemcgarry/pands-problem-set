import datetime
d = datetime.datetime.today().weekday()
print ("Enter the day number - 0 is Sunday, 1 is Monday etc.")

if d == 2 or d == 4 :
    print ("Today begins with the letter T")
    
    if d == 0 or d == 1 or d == 3 or d == 5 or d == 6 :
    
        print("Today doesn't begin with the letter T")
