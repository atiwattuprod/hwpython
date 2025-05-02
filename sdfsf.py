from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


fig = plt.figure(figsize=(10, 8))

ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-4,4,41)
y = np.linspace(-4,4,41)
x, y = np.meshgrid(x,y)
z = x**2 + y**2

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Star CS-2024')

surf = ax.plot_surface(x,y,z,cmap='plasma', edgecolor='none')

min_idx = np.unravel_index(np.argmin(z, axis=None), z.shape)
min_x = x[min_idx]
min_y = y[min_idx]
min_z = z[min_idx]
ax.scatter(min_x, min_y, min_z, color='red', s=100, label="Optimal Base Location")
ax.legend()

fig.colorbar(surf, shrink=0.5, aspect=10)
ax.view_init(elev=30, azim=45)

plt.show()