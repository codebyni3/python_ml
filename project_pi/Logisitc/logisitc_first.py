import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# data read
df= pd.read_csv('Logisitc/titanic_train.csv')
df.head()
df.isnull()

# sns.heatmap(x, yticklabels=False, cbar=False, cmap="YlGnBu")
sns.set_style("whitegrid")
# sns.countplot(x="Survived",data=df, hue='Sex', palette='RdBu_r')
# sns.distplot(df['Age'].dropna(),kde=False,color='darkred',bins=30)
# or
# df['Age'].plot.hist(bin= 30)

df.info()

# sns.countplot(x='SibSp', data=df, palette='pastel')
# df['Fare'].hist(bins=30,figsize=(10,4) )


# df['Fare'].plot.hist(bins=30 )

# import cufflinks as cf
# cf.go_online()

# df.iplot(kind='box', title='Box Plot')

# part 2

plt.figure(figsize=(10, 4))
sns.boxplot(x='Pclass', y='Age', data=df, palette='pastel')
plt.show()
