import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
#a=iris.head()
# sns.pairplot(iris, hue='species',palette='Dark2')

# create a kde plot of sepal_length versus sepal width for setosa species of flower.

"""seto = iris[iris['species']=='setosa']
sns.kdeplot(x=seto['sepal_width'], y=seto['sepal_length'], fill=True, cmap='twilight_r' )"""

# train text split

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

X = iris.drop('species', axis=1)
y=iris['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# call the SVC()

from sklearn.svm import SVC
svc_model= SVC()
svc_model.fit(X_train, y_train)
pred= svc_model.predict(X_test)

print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))


from sklearn.model_selection import GridSearchCV

param_grid= {'C':[0.1,1,10,100,1000], 'gamma':[1,0.1,0.01,0.001,0.0001]}
gsv = GridSearchCV(SVC(),param_grid,verbose=3)    # param_grid , SVC() 

gsv.fit(X_train, y_train)
gsv_pred = gsv.predict(X_test)

print(classification_report(y_test, gsv_pred))
print(confusion_matrix(y_test, gsv_pred))

plt.show()