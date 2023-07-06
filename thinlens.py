##Jacob Casey KCL MSc Artificial Intelligence

def calculate_image_distance(f, do):
    di = 1 / (1/f - 1/do)
    return di

def calculate_focal_length(do, di):
    f = 1 / (1/do + 1/di)
    return f

# Define the focal length and object distances
f = 35  # Focal length in mm
distances = [3000, 500]  # Object distances in mm

# Create a list to store the image distances
image_distances = []

# Loop over the object distances and calculate the image distances
for do in distances:
    di = calculate_image_distance(f, do)
    image_distances.append(di)

# Display the results
for do, di in zip(distances, image_distances):
    print(f'For an object at a distance of {do} mm, the image plane should be at a distance of {di:.3f} mm.')

# Now suppose we know the object and image distances and want to calculate the focal length
do_known = 3000  # Known object distance in mm
di_known = 2000  # Known image distance in mm

# Calculate the focal length
f_calculated = calculate_focal_length(do_known, di_known)

# Display the result
print(f'For an object at a distance of {do_known} mm and an image at a distance of {di_known} mm, the focal length is {f_calculated:.3f} mm.')
