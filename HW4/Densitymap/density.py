import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


data = pd.read_csv('UCI_Space_Data.csv', sep=',',header=None)
da=sns.load_dataset('iris')
plt.title('Density Map')
sns.kdeplot(da['sepal_width'])
plt.show()
