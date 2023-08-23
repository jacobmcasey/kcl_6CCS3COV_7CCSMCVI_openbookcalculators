import numpy as np
from collections import Counter

# Given feature vectors and their classes
objects = {
    (0.5,-0.4,0.5): '1',
    (-0.6,-0.2,0.1): '1',
    
    (0.3,0.3,0.4): '2',
    
    (-0.6,-0.1,-0.5): '3',
    
    (-0.8,0.4,0.5): '2'
}

# Input here too
new_object = (-0.4,-0.9,0.3)
k_ = 3

# Compute the Euclidean distance
def euclidean_distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

# 1. Nearest mean classifier
def nearest_mean(objects, point):
    # Compute the mean feature vector for each class
    means = {}
    for obj, cls in objects.items():
        if cls not in means:
            means[cls] = []
        means[cls].append(obj)

    means = {cls: np.mean(points, axis=0) for cls, points in means.items()}
    
    # Print prototype of each class
    for cls, mean in means.items():
        print(f"Prototype of class {cls} = {mean}")

    # Print distance of new object from prototypes
    distances = {}
    for cls, mean in means.items():
        distance = euclidean_distance(point, mean)
        distances[cls] = distance
        print(f"Distance of new object from prototype of class {cls}:", distance)

    # Classify based on the closest mean
    classification = min(distances, key=distances.get)
    print(f"Hence, new object is class {classification}.")
    return classification

# 2. Nearest neighbour classifier
def nearest_neighbour(objects, point):
    distances = {}
    for obj, cls in objects.items():
        distance = euclidean_distance(point, obj)
        distances[obj] = distance
        print(f"Distance of new object from exemplar {obj} of class {cls}:", distance)
    
    closest_obj = min(distances, key=distances.get)
    classification = objects[closest_obj]
    print(f"The closest exemplar is object {closest_obj}. Since object {closest_obj} is of class {classification}, the new object is also class {classification}.")
    return classification

# 3. k-nearest neighbour classifier
def k_nearest_neighbour(objects, point, k=3):
    distances = sorted([(obj, euclidean_distance(point, obj)) for obj in objects], key=lambda x: x[1])
    top_k = [objects[obj[0]] for obj in distances[:k]]
    
    # Print the k closest exemplars and their classes
    for obj, distance in distances[:k]:
        print(f"The {k}-closest exemplar is {obj} of class {objects[obj]}.")
    
    most_common = Counter(top_k).most_common(1)[0][0]
    count = Counter(top_k).most_common(1)[0][1]
    print(f"The majority of {k} closest exemplars are class {most_common} ({count} out of {k}), so the new object is classified as {most_common}.")
    return most_common

print("1. Classification using Nearest Mean:")
print(nearest_mean(objects, new_object))
print("\n2. Classification using Nearest Neighbour:")
print(nearest_neighbour(objects, new_object))
print("\n3. Classification using 3-Nearest Neighbour:")
print(k_nearest_neighbour(objects, new_object, k=k_))
