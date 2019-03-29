#Solution to Problem 10

#import pyplot from matplotlib
#Import numpy from matplotlib

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.colors as colour

# Assigning x values
x = (0, 4, 1)
#Functions to be plotted
y_1 = x
y_2 = x ** 2
y_3 = 2 ** x


#Plot of functions 
y_1 = plt.plot(0., 4., 0.1)
y_2 = plt.plot(0., 4., 0.1)
y_3 = plt.plot(0., 4., 0.1)

#Plotting functions using colour coded symbols
plt.plot(x, x, 'r--', x, x ** 2, 'bs', x, 2 ** x, 'g^')

#Axis labels
plt.xlabel("X")
plt.ylabel("Y")

#Display grid
plt.grid(True)

#Giving title to plot
plt.title("Plot of Functions - y = x, y = x ** 2, y = 2 ** x")

#Saving plot of functions
plt.savefig("Plot of Functions")

plt.show()