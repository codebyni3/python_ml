# # Normal distribution
# import matplotlib.pyplot as plt
# from numpy import random
# import seaborn as sns
# # x = random.normal(size=(2,3))

# # x = random.normal(loc=1, scale=2, size=(2,3))

# sns.displot(random.normal(size=(100)),  kind="kde")
# # print(x)

# plt.show()


# Binomial Distribution

"""prameter 3 :- n, p, size 
  n :- number of drials
  p:- probability of occurance of each trial.
  size:- the size of the returncat array
"""

# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt
# # arr= random.binomial(n=2, p=0.6, size=(3,4))
# sns.displot(random.binomial(n=2, p=0.5, size=100) )
# # print(arr)
# plt.show()

"""
 Difference Between Normal and Binomial Distribution

"""

from numpy import random, where
import seaborn as sns
import matplotlib.pyplot as plt

data={
    "normal":  random.normal(loc=50, scale= 2, size=100),
    "binomial": random.binomial(n=11, p=0.3, size=100),
    "poisson": random.poisson(lam=20, size=100),
    "uniform": random.uniform(low=5, high=58, size=100),
    "logistic": random.logistic(loc=39,scale=3, size=100),
    # "multinomial":random.multinomial(n=12, pvals=[1/6], size=100),
    "Exponential": random.exponential(scale=4, size=100),
    "Chi Square": random.chisquare(df=2, size=100),
    "Rayleigh": random.rayleigh(scale=3, size=100),
    "Pareto ": random.pareto(a=2, size=100),
    "zipf":random.zipf(a=3, size=100)
}

sns.displot(data, kind="kde")
plt.show()