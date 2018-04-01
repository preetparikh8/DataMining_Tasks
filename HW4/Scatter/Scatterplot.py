import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('UCI_Space_Data.csv', sep=',',header=None)

#ScatterPlot
data.plot(kind='scatter', x=2, y=3)
plt.ylabel('Leak-Pressure')
plt.xlabel(' Launch Tempreature ')
plt.show()