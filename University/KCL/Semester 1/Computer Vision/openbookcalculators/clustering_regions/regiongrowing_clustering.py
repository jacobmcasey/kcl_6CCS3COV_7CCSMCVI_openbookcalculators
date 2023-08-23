import numpy as np

# Define the image
image = np.array([[(20, 10, 5), (10, 20, 15)],
                  [(15, 5, 5), (5, 5, 20)],
                  [(15, 15, 15), (20, 15, 10)]])

# Define the threshold for the SAD
threshold = 12

# Choose the neighbors type: "all" or "cross"
neighbors_type = "all" # change this line to "cross" for 4-neighbors

# Get the shape of the image
rows, cols = image.shape[:2]

# Create an empty region matrix
regions = np.zeros((rows, cols))

# Define the region id counter
region_id = 1

# Function to calculate SAD
def calculate_sad(pixel1, pixel2):
    return sum(abs(p1 - p2) for p1, p2 in zip(pixel1, pixel2))

# Check all eight or four neighbours depending on the neighbors_type
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
                    # If the neighbour has no region, assign it to the current region
                    if regions[x, y] == 0:
                        regions[x, y] = region_id
                    # If the neighbour has a region, assign the current pixel to that region
                    else:
                        regions[i, j] = regions[x, y]
                        
        # If the current pixel has no region, assign a new region
        if regions[i, j] == 0:
            regions[i, j] = region_id
            region_id += 1

# Print the regions
print(regions)
