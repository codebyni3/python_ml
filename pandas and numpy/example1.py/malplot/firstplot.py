import matplotlib.pyplot as plt

import pandas as pd


df = pd.read_csv('data.csv')

# df.plot(kind='scatter', x = 'Maxpulse', y='Pulse')
df.plot(kind='line')
plt.show()