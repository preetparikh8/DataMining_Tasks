import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import kde
import matplotlib.cm as cm
import seaborn as sns
from wordcloud import WordCloud

data = pd.read_csv('UCI_Space_Data.csv', sep=',',header=None)

#StatsSummary
a = data.iloc[:,[2]]
print "The mean for column", np.mean(a)
print "The STD for column", np.std(a)
print "The median for column 2", np.median(a)
arr = np.ma.array(a).compressed()
med = np.median(arr)
print "The MAD for column 2", np.median(np.abs(arr - med))
print "The Maximum for column ", np.amax(a)
print "The Minimum for column ", np.amin(a)

#Histogram Plot
data.plot(kind='bar')
plt.ylabel('Frequency')
plt.xlabel('1)Number experiencing thermal distress  2)Launch temperature (degrees F) 3) Leak-check pressure (psi) ')
plt.title('UCI_Space_Data')
plt.show()

#BoxPlot
slice = data.iloc[:,[2,3]]
bp = slice.boxplot()
axes = plt.gca()
axes.set_ylim([0,250])
plt.show()


#ScatterPlot
data.plot(kind='scatter', x=2, y=3)
plt.ylabel('Leak-Pressure')
plt.xlabel(' Launch Tempreature ')
plt.show()

#DensityMap
da=sns.load_dataset('iris')
plt.title('Density Map')
sns.kdeplot(da['sepal_width'])
plt.show()

#ParallelCoOrdinates
data1=pd.read_csv('Iris.csv', sep=',',header=None)
data1.columns=["x1","x2","x3","x4","Name"]
plt.figure()
pd.tools.plotting.parallel_coordinates(data1,'Name')
plt.show()

#MatrixCoRelation
corr = data.corr()
sns.heatmap(corr,
        xticklabels=corr.columns.values,
        yticklabels=corr.columns.values)
plt.show()

#WordCloud
text = open('crimenyctweets.txt').read()
wordcloud = WordCloud(stopwords='grand').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()