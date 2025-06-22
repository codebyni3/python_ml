
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv('Logisitc/advertising.csv')
# describe
# df.describe()
# print(x)

# histogram bar

"""sns.histplot(df['Age'], bins=30)
# or

df['Age'].plot.hist(bins=30)
"""
# joinplot se area income verse age
# sns.jointplot(x='Age', y='Area Income', data=df)

# create a jointplot showing the kde distributions of Daily Time spent on site vs Age

# sns.jointplot(x='Age',y='Daily Time Spent on Site', data=df, kind='kde', color='red')


# create a jointplot of "Daily Time Spent on Site" VS "Daily Internet Usege"

# sns.jointplot(x='Daily Time Spent on Site', y='Daily Internet Usage', data=df, color='green')

# sns.pairplot(df, hue='Clicked on Ad')

"""Logistic Regression 

Split the data into training set and testing set using train_test_split
"""

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X= df[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','Male']]
y=df['Clicked on Ad']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

lm= LogisticRegression()
lm.fit(X_train, y_train)

pred = lm.predict(X_test)

print("Classification repot")
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))


sns.heatmap(confusion_matrix(y_test, pred), annot=True,yticklabels=False ,fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title("Confusion Matrix")

plt.show()
