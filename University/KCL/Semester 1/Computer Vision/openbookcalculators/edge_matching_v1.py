import numpy as np
import math

# Define the template and the image
T = np.array([[1, 1, 1], 
              [1, 0, 1], 
              [1, 1, 1]])


I = np.array([[0, 0, 1, 0], 
              [0, 1, 1, 1], 
              [0, 0, 0, 1], 
              [0, 1, 1, 1]])

# Function to calculate the minimum distance
def min_distance(T, I):
    total_distance = 0
    for i in range(T.shape[0]):
        for j in range(T.shape[1]):
            if T[i, j] == 1:
                # center element
                if i == 1 and j == 1:
                    total_distance += 2 if I[i, j] == 0 else 0
                else: 
                    total_distance += 1 if I[i, j] == 0 else 0
    print(total_distance)
    average_distance = total_distance / (T.size - 1)
    return average_distance

# Specify the locations in the image where the template fits
locations = [(2, 2), (3, 2), (2, 3), (3, 3)]

# Iterate over the specified locations in the image to find the best match for the template
min_dist = np.inf
best_location = None
for location in locations:
    i, j = location
    dist = min_distance(T, I[i-2:i+1, j-2:j+1])
    print(f"Pixel ({i},{j}) Distance = {dist}")
    if dist < min_dist:
        min_dist = dist
        best_location = location

print(f"\nHence, object at location {best_location}")
