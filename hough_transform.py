import numpy as np
import pandas as pd
from tabulate import tabulate
from decimal import Decimal, getcontext

# Set the precision
getcontext().prec = 6

# Define the binary image matrix
image_matrix = np.array([[1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]], dtype=np.uint8)

# Define the theta values and quantized r
theta_values = [0, 45, 90, 135]
quantized_r = int(np.round(np.sqrt(image_matrix.shape[0] ** 2 + image_matrix.shape[1] ** 2)))

# Initialize the accumulator array
accumulator_array = np.zeros((2 * quantized_r + 1, len(theta_values)), dtype=int)

# Perform Hough transform
for row in range(image_matrix.shape[0]):
    for col in range(image_matrix.shape[1]):
        if image_matrix[row, col] == 1:
            print(f"\nFor pixel at ({row}, {col}), the following lines are possible:")
            for theta_index, theta in enumerate(theta_values):
                r_before_round = Decimal(row) * Decimal(np.cos(np.deg2rad(theta))) - Decimal(col) * Decimal(np.sin(np.deg2rad(theta)))
                r = int(round(r_before_round))
                accumulator_array[r + quantized_r, theta_index] += 1
                print(f"θ={theta}, r={row}cos({theta})-{col}sin({theta})={r_before_round} ≈ {r}")

# Flip accumulator array upside down
accumulator_array = np.flipud(accumulator_array)

# Create a dataframe for a nicer display of the accumulator array
df = pd.DataFrame(accumulator_array, columns=theta_values, index=range(quantized_r, -quantized_r - 1, -1))

# Print the final accumulator array
print("Final accumulator array:\n")
print(tabulate(df, headers='keys', tablefmt='psql', showindex="always"))
print()

# Find the maximum value and its indices
max_value = np.max(accumulator_array)
max_indices = np.argwhere(accumulator_array == max_value)
r_peak = quantized_r - max_indices[0, 0]
theta_peak = theta_values[max_indices[0, 1]]

# Print the maximum value and its indices
print("Maximum value in the accumulator array:")
print("Value:", max_value)
print("Indices (θ, r):", theta_peak, r_peak)