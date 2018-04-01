import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('UCI_Space_Data.csv', sep=',',header=None)


#Histogram Plot
data.plot(kind='bar')
plt.ylabel('Frequency')
plt.xlabel('1)Number experiencing thermal distress  2)Launch temperature (degrees F) 3) Leak-check pressure (psi) ')
plt.title('UCI_Space_Data')
plt.show()

