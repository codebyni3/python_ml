import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

df =pd.read_csv("Knn/KNN_Project_Data")
# sns.pairplot(df,hue='TARGET CLASS',palette='coolwarm')
# standarscaler

scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))

scaler_base= scaler.transform(df.drop('TARGET CLASS', axis=1))
# remore binarry data
df_feat = pd.DataFrame(scaler_base, columns=df.columns[:-1])

X=df_feat
y=df['TARGET CLASS']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(scaler_base,df['TARGET CLASS'],test_size=0.3)

kn=KNeighborsClassifier()
kn.fit(X_train, y_train)
pred = kn.predict(X_test)

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

"""
There is a comparison between 2 particles
"""

error_df=[]
for i in range(1,40):
    knn= KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i= knn.predict(X_test)
    error_df.append(np.mean(pred_i != y_test))



knn= KNeighborsClassifier(n_neighbors=17)
knn.fit(X_train, y_train)
pred_i = knn.predict(X_test)
print(classification_report(y_test, pred_i))

plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_df, color='red',marker='o', linestyle='--')

plt.title("Error Vs K")
plt.xlabel("k")
plt.ylabel("Error")
# sns.pairplot(data=df)

plt.show()