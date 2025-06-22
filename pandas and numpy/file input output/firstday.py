# question1
# Write a Pandas program to select rows where the value in the 'A' column is greater than 4.

import pandas as pd
# data = {
#     'A':[1, 6, 8, 3, 7],
#     'B':[5, 2, 9, 4, 1]
# }

# df = pd.DataFrame(data)
# new_as = df[df['A']>4]
# print(new_as)


# 2. Write a Pandas program to select only the 'X' and 'Y' columns from the DataFrame.
# data= {
#     'X':[1,2,4,5],
#     'Y':['A','S','D','W'],
#     'Z':[4,5,7,9]
# }
# df1= pd.DataFrame(data)
# df=df1[['X','Y']]
# print(df)/

# 3.Write a Pandas program to set a MultiIndex and access specific data using it.


# data= {
#     'X':[1,2,4,5],
#     'Y':['A','S','D','W'],
#     'Z':[4,5,7,7]
# }
# df= pd.DataFrame(data)
# de_ds= df.set_index(['Y','Z'])
# print(de_ds)
# print("\nSales in Canada in 2021:")
# print(de_ds.loc[('S',5)])

#4. Write a Pandas program to slice DataFrame based on MultiIndex levels.

# data={
#     'a':[1,2,5,7,9],
#     'b':[12,5,3,8,10],
#     'c':['one', 'one', 'two', 'two', 'one']
# }
# fe= pd.DataFrame(data)
# df=fe.set_index(['a','c'])

# result= df.loc[(2, 'one')]

# print(result)/
# import pandas as pd

# Create a DataFrame
# df = pd.DataFrame({
#     'A': [1, 6, 8, 3, 7],
#     'B': [5, 2, 9, 4, 1],
#     'C': ['one', 'one', 'two', 'two', 'one']
# })

# # Set MultiIndex
# df = df.set_index(['C', 'A'])

# # Slice DataFrame
# result = df.loc['one']
# print(result)




# 6.
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 6, 8, 3, 7],
    'B': [5, 2, 9, 4, 1],
    'C': ['one', 'one', 'two', 'two', 'one']
})

# Set MultiIndex
df = df.set_index(['C', 'A'])

# Slice DataFrame
result = df.reindex()
print(result)
