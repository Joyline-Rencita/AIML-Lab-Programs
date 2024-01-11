# prog 7 :  KMeans

import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

# load the data
data = pd.read_csv('/content/drive/MyDrive/contents/prog7.csv')
f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1,f2)))
print('x: ',X)
print('The graph for the dataset is:\n')
plt.scatter(f1, f2, c="black")
plt.show()
print("\n")

kmeans = KMeans(2)
labels = kmeans.fit(X).predict(X)
print("Labels are : ",labels)
print("Graph ofr kmeans is :")
plt.scatter(f1, f2, c=labels)
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:,0], centroids[:,1], marker='*', c='red')
plt.show()

gmm = GaussianMixture(2)
labels = gmm.fit(X).predict(X)
print("Labels are : ",labels)
print("Graph for EL Agorithm is :")
plt.scatter(f1, f2, c=labels)
plt.show()


output:

x:  [[1.  1. ]
 [1.5 2. ]
 [3.  4. ]
 [5.  7. ]
 [3.5 5. ]
 [4.5 5. ]
 [3.5 4.5]]
The graph for the dataset is:




Labels are :  [1 1 0 0 0 0 0]
Graph ofr kmeans is :
/usr/local/lib/python3.10/dist-packages/sklearn/cluster/_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
  warnings.warn(

Labels are :  [1 1 0 0 0 0 0]
Graph for EL Agorithm is :
