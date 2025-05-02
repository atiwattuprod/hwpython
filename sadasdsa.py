from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# Initialize the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create numerical arrays for x and y
x = np.linspace(-4, 4, 41)
y = np.linspace(-4, 4, 41)
X, Y = np.meshgrid(x, y)

# Calculate Z as the sum of squares of X and Y
Z = X**2 + Y**2

# Set axis labels and plot title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Z')
ax.set_title('Star CS-2024')

# Find and plot the minimum point on the surface
min_idx = np.unravel_index(np.argmin(Z, axis=None), Z.shape)
min_x = X[min_idx]
min_y = Y[min_idx]
min_z = Z[min_idx]
ax.scatter(min_x, min_y, min_z, color='red', s=100, label="Optimal Base Location")

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap=cm.jet, antialiased=False)

# Add color bar
fig.colorbar(surf, shrink=0.5, aspect=10)

# Display the legend
ax.legend()

# Show the plot
plt.show()
