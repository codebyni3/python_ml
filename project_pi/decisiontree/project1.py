import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("decisiontree/loan_data.csv")
df.info()
A= df.describe()
B=df.head()
print(B)

# EXPLORATORY DATA ANALYSIS

"""plt.figure(figsize=(10, 6))
df[df['credit.policy']==0]['fico'].hist(bins=30, color='red', alpha=0.6, label='credit.policy=0')
df[df['credit.policy']==1]['fico'].hist(bins=30, color='green', alpha=0.6, label='credit.policy=1')

plt.title("Exploratory data analysis")
plt.xlabel("FICO")
plt.legend()
plt.show()"""


# not.fully.paid
"""plt.figure(figsize=(10,6))
df[df['not.fully.paid']==1]['fico'].hist(bins=35, color='blue', label='not.fully.paid=1', alpha=0.6)
df[df['not.fully.paid']==0]['fico'].hist(bins=35, color='orange', label='not.fully.paid=0', alpha=0.6)

plt.title("not.fully.paid")
plt.legend()

plt.show()"""


# Create a countplot using seaborn showing the counts of loans by purpose
#  with the color hue defined by not.fully.paid.

"""plt.figure(figsize=(10,6))
sns.countplot(data=df, x='purpose',hue='not.fully.paid', palette='Set1' )
plt.show()"""

# ** Let's see the trend between FICO score and interest rate. 
# Recreate the following jointplot.**


"""sns.jointplot(x='fico', y='int.rate', data=df, color='red')
plt.show()"""


# ** Create the following lmplots to see if the trend differed between not.fully.paid and credit.policy. 
# Check the documentation for lmplot() if you can't figure out how to separate it into columns.**

"""plt.figure(figsize=(11,6))
# sns.lmplot(y='int.rate',x='fico' ,data=df, hue='not.fully.paid', col='credit.policy')
sns.lmplot(y='int.rate',x='fico' ,data=df, hue='credit.policy', col='not.fully.paid')
plt.show()"""


# part 2 
"""
SETTING UP THE DATA

## Categorical Features

Notice that the **purpose** column as categorical

That means we need to transform them using dummy variables so sklearn will be able to understand them. Let's do this in one clean step using pd.get_dummies.

Let's show you a way of dealing with these columns that can be expanded to multiple categorical features if necessary.

**Create a list of 1 element containing the string 'purpose'. Call this list cat_feats.**
"""


cat_feat= ['purpose']

final_data= pd.get_dummies(df, columns=cat_feat, drop_first=False)
E=final_data.head()
print(E)

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


X= final_data.drop('not.fully.paid', axis=1)
y=final_data['not.fully.paid']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

dree= DecisionTreeClassifier()
dree.fit(X_train, y_train)
dree_pred= dree.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, dree_pred))
print(confusion_matrix(y_test, dree_pred))


# Traning the random forest model
# **Create an instance of the RandomForestClassifier class and fit it to our training data from the previous step.**

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=600)

rfc.fit(X_train, y_train)
rfc_pred = rfc.predict(X_test)

print(classification_report(y_test, rfc_pred))
print(confusion_matrix(y_test, rfc_pred))
