import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics

# Load data
df = pd.read_csv("USA_Housing.csv")

# df.columns
# Select features (exclude 'Price' and 'Address')
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]

# Target variable
y = df['Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

# Fit Linear Regression model
lm = LinearRegression()
lm.fit(X_train, y_train)

# Print intercept
print("Intercept:", lm.intercept_)

# Create DataFrame for coefficients
cmf = pd.DataFrame(lm.coef_.reshape(-1, 1), index=X_train.columns, columns=['Coeff'])
print(cmf)

#  prediction 
predictions = lm.predict(X_test)
plt.scatter(y_test, predictions)
sns.displot(y_test - predictions)

print("MAE:", metrics.mean_absolute_error(y_test, predictions) )
plt.show()