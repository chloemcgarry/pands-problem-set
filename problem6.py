# Solution to problem 6

#Creating string
string = "The quick brown fox jumps over the lazy dog"

#Sentence 
for word in string.split()[::2]:

#Print every second word in the sentence
    print(word)