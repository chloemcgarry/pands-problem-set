#Solution to problem 3

for x in range(1000, 10001):
# for all numbers in the range (1000,10001)
# range will be from 1000 to 10000 inclusive
    
    if x % 6 == 0 or x % 12 != 0:
        print (x)
# print numbers that are divisible by 6 but not by 12

