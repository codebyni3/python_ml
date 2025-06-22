import pandas as pd
# data = pd.DataFrame({
#     "EmployeeID":[111,112],
#     "Name":["Rajkumar","Deepak"],
#     "Department":["Back-end deloper","SEO Executive"],
#     "Position":["Manager","Manager"],
#     "Salary":[34500, 28900]
# })


# data.to_csv("selary.csv", mode='a', header=False, index=False)
data=pd.read_csv("selary.csv")
# data1=data[data["Name"]=='Edward']['Salary']
# data1= data.groupby('EmployeeID')['Salary'].mean()
data1= data['Salary'].nunique()
print(data1)