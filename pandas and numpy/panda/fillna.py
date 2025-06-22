# import pandas as pd

# data = pd.read_csv("employee_data_with_missing.csv")

# # Optionally check missing data
# Missing_data = data[data.isnull().any(axis=1)]
# Missing_data1= Missing_data.fillna({'Department':'none'})
# Missing_data1= Missing_data.fillna({'Salary':'BANK ERROR'})


# print(Missing_data1)

# # Correct pd.melt usage
# # df = pd.melt(data, value_vars=['Salary'], value_name='Name')
# # print(df)
import numpy as np

print(np.__version__)
