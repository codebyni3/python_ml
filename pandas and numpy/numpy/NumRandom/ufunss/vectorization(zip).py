"""
    Without ufunc, we can use Python's built-in zip() method:
x=[1,2,3,4]
y=[2,4,5,7]
z=[]
for i,j in zip(x,y):
  z.append(i+j)
print(z)
"""
"""
NumPy has a ufunc for this, called add(x, y) that will produce the same result.


import numpy as np

x=[2,4,5,6]
y=[4,6,7,8]
z=np.add(x ,y)
print(z)
print(type(z))

"""
# create own ufunc
"""
import numpy as np

# print(type(np.concatenate))
# print(type(np.add))
if type(np.add)== np.ufunc:
    print("win")
else:
    print("low")
"""
import numpy as np

arr1= np.array([1,4,6,8])
arr2= np.array([9,4,9,2])
result= np.add(arr1 , arr2)
print(result)
