import pandas as pd

# creating a dataframe
df = pd.DataFrame({'Name': {0: 'John', 1: 'Bob', 2: 'Shiela'},
                   'Course': {0: 'Masters', 1: 'Graduate', 2: 'Graduate'},
                   'Age': {0: 27, 1: 23, 2: 21}})

# Corrected value_name as a string
# df2 = pd.melt(df, id_vars=["Name"], value_name="Value")


df2 = pd.melt(df, id_vars=['Name'], value_vars=["Age"])
print(df2)

