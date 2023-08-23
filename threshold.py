import numpy as np

def hysteresis_thresholding(matrix, low_threshold, high_threshold):
    # Initialize matrices for strong and weak edges
    strong_edges = matrix > high_threshold
    weak_edges = (matrix >= low_threshold) & (matrix <= high_threshold)

    M, N = matrix.shape
    output_matrix = np.zeros((M, N), dtype=np.uint8)

    for i in range(M):
        for j in range(N):
            if weak_edges[i, j]:
                # Extract 3x3 neighborhood
                neighborhood = matrix[max(i-1, 0):min(i+2, M), max(j-1, 0):min(j+2, N)]
                if np.any(neighborhood > high_threshold):
                    output_matrix[i, j] = 1
            elif strong_edges[i, j]:
                output_matrix[i, j] = 1

    return output_matrix

# Grayscale image matrix
image_matrix = np.array([[0.4, 0.4, 0.6, 0.8, 0.2],
                         [0.9, 0.3, 0.5, 0.1, 0.6],
                         [0.8, 0.0, 0.7, 0.5, 0.0],
                         [0.6, 0.3, 0.5, 0.6, 0.6]])

# Low and high threshold values
low_threshold_value = 0.55
high_threshold_value = 0.75

# Perform hysteresis thresholding
thresholded_image = hysteresis_thresholding(image_matrix, low_threshold_value, high_threshold_value)

# Print the thresholded image
print(thresholded_image)
