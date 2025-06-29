# data ko clusters (group)

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs

data=make_blobs(n_samples=200, centers=4, n_features=2,random_state=101)

# sns.scatterplot(x=data[0][:,0], y=data[0][:,1],hue=data[1], palette='deep')   # X-AXIS  values(1 col), y-axis  value(2nd col)
"""a=data[1]  #create label
plt.scatter(data[0][:,0], data[0][:,1],c=data[1])
print(a)"""


from sklearn.cluster import KMeans

kmeans= KMeans(n_clusters=4)

kmeans.fit(data[0])     #data[0] = X
kmeans.cluster_centers_    #  each cluster give center
kmeans.labels_             # give cluster label  (200 point  , 200 labels )


fig,(ax1,ax2)= plt.subplots(1,2, sharey=True, figsize=(10,6))
ax1.set_title("K Means")
ax1.scatter(data[0][:,0], data[0][:,1],c=kmeans.labels_ ,cmap='rainbow')

ax2.set_title("Original")
ax2.scatter(data[0][:,0], data[0][:,1],c=data[1] ,cmap='rainbow')
# pred label
plt.show()