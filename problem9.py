# Solution to problem 9

#User inputs file name, assigning it to text
text = input("Please enter the file: ")

with open(text) as f:

#For each line in the file
        for i, line in f:

#Prints every even numbered line in the file
                if i % 2 == 0:
                        print(line)