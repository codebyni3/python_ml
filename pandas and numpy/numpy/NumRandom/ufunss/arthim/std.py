# import numpy as np

# arr = np.array([1,2,3,4,44])
# # result = np.std(arr)
# result= np.mean(arr)
# print(result)


from matplotlib import axis
import numpy as np

a1 = np.array([1,2,3])
a2= np.array([4,5,6])
s1= np.sum([a1,a2])
s2 =np.sum([a1,a2], axis=1)
s3= np.cumsum([a1,a2])
s4= np.cumprod([a1, a2])
print(s1)
print(s2)
print(s3)
print(s4)