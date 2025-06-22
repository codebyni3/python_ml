from turtle import color
from annotated_types import Predicate
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

data= pd.read_csv("social_media")
# df=data.head()
# sns.jointplot(x='sex',y='day', data=df)
# sns.displot(df['sex'], kde=False, color='red')
X=data[['Age','EstimatedSalary']]
y=data['Purchased']

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lm= LogisticRegression()
lm.fit(X_train, y_train)

# prediction

Y_pred =lm.predict(X_test)

cm=confusion_matrix(y_test, Y_pred)
print(classification_report(y_test, Y_pred))

# color['Male':'red', 'Female':'green']
sns.barplot(data=data, x='Gender', y='Age',palette={'Male': 'red', 'Female': 'green'})
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix (Linear Regression)")
plt.show()