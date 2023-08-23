import numpy as np

def neighbors(arr, x, y, n=3):
    ''' Given a 2D-array, returns an nxn array whose "center" element is arr[x,y]'''
    arr = np.roll(np.roll(arr, shift=-x+1, axis=0), shift=-y+1, axis=1)
    return arr[:n, :n]

def calculate_sad(left_image, right_image, row, col, window_size=3):
    # Extract the 3x3 window centered around the target pixel in the left image
    left_window = neighbors(left_image, row, col, window_size)
    print(f"*CHECK THIS* left_window:\n {left_window}\n")
    right_image_padded = np.pad(right_image, (window_size // 2, window_size // 2), mode='constant')
    sad_matrix = np.zeros_like(right_image)

    # Iterate through the right image, shifting the target window from the left image
    for r in range(right_image.shape[0]):
        for c in range(right_image.shape[1]):
            # Extract the corresponding window from the right image
            right_window = neighbors(right_image_padded, r + window_size // 2, c + window_size // 2, window_size)
            
            # Calculate the SAD between the target window from the left image and the current window from the right image
            sad = np.sum(np.abs(left_window - right_window))
            
            # Store the SAD value in the corresponding position in the SAD matrix
            sad_matrix[r, c] = sad

    return sad_matrix

def find_best_match(sad_matrix):
    best_match_row, best_match_col = np.unravel_index(sad_matrix.argmin(), sad_matrix.shape)
    return best_match_row, best_match_col

left_image = np.array([
    [40, 60, 40, 20, 50],
    [10, 50, 80, 80, 30],
    [70, 10, 70, 60, 90],
])

right_image = np.array([
    [20, 70, 70, 20, 50],
    [30, 20, 50, 10, 50],
    [50, 70, 40, 80, 70],
])

# Target pixel's coordinates are given in the form (column, row)
target_col, target_row = 2, 2

# Adjust the coordinates to match the Python zero-indexing
col = target_col - 1
row = target_row - 1

sad_matrix = calculate_sad(left_image, right_image, row, col)
best_match_row, best_match_col = find_best_match(sad_matrix)

# Calculate the disparity in (column, row) form
disparity = (col - best_match_col, row - best_match_row)

print(f"Final SAD Matrix:\n {sad_matrix}")
print("For point({}, {}), SAD line scan is = {}".format(target_col, target_row, sad_matrix[row].flatten()))
print("Hence, best match is at location({}, {}) in the right image. Disparity is RIGHT to LEFT (which is calculated by left-right) = ({}, {}) - ({}, {}) = {}.".format(best_match_col + 1, best_match_row + 1, target_col, target_row, best_match_col + 1, best_match_row + 1, disparity))
