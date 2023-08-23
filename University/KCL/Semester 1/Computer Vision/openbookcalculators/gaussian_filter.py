##Jacob Casey KCL MSc Artificial Intelligence

import numpy as np

def generate_gaussian_filter(size, sigma):
    # Input validation
    if size < 3 or size % 2 == 0:
        raise ValueError("Size must be an odd number and greater than or equal to 3.")
    if sigma <= 0:
        raise ValueError("Sigma must be greater than zero.")
    
    # Create a grid of x and y coordinates with the origin at the center
    range_values = np.arange(-size // 2 + 1., size // 2 + 1.)
    x_values, y_values = np.meshgrid(range_values, range_values)
    print(f"x values:\n{x_values}")
    print(f"y values:\n{y_values}")
    
    # Calculate the Gaussian function for each point in the grid
    exponent = -(x_values**2 + y_values**2) / (2. * sigma**2)
    gaussian_values = 1 / (2 * np.pi * sigma**2) * np.exp(exponent)

    # Round the Gaussian values to five decimal places
    rounded_gaussian_values = np.round(gaussian_values, 5)

    return rounded_gaussian_values

# Generate a 3x3 Gaussian filter with a standard deviation of 0.6

gaussian_filter = generate_gaussian_filter(3, 0.45)

# Display the Gaussian filter values
print(f"\nGaussian filter values:\n{gaussian_filter}")