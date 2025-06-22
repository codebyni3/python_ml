
from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

# arr1 = np.array(["python", "java","mysql","javascript","Ruby"])
# arr2= np.array([45,64,73,12,53])

# plt.pie(arr2, labels=arr1, autopct="%5.1f%%") 
# plt.bar(arr1,arr2)
# plt.scatter(arr1, arr2)



# arr = np.random.randn(200)
# plt.hist(arr, bins=100)

# tym = [1,2,3,4,5]
# temp=[13,20,33,40,20]
# fig,ax = plt.subplots()

# ax.plot(tym,temp, linestyle='-',marker='*' ,color='g',label='temp')

# ax.set_xlabel("tym(hours)")
# ax.set_ylabel("temp")
# ax.set_title("chart of temp")

# ax.legend()




# 2*2
fig, axs = plt.subplots(2,2)
axs[0,0].plot([1,2,3],[2,5,1])
axs[1,0].scatter([3,1,2],[8,1,3])
axs[1,1].bar([1,2,4],[5,2,6])
axs[0,1].hist([3,2,1,4,6,9,11,35])
plt.show()


