import numpy as np

# Define template and image
T = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

I = np.array([
    [0.1, 0.5, 0.9, 1.0],
    [0.6, 0.6, 0, 0.7],
    [0.9, 0, 0, 0.6],
    [0.7, 0.8, 0.6, 0.7]
])

def cross_correlation(template, image):
    return np.sum(template * image)

def normalized_cross_correlation(template, image):
    numerator = np.sum(template * image)
    denominator = np.sqrt(np.sum(template**2) * np.sum(image**2))
    return numerator / denominator

def euclidean_distance(template, image):
    return np.sqrt(np.sum((template - image) ** 2))

def sliding_window(image, window_shape):
    for i in range(image.shape[0] - window_shape[0] + 1):
        for j in range(image.shape[1] - window_shape[1] + 1):
            yield image[i:i+window_shape[0], j:j+window_shape[1]], (j + window_shape[1]//2, i + window_shape[0]//2)

regions = list(sliding_window(I, T.shape))

# Calculate the best match using each method
methods = [cross_correlation, normalized_cross_correlation, euclidean_distance]
names = ['Cross-correlation', 'Normalized Cross-correlation', 'Euclidean Distance']

for i, method in enumerate(methods):
    scores = []
    for region, (y, x) in regions:
        score = method(T, region)
        scores.append(score)
        print(f"{names[i]} for central pixel at ({x+1}, {y+1}): {score}")
    
    best_match_index = np.argmax(scores) if i != 2 else np.argmin(scores)
    best_region_coordinates = regions[best_match_index][1]
    print(f"{names[i]}: Best match central pixel at ({best_region_coordinates[0]+1}, {best_region_coordinates[1]+1}) with score {scores[best_match_index]}\n")
