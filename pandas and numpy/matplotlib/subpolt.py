# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 50, 100)

# fig, axes = plt.subplots(2, 2, figsize=(9, 5))

# axes[0, 0].plot(x, np.sin(x))
# axes[0, 0].set_title("Sine")

# axes[0, 1].plot(x, np.cos(x))
# axes[0, 1].set_title("Cosine")

# axes[1, 0].plot(x, np.tan(x))
# axes[1, 0].set_title("Tangent")

# axes[1, 1].plot(x, np.exp(-x))
# axes[1, 1].set_title("Exponential Decay")

# plt.tight_layout()
# plt.show()

# x = np.linspace(1,20, 30)

# fig, ax = plt.subplots(2,2, figsize=(10,2))
# ax[0,0].plot(x, np.sin(x))
# ax[0,0].set_title("sin")

# ax[0,1].plot(x, np.cos(x))
# ax[0,1].set_title("cos")

# ax[1,0].plot(x, np.tan(x))
# ax[1,0].set_title("tan")

# ax[1,1].plot(x, np.exp(-x))
# ax[1,1].set_title("tan")

# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt

# Sample data
time = [0, 1, 2, 3, 4, 5]
temperature = [25, 27, 29, 31, 28, 26]

# Create a figure and axes
fig, ax = plt.subplots()

# Create a line plot
ax.plot(time, temperature, marker='o', linestyle='--', 
        color='b', label='Temperature')

# Add labels and title
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Temperature Variation Over Time')

# Add a legend
# ax.legend()

# Display the plot
plt.show()