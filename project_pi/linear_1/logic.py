from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
# data load 
df=pd.read_csv("data")
X = df[['Age', 'Weight', 'BloodPressure']]
y=df['HasDiabetes']


# data = load_iris()
# X= data.data
# y=(data.target==0).astype(int)  #binary classification (yes/ no  0 ya 1 )

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

lm = LogisticRegression()
lm.fit(X_train, y_train)

# preducatoin

y_pred= lm.predict(X_test)

print("Accuracy", accuracy_score(y_pred, y_test))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

