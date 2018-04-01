import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('UCI_Space_Data.csv', sep=',',header=None)

#BoxPlot
slice = data.iloc[:,[2,3]]
bp = slice.boxplot()
axes = plt.gca()
axes.set_ylim([0,250])
plt.show()