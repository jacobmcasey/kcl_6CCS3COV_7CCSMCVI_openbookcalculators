import numpy as np

# Similarity methods
def cross_correlation(template, image):
    return np.sum(template * image)

def normalized_cross_correlation(template, image):
    numerator = np.sum(template * image)
    denominator = np.sqrt(np.sum(template**2) * np.sum(image**2))
    return numerator / denominator

def sum_of_absolute_differences(template, image):
    return np.sum(np.abs(template - image))

# Templates and Image patch
templates = {
    'T1': np.array([
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
    ]),
    'T2': np.array([
            [1, 1, 1],
            [1, 1, 0],
            [1, 1, 1]
    ]),
    'T3': np.array([
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1]
    ])
}

I = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
])

methods = [cross_correlation, normalized_cross_correlation, sum_of_absolute_differences]
names = ['Cross-correlation', 'Normalized Cross-correlation', 'Sum of Absolute Differences']

# Calculate similarities for each template with the image patch
for template_name, template in templates.items():
    print(f"Comparing template {template_name} with image patch I:")
    for k, method in enumerate(methods):
        score = method(template, I)
        print(f"{names[k]}: {score}")
    print("\n")
