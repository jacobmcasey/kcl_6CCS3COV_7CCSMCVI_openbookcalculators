import numpy as np

# Similarity methods
def cross_correlation(template, image):
    return np.sum(template * image)

def normalized_cross_correlation(template, image):
    numerator = np.sum(template * image)
    denominator = np.sqrt(np.sum(template**2) * np.sum(image**2))
    return numerator / denominator

def euclidean_distance(template, image):
    return np.sqrt(np.sum((template - image) ** 2))

def correlation_coefficient(patch1, patch2):
    # Calculate mean of the patches
    mean_patch1 = np.mean(patch1)
    mean_patch2 = np.mean(patch2)

    # Calculate the numerator and denominators for the correlation coefficient
    numerator = np.sum((patch1 - mean_patch1) * (patch2 - mean_patch2))
    denominator_patch1 = np.sqrt(np.sum((patch1 - mean_patch1) ** 2))
    denominator_patch2 = np.sqrt(np.sum((patch2 - mean_patch2) ** 2))
    
    return numerator / (denominator_patch1 * denominator_patch2)

# Add this function
def sum_of_absolute_differences(template, image):
    return np.sum(np.abs(template - image))

# Given image patches
patches = {
    'A': np.array([
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
    ]),
    'B': np.array([
            [0, 0, 0, 0],
            [1, 0, 1, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0]
    ]),
    'C': np.array([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 1, 1, 1]
    ])
}

# Add the function to the methods list
methods = [cross_correlation, normalized_cross_correlation, euclidean_distance, correlation_coefficient, sum_of_absolute_differences]
names = ['Cross-correlation', 'Normalized Cross-correlation', 'Euclidean Distance', 'Correlation Coefficient', 'Sum of Absolute Differences']

# Calculate similarities for each pair of image patches
patch_names = list(patches.keys())
for i in range(len(patch_names)):
    for j in range(i+1, len(patch_names)):
        patch1_name, patch1 = patch_names[i], patches[patch_names[i]]
        patch2_name, patch2 = patch_names[j], patches[patch_names[j]]
        
        print(f"Comparing patches {patch1_name} & {patch2_name}:")
        for k, method in enumerate(methods):
            score = method(patch1, patch2)
            print(f"{names[k]}: {score}")
        print("\n")
