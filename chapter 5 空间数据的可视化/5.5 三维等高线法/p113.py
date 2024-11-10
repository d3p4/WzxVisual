import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig4 = plt.figure(figsize=(13, 9))
ax4 = plt.axes(projection='3d')

xx = np.arange(-6, 6, 0.1)
yy = np.arange(-6, 6, 0.1)
X, Y = np.meshgrid(xx,  yy)
Z = np.sin(np.sqrt(X**2+Y**2))

ax4.plot_surface(X, Y, Z, alpha=0.8, cmap='winter')
ax4.contour(X, Y, Z, zdir='z',  offset=-3, cmap="rainbow")

ax4.set_xlabel('X', size=16)
ax4.set_xlim(-6, 6)
ax4.set_ylabel('Y', size=16)
ax4.set_ylim(-6, 6)
ax4.set_zlabel('Z', size=16)
ax4.set_zlim(-6, 6)

plt.tick_params(labelsize=13)

plt.show()
