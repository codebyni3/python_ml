# from sklearn.metrics import 
# import numpy as np
from turtle import color
from matplotlib import markers
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
y_true = [3.0, -0.5, 2.0, 7.0]
y_pred = [2.5, 0.0, 2.1, 7.8]

mes =mean_absolute_error(y_true, y_pred)
print("Mean Absolute Error :", mes)

plt.figure(figsize=(8,4))
plt.plot(y_true,marker='o', color='blue')
plt.plot(y_pred, marker='*', color='green')
plt.title("Mean Absolute Error")
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.legend()
plt.show()
