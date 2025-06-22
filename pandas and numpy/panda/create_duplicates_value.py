import pandas as pd

arr = pd.DataFrame({
    "EmployeeID":[111,112],
    "Name":["Rajkumar","Deepak"],
    "Department":["Back-end deloper","SEO Executive"],
    "Position":["Manager","Manager"],
    "Salary":[34500, 28900]
})

# type 1 
# arr1=  pd.concat([arr,arr],ignore_index=True)
# print(arr1)


# type 2
arr1 = arr.loc[arr.index.repeat(3)].reset_index(drop=True)
print(arr1)
