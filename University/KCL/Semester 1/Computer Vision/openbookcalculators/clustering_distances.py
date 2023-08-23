from scipy.spatial.distance import pdist, cdist
import numpy as np
from decimal import Decimal

# Assign the feature vectors to two clusters
cluster1 = np.array([[2, 4, 5], [1,4,4], [2,3,6]])
cluster2 = np.array([[5,6,2], [7,4,3]])

# Single-link clustering (Minimum distance)
def single_link(cluster1, cluster2):
    dist_matrix = cdist(cluster1, cluster2, 'cityblock')
    return np.min(dist_matrix)

# Complete-link clustering (Maximum distance)
def complete_link(cluster1, cluster2):
    dist_matrix = cdist(cluster1, cluster2, 'cityblock')
    return np.max(dist_matrix)

# Group-average clustering (Average distance)
def group_average(cluster1, cluster2):
    dist_matrix = cdist(cluster1, cluster2, 'cityblock')
    return np.mean(dist_matrix)

# Centroid clustering (Distance between the centroids of two clusters)
def centroid_link(cluster1, cluster2):
    centroid1 = np.mean(cluster1, axis=0)
    centroid2 = np.mean(cluster2, axis=0)
    return np.sum(np.abs(centroid1 - centroid2))

print("Single-link clustering: ", Decimal(single_link(cluster1, cluster2)))
print("Complete-link clustering: ", Decimal(complete_link(cluster1, cluster2)))
print("Group-average clustering: ", Decimal(group_average(cluster1, cluster2)))
print("Centroid clustering: ", Decimal(centroid_link(cluster1, cluster2)))
