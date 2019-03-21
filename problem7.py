# Solution to problem 7

number = float(input("Enter a positive integer"))
#User inputs a positive integer
#Positive integer is assigned a floating number

squareroot = number ** 0.5
# floating number is raised to 0.5 (which is the square root)

print(squareroot)
#Print square root to find the square root of the input
approx = float("0.1f" % (squareroot))
#To find the approximation of the square root