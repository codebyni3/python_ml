# class calcutor:
#     def add (self,a,b):
#         return a+b
#     def subtact(self,a,b):
#         return a-b
# s1 = calcutor()
# print(s1.add(3,4))
# print(s1.subtact(4,3))/


# class Employee:
#     def __init__(self,name,id , depatment):
#           self.name = name
#           self.id = id
#           self.depatment=depatment
#     def display(self):
#         print(f"name:- {self.name}")
#         print(f"id:- {self.id}")
#         print(f"depatment:- {self.depatment}")
# s1=Employee("nitin",101,"python develper")
# s1.display()


import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 6, 8, 3, 7],
    'B': [5, 2, 9, 4, 1]
})

# Select rows where 'A' is greater than 4
result = df[df['A'] > 4]
print(result)
