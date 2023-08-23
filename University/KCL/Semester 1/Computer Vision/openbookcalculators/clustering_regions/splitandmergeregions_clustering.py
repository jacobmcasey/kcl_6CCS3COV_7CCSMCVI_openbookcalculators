import numpy as np

# Define the 3x3 image
image = np.array([[(5, 10, 15), (10, 15, 30), (10, 10, 25)],
                  [(10, 10, 15), (5, 20, 15), (10, 5, 30)],
                  [(5, 5, 15), (30, 10, 5), (30, 10, 10)]])

# Get the shape of the image
rows, cols = image.shape[:2]

# Create an initial region matrix, with each pixel as a region
regions = np.array([[i*cols + j + 1 for j in range(cols)] for i in range(rows)])

# Define the threshold for the SAD
threshold = 12

# Choose the neighbors type: "all" or "cross"
neighbors_type = "all" # change this line to "cross" for 4-neighbors

# Function to calculate SAD
def calculate_sad(pixel1, pixel2):
    return sum(abs(p1 - p2) for p1, p2 in zip(pixel1, pixel2))

# Check all eight or four neighbours depending on the neighbors_type for merging
for i in range(rows):
    for j in range(cols):
        # Current pixel
        current_pixel = image[i, j]

        if neighbors_type == "all":
            # Neighbours coordinates for all 8 neighbours
            neighbours = [(i-1, j-1), (i-1, j), (i-1, j+1), 
                          (i, j-1),               (i, j+1), 
                          (i+1, j-1), (i+1, j), (i+1, j+1)]
        elif neighbors_type == "cross":
            # Neighbours coordinates for 4 neighbours (up, down, left, right)
            neighbours = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        # Process each neighbour
        for x, y in neighbours:
            # Check if neighbour coordinate is inside the image
            if 0 <= x < rows and 0 <= y < cols:
                neighbour_pixel = image[x, y]
                
                # Check if SAD is less than threshold
                if calculate_sad(current_pixel, neighbour_pixel) < threshold:
                    # Merge the regions of the current pixel and the neighbour
                    regions[regions == regions[x, y]] = regions[i, j]

# Print the regions
print(regions)
