import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score,confusion_matrix


df= pd.read_csv('Logisitc/titanic_train.csv')

# plt.figure(figsize=(10,4))
# sns.boxplot(x='Pclass', y='Age', data= df,)
 
def image_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age
df['Age']= df[['Age', 'Pclass']].apply(image_age, axis=1)
df.drop('Cabin', axis=1, inplace=True)
df.dropna(inplace=True)
# sns.heatmap(df.isnull(),yticklabels=False, cbar=False, cmap='viridis')
# print(df)
sex= pd.get_dummies(df['Sex'], drop_first=True)
embark= pd.get_dummies(df['Embarked'], drop_first=True)


df= pd.concat([df, sex, embark], axis=1)

# num= df.head()
# print(num)

df.drop(['Sex', 'Embarked', 'Name', 'Ticket','PassengerId'], axis=1, inplace=True)
# num2= df.head()
# print(num2)



"""part 3 train text"""





# Features and Target
X = df.drop('Survived', axis=1)
y = df['Survived']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Model
logmodel = LogisticRegression()
# logmodel.fit(X_train,y_train)
logmodel.fit(X_train, y_train)

# Prediction
y_pred = logmodel.predict(X_test)

# Accuracy Score
print("✅ Accuracy:", accuracy_score(y_test, y_pred))

# Full Classification Report
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

# convent class REpot 
repot = pd.DataFrame(classification_report(y_test, y_pred, output_dict=True))


plt.figure(figsize=(6, 4))
# sns.heatmap(confusion_matrix(y_test, y_pred), cbar=False, yticklabels=False,cmap='coolwarm')

sns.heatmap(repot, yticklabels=False, cmap='BuGn')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

