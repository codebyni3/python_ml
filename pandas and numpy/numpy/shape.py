# 2-D array shape
from traceback import print_tb
import numpy as np
# arr = np.array([[1,2,3,4],[4,5,6,7]])
# print(arr.shape)
# 2,4
arr = np.array([1,2,3,4], ndmin=4)
print(arr.shape)
print(type(arr.shape))

arr1 =np.array([[5,6,7,8],[1,2,3,4]])
for i in arr1:
     print(i)
