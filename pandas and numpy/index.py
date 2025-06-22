# import pandas as pd

# d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1, 11]}
# df = pd.DataFrame(data=d)

# print("Original DataFrame")
# print(df)

# # Using iloc
# s1 = df.iloc[1, :]

# # Alternatively, you can directly reference the column by name
# #s1 = df['col1']

# print("\n1st column as a Series:")
# print(s1)
# print(type(s1)) 


# import pandas as pd
# s = pd.Series(['100', '200', 'python', '300.12', '400'])
# print("Original Data Series:")
# print(s)
# s2 = pd.Series(['nitin','900'])
# new_s = pd.concat([s,s2])
# print(new_s)

import pandas as pd
# s = pd.Series([0,1,2,3,4,5,6,7,8,9,10])
# print(s)
# n=6
# new_s = s[s<n]
# print(new_s)
import numpy as np
# s = pd.Series([1,2,3,4,5])
# s1=pd.Series([2,4,6,8,10])
# print(s)
# print(s1)
# # s2= s[~s.isin(s1)]
# # print(s)
# print("\n another given series")
# s11 = pd.Series(np.union1d(s,s1))
# s12= pd.Series(np.intersect1d(s,s1))
# result = s11[~s11.isin(s12)]
# print(result)

# import pandas as pd
import numpy as np

# Sample data with NaN values
data = {
    'Age': [25, 30, np.nan, 28, 35, np.nan, 40],
    'Score': [88, 92, 85, np.nan, 90, 95, np.nan]
}
df = pd.DataFrame(data)
print(df)

mear = df['Age'].mean()
df['mear_num']= df['Age'].fillna(mear)
median_val = df['Age'].median()
df['mear_median']= df['Age'].fillna(median_val)
mode_val = df['Age'].mode()[0]
df['m_num']= df['Age'].fillna(mode_val)
print(df)

