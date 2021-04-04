import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D

N=200
x = np.linspace(-10, 10, N)
y = np.linspace(-10, 10, N)
X, Y = np.meshgrid(x,y)
z= 5-5*np.cos((((X/5)**2+(Y/5)**2)))**2

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, z, cmap=cm.viridis)
ax.set_zlim3d(-1.,6)
plt.colorbar(surf, shrink=0.5, aspect=10)

plt.show()