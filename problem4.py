#solution to problem 4

x = int(input("Please enter a positive integer"))
# User asked to input a positive integer and assigned to x
while x != 1:

#Divide x by 2 if even.
    if x % 2 == 0:
        x = x // 2

        print (x)

else:
#Muliplying x by 3 and adding 1 if odd.
    x = x * 3 + 1
    
    print (x)
#Printing the value of x.