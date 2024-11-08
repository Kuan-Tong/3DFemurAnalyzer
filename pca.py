from sklearn.decomposition import PCA
import numpy as np
import scipy.io as scio
import matplotlib.pyplot as plt

data = scio.loadmat()

pca = PCA(0.9)

pca.fit(data)
transformed_point = pca.transform(data)

mean_values = pca.mean_
transformed_features = pca.transform(data)
sorted_eigenvalues = np.sort(pca.explained_variance_)[::-1]
sorted_indices = np.argsort(pca.explained_variance_)[::-1]
sorted_eigenvectors = pca.components_[sorted_indices]

explained_variance_ratio = pca.explained_variance_ratio_

