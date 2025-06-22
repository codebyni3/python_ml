# linear Resgression Project 

from annotated_types import Predicate
from narwhals import col
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

Customers = pd.read_csv('Ecommerce_Customers')
# Customers.head()
# A=Customers.describe()
# B=Customers.info()
# print(B)

# sns.jointplot(data=Customers, x='Time on Website', y= 'Yearly Amount Spent')
# sns.jointplot(data=Customers, x='Time on App', y='Yearly Amount Spent')

# sns.jointplot(data=Customers, x='Time on App', y='Yearly Amount Spent',kind='hex' )

"""let explore these types of relationships across the entire data set. Use Pairplot to recrete  the plot below. """
# sns.pairplot(Customers)

"""length of membership"""
# sns.lmplot(data=Customers,x='Length of Membership', y='Yearly Amount Spent')

""" Training and Testing Data"""

X=Customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
y= Customers['Yearly Amount Spent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

"""Trining the Model"""

lm = LinearRegression()
lm.fit(X_train, y_train)

lm.coef_
""" predicting test data """
predictions=lm.predict(X_test)

plt.scatter(y_test, predictions)
plt.xlabel('y Test (true Values)')
plt.ylabel("Prediction Values")

"""Evaluting the model"""

print("MAE:", metrics.mean_absolute_error(y_test, predictions))
print("MSE:", metrics.mean_squared_error(y_test, predictions))
print("RMSE:", np.sqrt(metrics.mean_squared_error(y_test, predictions)))

print(metrics.explained_variance_score(y_test, predictions))
""" Residuls 
   plot a histogram of the residuals and make sure it looks normally distributed . use either
   seaborn displot or just plt.hist()
"""
sns.displot((y_test - predictions), bins= 90)

#  console
cdf= pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])
print(cdf)
plt.show()