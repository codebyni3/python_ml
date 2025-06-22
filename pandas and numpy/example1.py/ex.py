# class father:
#     def skill(self):
#         print("coding","progmming")
# class mother:
#     def skill(self):
#         print("art", "cocking")
# class son(father,mother):
#     def skill(self):
#         father.skill(self),
#         mother.skill(self)
#         print("sports")

# x = son()
# x.skill()
 
# multilevel 

# class grandfather:
#     def house(self):
#         print("own the big house")
# class father(grandfather):
#     def car(self):
#         print("own the car")
# class son(father):
#     def bick(self):
#         print("own the bick")
# c = son()
# c.house()
# c.car()
# c.bick()


# loc() & iloc()

import pandas as pd
data = {'Brand': ['Maruti', 'Hyundai', 'Tata', 
                               'Mahindra', 'Maruti', 'Hyundai', 
                               'Renault', 'Tata', 'Maruti'], 
                     'Year': [2012, 2014, 2011, 2015, 2012, 
                              2016, 2014, 2018, 2019], 
                     'Kms Driven': [50000, 30000, 60000, 
                                    25000, 10000, 46000, 
                                    31000, 15000, 12000], 
                     'City': ['Gurgaon', 'Delhi', 'Mumbai', 
                              'Delhi', 'Mumbai', 'Delhi', 
                              'Mumbai', 'Chennai',  'Ghaziabad'], 
                     'Mileage':  [28, 27, 25, 26, 28, 
                                  29, 24, 21, 24]}
df = pd.DataFrame(data)
# print(df.loc[1])
# print(df.at[1,"City"])
# print(df.iat[1,1])

# print(df.axes[1])
df['Place']=['jaipur','ajmer','kota','jhunjhunu','ambala','jhodpur','pali','humanghadh','udaypur']

print(df)