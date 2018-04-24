import pandas
import pylab as pl
from sklearn.cluster import KMeans

data = pandas.read_csv('Iris.csv')
X = data[['SepalWidth']]
Y = data[['PetalLength']]

R = range(5, 15)
kmeans = [KMeans(n_clusters=k) for k in R]

score = [kmeans[k].fit(Y).score(Y) for k in range(len(kmeans))]

pl.plot(R,score)
pl.xlabel('No of Clusters')
pl.ylabel('Score')
pl.title('K- means Cluster Curve')
pl.show()