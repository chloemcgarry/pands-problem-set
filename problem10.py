#Solution to Problem 10

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.colors as colour


x = np.arange(0.0, 4.0, 0.01)

y_1 = x
y_2 = x ** 2
y_3 = 2 ** x

plt.plot([0, 1, 2, 3, 4], colour = "red")
plt.plot([0, 1, 4, 9,16], colour = "blue")
plt.plot([1, 2, 4, 8, 16], colour = "green")


plt.xlabel("X")
plt.ylabel("Y")

plt.title("Plot of Functions - y = x, y = x ** 2, y = 2 ** x")

plt.savefig("Plot of Functions")

plt.show()