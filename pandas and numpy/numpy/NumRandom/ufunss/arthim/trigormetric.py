import numpy as np

arr = np.array([90, 180])
x = np.deg2rad(arr)

print(np.around(x, 2))


arr2 = np.around(np.cos(np.pi/3), 2)
print(arr2)
 
 