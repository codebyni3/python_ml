# import numpy as ni

# arr = ni.array([1,2,3,4,56,7])
# # arrw1 = ni.array_split(arr ,4)
# arrw1 = ni.split(arr, 2)

# print(arrw1)/

# hsplit , vsplit, dsplit 
# 1 horzinte 
# import numpy as np
# arr = np.array([[1,2,3,4],
#                 [5,6,7,8]])
# result = np.hsplit(arr,2)
# print(result)

# 2 vertically 

# import numpy as np
# arr = np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [19,2,42,42],
#                 [89,44,65,36]])
# result = np.vsplit(arr,4)
# print(result)

# 3 d
import numpy as np
arr = np.array([[[2,3,4],
                [5,6,8]]
                ])
result = np.dsplit(arr,3)
print(result)