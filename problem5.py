# Solution to problem 5
# Reference:https://www.programiz.com/python-programming/examples/prime-number

x = int(input("Enter a positive integer"))

if x > 1:
    for i in range(2, x):
        #checking for factors of the input
        if (x % i) == 0:
            print(x, "is not a prime number")
            print(x, "times", x //i, "is", x)
        break
    else: 
        print(x, "is a prime number")
else:
    print(x, "is not a prime number")