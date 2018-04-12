import pandas
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

data = pandas.read_csv('Iris.csv')
X = data[['SepalWidth']]
Y = data[['PetalLength']]

Nc = range(5, 15)
kmeans = [KMeans(n_clusters=i) for i in Nc]

score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]

pl.plot(Nc,score)
pl.xlabel('No of Clusters')
pl.ylabel('Score')
pl.title('Cluster Curve')
pl.show()