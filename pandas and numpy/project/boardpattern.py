from matplotlib import axis, figure
import numpy as np
import matplotlib.pyplot as plt

def numpor(size=8):
    board=np.indices((size, size)).sum(axis = 0)%2
    plt.figure(figsize=(6,6))
    plt.imshow(board, cmap="gray")

    plt.xticks([])
    plt.yticks([])
    plt.title("card board ")
    plt.show()

numpor()
