# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # sns.displot([1,2,3,5,6,7,8,9], kind='hist')
# # plt.show()

# from operator import le
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# # Load example dataset
# # data = sns.load_dataset("iris")

# # # Create a scatter plot
# # sns.scatterplot(x="sepal_length", y="sepal_width",hue="species", data=data)
# # # sns.scatterplot(x="",y="")
# # # Show plot
# # plt.show()

# arr = np.array([1,99,12,4,5,87,29,32])

# df= pd.DataFrame(
#     {
#         "height": np.arange(len(arr)),
#         "width": arr
#     }
# )

# sns.lineplot(x="height", y="width", data=df)
# plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
import seaborn as sns

arr = np. array([12,32,44,10,30,2])

# df = pd.DataFrame({
#     "bit": np.arange(len(arr)),
#     "kumar": arr
#     })

# sns.barplot(x="bit", y="kumar", data=df)                barplot
# sns.boxplot(x="bit", y="kumar", data=df)
# sns.catplot(x="bit", y="kumar", data=df)

df = pd.DataFrame({
    "name":["nitin","amit","deepak","spriya","komal","kanchin"],
    "gender":["male","male","male","female","female","feamle"]
})


sns.countplot(x="gender", data=df)



plt.show()
