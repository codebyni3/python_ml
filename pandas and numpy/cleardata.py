import pandas as pd
df = pd.read_csv("dara.csv")
pr=df.drop([0,3],axis=0)
print(pr.reset_index())


# import pandas as pd

# df = pd.read_csv('dara.csv')

# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# df.dropna(subset=['Date'], inplace=True)
# print(df.to_string())
