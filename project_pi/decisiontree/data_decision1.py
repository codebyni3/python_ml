from pyexpat import features
from matplotlib import axis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
df= pd.read_csv('decisiontree/kyphosis.csv')

X= df.drop('Kyphosis', axis=1)
y=df['Kyphosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

dree=DecisionTreeClassifier()

dree.fit(X_train, y_train)
pred= dree.predict(X_test)


print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

from sklearn.ensemble import RandomForestClassifier


rfc= RandomForestClassifier(n_estimators=200)
rfc.fit(X_train,y_train)
rfc_pred=rfc.predict(X_test)

print(confusion_matrix(y_test, rfc_pred))
print(classification_report(y_test, rfc_pred))

a=df['Kyphosis'].value_counts()
print(a) 



from IPython.display import Image
from io import StringIO
import pydot
features = list(df.columns[1:])
print(features)