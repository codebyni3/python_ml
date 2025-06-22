import numpy as np
import matplotlib.pyplot as plt

size = 50
radius = 1
A = np.linspace(0, 2*np.pi, size)

x = radius * np.cos(A)
y = radius * np.sin(A)

fig, ax = plt.subplots()
ax.scatter(x, y, color="black", s=50)  # Fixed 'scarplot' to 'scatter'
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_title("SHOW me")  # Fixed 'ax.title' to 'ax.set_title'
# ax.axis("off")
ax.set_aspect("equal")

# set_aspect jo ki ye kam krta hai ki digram ko set krta hai 
plt.show()
