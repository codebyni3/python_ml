import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.datasets import load_breast_cancer
lbc = load_breast_cancer()

lbc.keys()

df_feat= pd.DataFrame(lbc['data'], columns=lbc['feature_names'])
df_feat.info()

lbc['target_names']
# print(lbc)

from sklearn.model_selection import train_test_split

X=df_feat
y=lbc['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

from sklearn.svm import SVC
lm=SVC()

lm.fit(X_train, y_train)
pred= lm.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, pred))
print('\n')
print(confusion_matrix(y_test, pred))


# gridsearchcv


from sklearn.model_selection import GridSearchCV

param_grid = {'C':[0.1,1,10,100,1000], 'gamma':[1,0.1,0.01,0.001,0.0001]}

grd=GridSearchCV(SVC(), param_grid, verbose=3)

grd.fit(X_train, y_train)

grd.best_params_
grd.best_estimator_

grd_pred = grd.predict(X_test)

print(classification_report(y_test, grd_pred))

print(confusion_matrix(y_test, grd_pred))
