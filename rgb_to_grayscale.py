import numpy as np

def rgb_to_grayscale(R, G, B):
    # Input validation
    if R.shape != G.shape or G.shape != B.shape:
        raise ValueError("All three matrices must have the same shape.")

    # Check if any of the values are out of the 8-bit range
    if (R < 0).any() or (R > 255).any() or (G < 0).any() or (G > 255).any() or (B < 0).any() or (B > 255).any():
        raise ValueError("All values must be in the 8-bit range (0 to 255).")

    # Calculate the grayscale values using the 3:2:1 ratio
    grayscale = (3 * R + 2 * G + B) / 6
    
    # Round the grayscale values to the nearest integer
    grayscale_rounded = np.round(grayscale).astype(int)

    return grayscale_rounded

# Define the R, G, and B channels
R = np.array([
    [255, 233, 71],
    [231, 161, 140],
    [32, 24, 245]
])

G = np.array([
    [250, 245, 36],
    [40, 124, 107],
    [248, 204, 234]
])

B = np.array([
    [255, 9, 173],
    [245, 217, 193],
    [167, 239, 190]
])

# Convert the RGB image to grayscale
grayscale = rgb_to_grayscale(R, G, B)

print(grayscale)
