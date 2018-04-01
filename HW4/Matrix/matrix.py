import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


data = pd.read_csv('UCI_Space_Data.csv', sep=',',header=None)
#MatrixCoRelation
corr = data.corr()
sns.heatmap(corr,
        xticklabels=corr.columns.values,
        yticklabels=corr.columns.values)
plt.show()


