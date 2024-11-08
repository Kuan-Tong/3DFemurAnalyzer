import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np



X = np.real(np.load())
plt.scatter(X[:, 0], X[:, 1],c='white', marker='o',edgecolor='black', s=50)
plt.show()

model = KMeans(n_clusters=3, init='k-means++',n_init=10, max_iter=300, tol=1e-04, random_state=None)

y_pred = model.fit_predict(X)
clusterCenter = model.cluster_centers_

plt.scatter(
    X[y_pred == 0, 0], X[y_pred == 0, 1],
    s=50,
    marker='o', edgecolor='black',
    label='cluster 1'
)
plt.scatter(
    X[y_pred == 1, 0], X[y_pred == 1, 1],
    s=50,
    marker='o', edgecolor='black',
    label='cluster 2'
)
plt.scatter(
    X[y_pred == 2, 0], X[y_pred == 2, 1],
    s=50,
    marker='o', edgecolor='black',
    label='cluster 3'
)
plt.scatter(
    X[y_pred == 3, 0], X[y_pred == 3, 1],
    s=50,
    marker='o', edgecolor='black',
    label='cluster 4'
)

plt.scatter(
    model.cluster_centers_[:, 0], model.cluster_centers_[:, 1],
    s=250, marker='*',
    c='red', edgecolor='black',
    label='centroids'
)
plt.legend(scatterpoints=1)
plt.grid()
plt.show()


