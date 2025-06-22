from turtle import color
from matplotlib import markers
from matplotlib.lines import lineStyles
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
df= pd.read_csv('Knn/Classified Data')

scaler = StandardScaler()
# first binary ko drop kiya
scaler.fit(df.drop('TARGET CLASS', axis=1))
scaler_feat= scaler.transform(df.drop('TARGET CLASS', axis=1))

df_feat = pd.DataFrame(scaler_feat,  columns=df.columns[:-1])

df_feat.head()

X= df_feat
y= df['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# KNeighborsClassifier

kn= KNeighborsClassifier(n_neighbors=1)
kn.fit(X_train, y_train)

pred=kn.predict(X_test)

# 

print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))

#  k 

error_rate = []
for i in range(1, 40):
    knn= KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    
    # ab error_rate me append krte (add krte hai )
    error_rate.append(np.mean(pred_i != y_test))

    # matplot 
knn= KNeighborsClassifier(n_neighbors=17)
knn.fit(X_train, y_train)
pred_i = knn.predict(X_test)
print(classification_report(y_test, pred_i))

plt.figure(figsize=(6,10))
plt.plot(range(1,40), error_rate, color='blue', marker='o',linestyle='--' )

plt.title("Error vs K value")
plt.xlabel("K")
plt.ylabel("Error ")

plt.show()