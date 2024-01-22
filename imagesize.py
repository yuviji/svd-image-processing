# Simulate the Sizes of 3,000 Random Image Files

import matplotlib.pyplot as plt
import numpy as np

# Generate random data for demonstration
x_resolution = np.random.randint(100, 8000, size=3000)
y_resolution = np.random.randint(100, 8000, size=3000)
img_size = 3 * x_resolution * y_resolution / 1e6

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x_resolution, y_resolution, img_size, c='blue', marker='o', label='Image Size')

ax.set_xlabel('X-Resolution (pixels)')
ax.set_ylabel('Y-Resolution (pixels)')
ax.set_zlabel('Approximate Image Size (MB)')

# Adjust legend position
ax.legend(loc='lower right')

# Adjust view of the graph
ax.view_init(elev=20, azim=225)

ax.grid(True)
plt.show()