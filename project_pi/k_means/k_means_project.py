import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df= pd.read_csv('k_means/College_Data', index_col=0)
# df1=df.head()

# df1=df.info()
# print(df1)


# EDA  data visualizations!

# 1. sns.scatterplot(x='Room.Board', y='Grad.Rate', data=df, hue='Private')

# 2.  sns.scatterplot(y='F.Undergrad', x='Outstate', data=df, hue='Private')



# 3 topic

# g=sns.FacetGrid(data=df, hue='Private', palette='coolwarm')
# h=g.map(plt.hist,'Outstate', bins=20, alpha=0.7)


# 4
# g=sns.FacetGrid(data=df, hue='Private', palette='coolwarm')
# h=g.map(plt.hist,'Grad.Rate', bins=20, alpha=0.7)


# 5 how there seems to be a private schools with a graduations rate of higher than 100% .what is the name of that schools 

# a=df[df['Grad.Rate']>100]

# 6

# df['Grad.Rate']['Cazenvia College']= 100
# a=df[df['Grad.Rate']>100]
# print(a)

# g=sns.FacetGrid(data=df, hue='Private', palette='coolwarm')
# h=g.map(plt.hist,'Grad.Rate', bins=20, alpha=0.7)



from sklearn.cluster import KMeans
kmeans= KMeans(n_clusters=2)

kmeans.fit(df.drop('Private', axis=1))

kmeans.cluster_centers_
kmeans.labels_


#  create a new col for df called 'Cluster', Which is a 1 for a private school and a 0 for a public school .

def convert(Private):
    if Private=='Yes':
        return 1
    else:
        return 0
    
df['Cluster']= df['Private'].apply(convert)
a=df.head(2)


from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(df['Cluster'], kmeans.labels_))
print('/n')
print(confusion_matrix(df['Cluster'],kmeans.labels_))

print(a)
plt.show()


