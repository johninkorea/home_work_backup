import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N=200
x = np.linspace(-10, 10, N)
y = np.linspace(-10, 10, N)
print(x.shape,y.shape)
X, Y = np.meshgrid(x,y)
print(X.shape,Y.shape)
z= 10-(X**2+(Y/2)**2)
#z= 5-5*np.sin((((X/5)**2+(Y/7)**2)))**2


fig = plt.figure(figsize=(8,8))
im = plt.imshow(z, aspect='equal', extent=(-10,10,-10,10))
levels=np.arange(-100, 10, 5)
#levels=np.arange(0, 5, 1)
ctr = plt.contour(z, levels,  extent=(-10,10,-10,10))

plt.show()