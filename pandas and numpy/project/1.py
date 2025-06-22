"""from re import split
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as ptl

# Load dataset
df = pd.read_csv("D:/pandas and numpy/employee_meal_data.csv")  # Use forward slashes or raw string

# Define custom colors for each day
day1 = {
    'Sat': 'blue',  
    'Thur': 'green',
    'Sun': 'yellow',
    'Fri': 'red'
    
}

# Countplot for gender
# sns.countplot(x='sex', data=df, palette={'Male': 'blue', 'Female': 'green'})

# Boxplot for total_bill by day
# sns.boxplot(x='day', y='total_bill', data=df, palette= day1)
# sns.boxplot(x='day', y='total_bill', data=df, hue='smoker')
# sns.violinplot(x='day', y='total_bill', data=df, hue='sex', palette={'Male': 'lightblue', 'Female':'lightgreen'})


# Show the plots
# ptl.show()
sns.stripplot(x='day', y='total_bill', data= df,hue='sex', split=True)
sns.pairplot(data=df)
sns.pairplot(df)
g=sns.PairGrid(df)
g.map(ptl.bar)

sns.countplot(x='sex', data=df)
ptl.show()"""




import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('employee_meal_data.csv')
df.head()
sns.countplot(x='sex', data=df)
plt.show()