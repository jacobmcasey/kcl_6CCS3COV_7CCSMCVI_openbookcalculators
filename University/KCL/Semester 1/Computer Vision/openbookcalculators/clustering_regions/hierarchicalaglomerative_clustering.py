# Remarks:
# Uses SAD
# Merges based on minimum distance in proximity matrix
import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist
from itertools import combinations

pd.set_option('display.max_rows', 10)

# Function to calculate SAD
def calculate_sad(pixel1, pixel2):
    return sum(abs(p1 - p2) for p1, p2 in zip(pixel1, pixel2))

# Function to calculate distance between clusters
def calculate_cluster_distance(cluster1, cluster2):
    return np.mean([calculate_sad(pixel1, pixel2) for pixel1 in cluster1 for pixel2 in cluster2])

# Define the image
image = np.array([[(1, -0.8), (0.8, 0.8), (0.1, 0.7)],
                  [(0.8, 0.3), (0.6, -0.5), (-0.2, -0.9)]])

# Define the desired number of clusters/regions
n_clusters = 4

# Flatten the image
flat_image = np.reshape(image, (-1, image.shape[-1]))

# Initialize clusters
clusters = {f'c{i+1}': [list(pixel)] for i, pixel in enumerate(flat_image)}


# Create initial proximity matrix
proximity_matrix = pd.DataFrame(index=clusters.keys(), columns=clusters.keys())
for comb in combinations(clusters.keys(), 2):
    proximity_matrix.loc[comb[0], comb[1]] = calculate_cluster_distance(clusters[comb[0]], clusters[comb[1]])
    proximity_matrix.loc[comb[1], comb[0]] = calculate_cluster_distance(clusters[comb[1]], clusters[comb[0]])

print(proximity_matrix.fillna('-'))
print("\n")

while len(clusters) > n_clusters:
    # Calculate all pairwise distances
    distances = [(c1, c2, calculate_cluster_distance(clusters[c1], clusters[c2]))
                 for c1, c2 in combinations(clusters.keys(), 2)]

    # Find the pair of clusters with the smallest distance
    c1, c2, _ = min(distances, key=lambda x: x[2])

    # Merge the closest clusters
    clusters[f'{c1}+{c2}'] = clusters[c1] + clusters[c2]

    # Delete the merged clusters
    del clusters[c1]
    del clusters[c2]

    # Create proximity matrix
    proximity_matrix = pd.DataFrame(index=clusters.keys(), columns=clusters.keys())
    for comb in combinations(clusters.keys(), 2):
        proximity_matrix.loc[comb[0], comb[1]] = calculate_cluster_distance(clusters[comb[0]], clusters[comb[1]])
        proximity_matrix.loc[comb[1], comb[0]] = calculate_cluster_distance(clusters[comb[1]], clusters[comb[0]])
    
    print(proximity_matrix.fillna('-'))
    print("\n")

# Now, clusters contains n_clusters clusters, each of which is a list of pixels
for i, cluster_id in enumerate(clusters.keys()):
    print(f"Region {i+1}: {cluster_id}")
    for pixel in clusters[cluster_id]:
        print(f"Pixel: {pixel}")
    print("\n")