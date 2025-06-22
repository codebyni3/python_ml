
# import pandas as pd
# import matplotlib.pyplot as plt

# read= pd.read_csv("selary.csv")

# name =read["Name"],
# salary = read["Salary"]

# # print(read)
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('selary.csv')
colors = df['Department'].map({
    'HR': 'red',
    'IT': 'blue',
    'Sales': 'green',
    'Finance': 'orange',
    'Marketing': 'purple'
})

plt.figure(figsize=(10, 6))
plt.barh(df['Name'], df['Salary'], color=colors)
plt.xlabel('Salary (USD)')
plt.ylabel('Employee Name')
plt.title('Horizontal Bar Chart - Employee Salaries')
plt.tight_layout()
plt.show()
