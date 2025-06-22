# import random

# matrix = [[random.random()for i in range(4)]for j in range(3)]
# suim= [sum(row)/len(row)for row in matrix]
# print(suim)

# lst = [1,4,6,2,9,5]
# # min index val, max
# min_val = lst.index(min(lst))
# max_val = max(lst)
# print(min_val)
# print(max_val)

# matrix = [[1 if i == 0 or i == 4 or j == 0 or j == 4 else 0 for j in range(5)] for i in range(5)]
# print(matrix)
# import math
# lst = [1, 2, 3, 4, 5]
# exponential_lst = [math.exp(x) for x in lst]
# print(exponential_lst)

# port = [[1 if i==0 or i == 4 or j==0 or j==4 else 0 for j in range(5)]for i in range(5)]
# print(port)

#Find the unique values and their counts in a list.
 
# lst = [1,2,4,1,2,3,4,5,1,4]
# unick_num= list(set(lst))
# count = {x: lst.count(x)for x in lst}
# print(unick_num)
# print(count)


#Create a 3x3 list of lists with values ranging from 0 to 8.

# matrix = [[i+j*3 for i in range(3)]for j in range(3)]
# print(matrix) 

# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.dropna())
import pandas as pd

df = pd.read_csv('data1.csv')

df.fillna(20,inplace=True)

print(df.to_string())
