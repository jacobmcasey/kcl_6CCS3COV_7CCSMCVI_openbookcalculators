import numpy as np

# Function to calculate SAD
def calculate_sad(pixel1, pixel2):
    return sum(abs(p1 - p2) for p1, p2 in zip(pixel1, pixel2))

# *HERE: Define the image
image = np.array([[(5, 10, 15), (10, 15, 30), (10, 10, 25)],
                  [(10, 10, 15), (20, 20, 15), (10, 5, 10)],
                  [(5, 5, 15), (30, 10, 5), (30, 10, 10)]])

# *HERE: Initialize cluster centers
clusters = [(10, 10, 10), (30, 20, 10)]

# Get the shape of the image
rows, cols = image.shape[:2]

# Number of clusters
k = len(clusters)

# Initialize the regions matrix
regions = np.zeros((rows, cols))

# Start the K-means algorithm
while True:
    # Step 1: Assign each pixel to the closest cluster center
    new_regions = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            distances = [calculate_sad(image[i, j], cluster) for cluster in clusters]
            new_regions[i, j] = np.argmin(distances)
    
    # If the regions are the same as the last iteration, the algorithm has converged
    if np.array_equal(regions, new_regions):
        break
    regions = new_regions

    # Step 2: Update the cluster centers to be the mean of the pixels in each cluster
    for c in range(k):
        members = image[regions == c]
        if len(members) > 0:
            clusters[c] = tuple(np.mean(members, axis=0))

print("Final Regions:")
print(regions + 1)  # adding 1 so that regions are 1-indexed