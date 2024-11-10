import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 31, 1)
y1 = 3*np.sin(2*x)+2*x+1
y2 = 2*np.cos(2*x)+3*x+9

plt.plot(x, y1)
plt.plot(x, y2)

plt.show()


