import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import pandas as pd

data1=pd.read_csv('Iris.csv', sep=',',header=None)
data1.columns=["x1","x2","x3","x4","Name"]
plt.figure()
parallel_coordinates(data1,'Name')
plt.show()