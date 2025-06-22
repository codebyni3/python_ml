# importing library
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])

fig, ax = plt.subplots(2,2)

# ax[0,0].plot(arr, arr)
# ax[0,1].plot(arr, arr*arr)
# ax[1,0].plot(arr, arr*2)
# ax[1,1].plot(arr, arr)

# ax[0,0].set_title("toi")
# ax[0,1].set_title("toi")
# ax[1,0].set_title("toi")
# ax[1,1].set_title("toi")

title=["A","B","C","D"]
y=[x, x*x, x*2, x*x*x]

for i in range(4):
    plt.subplots(2,2)
    plt.plot(x, y[i])
    plt.gca().set_title(title[i])


fig.tight_layout()
plt.show()