# Solution to problem 5

# ASking user to input a positive integer. Assigning the it x
x = int(input("Enter a positive integer"))

if x > 1:
    for i in range(2, x):
        #checking for factors of the input
        if (x % i) == 0:

#Prints x isn't a prime then break the loop once a factor of i is found.
            print(x, "is not a prime number")
            print(x, "times", x //i, "is", x)
        break


    else: 
# Prints x is a prime number if no factors are found
    print(x, "is a prime number")
else:
    print(x, "is not a prime number")