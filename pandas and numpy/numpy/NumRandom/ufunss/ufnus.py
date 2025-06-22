import pandas as pd

# Create a date range
dates = pd.date_range('20230101', periods=6)

# Create a DataFrame with a datetime index
df = pd.DataFrame({'Value': [10, 20, 30, 40, 50, 60]}, index=dates)
print(df)
