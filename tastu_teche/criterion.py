import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# https://pythonprogramminglanguage.com/kmeans-elbow-method/


def elbow_global(X, kmeanModel):
    # / X.shape[0]
    return sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1))


def elbow_local(X, kmeanModel):
    return sum([np.sum(cdist(
        X[np.where(kmeanModel.labels_ == i)], [kmeanModel.cluster_centers_[i]], 'euclidean')) for i in range(kmeanModel.n_clusters)])


def elbow_inertia(X, kmeanModel):
    return kmeanModel.inertia_


def compute_bic(X, kmeans):
    """
    Computes the BIC metric for a given clusters

    Parameters:
    -----------------------------------------
    kmeans:  List of clustering object from scikit learn

    X     :  multidimension np array of data points

    Returns:
    -----------------------------------------
    BIC value
    """
    # assign centers and labels
    centers = [kmeans.cluster_centers_]
    labels = kmeans.labels_
    # number of clusters
    m = kmeans.n_clusters
    # size of the clusters
    n = np.bincount(labels)
    # size of data set
    N, d = X.shape
    #XX = X.toarray()
    # compute variance for all clusters beforehand
    cl_var = (1.0 / (N - m) / d) * sum([sum(cdist(
        X[np.where(labels == i)], [centers[0][i]], 'euclidean')**2) for i in range(m)])
    const_term = 0.5 * m * np.log(N) * (d + 1)
    BIC = np.sum([n[i] * np.log(n[i]) -
                  n[i] * np.log(N) -
                  ((n[i] * d) / 2) * np.log(2 * np.pi * cl_var) -
                  ((n[i] - 1) * d / 2) for i in range(m)]) - const_term
    return(BIC)


from sklearn.metrics import silhouette_score


def sil_coeff(X, kmeanModel):
    if kmeanModel.n_clusters > 1:
        sil_coeff = silhouette_score(X, kmeanModel.labels_, metric='euclidean')
    else:
        sil_coeff = 0
    return sil_coeff


def elbow_k(X, k):
    kmeanModel = KMeans(n_clusters=k).fit(X)
    kmeanModel.fit(X)
    return (k, elbow_inertia(X, kmeanModel), elbow_local(
            X, kmeanModel), elbow_global(X, kmeanModel), compute_bic(X, kmeanModel), sil_coeff(X, kmeanModel))


def elbow_all(X):
    # k means determine k
    distortions = []
    K = range(1, 30)
    for k in K:
        print('----KMeans --%s' % str(k))
        distortions.append(elbow_k(X, k))
    return distortions


def elbow_plot(distortions, ic_n=1):
    ic_name = ['elbow_inertia', 'elbow_local',
               'elbow_global', 'BIC', 'silhouette_score']
    # Plot the elbow
    K = [d[0] for d in distortions]
    plt.plot(K, [d[ic_n] for d in distortions], 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.title('The %s Method showing the optimal k' % ic_name[ic_n - 1])
    # plt.show()


#distortions = elbow_plot(np.array(matrix[x_cols]))
