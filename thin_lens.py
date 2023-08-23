## Jacob Casey KCL MSc Artificial Intelligence

# Function Definitions
def calculate_image_distance(f, do):
    """Calculate the image distance (di) using the focal length (f) and object distance (do) in mm."""
    return 1 / (1/f - 1/do)

def calculate_focal_length(do, di):
    """Calculate the focal length (f) using the object distance (do) and image distance (di) in mm."""
    return 1 / (1/do + 1/di)

def calculate_object_distance(f, di):
    """Calculate the object distance (do) using the focal length (f) and image distance (di) in mm."""
    return 1 / (1/f - 1/di)

# Constants
f = 30  # Focal length in mm
distances = [6000]  # Object distances in mm (you can add multiple, ensure values are in mm)

# Calculating and Storing Image Distances
image_distances = [calculate_image_distance(f, do) for do in distances]

# Displaying Image Distances
for do, di in zip(distances, image_distances):
    print(f'For an object at a distance of {do} mm, the image plane should be at a distance of {di:.3f} mm.')

# Calculating and Displaying Object Distance Example
f_known = 30
di_known = 2000
do_calculated = calculate_object_distance(f_known, di_known)
print(f'\nFor a focal length of {f_known} mm and an image at a distance of {di_known} mm, the object distance is {do_calculated:.3f} mm.')

# Below part is for calculating the focal length if you know the object and image distances.
do_known = 3000
di_known = 2000
f_calculated = calculate_focal_length(do_known, di_known)
print(f'\nFor an object at a distance of {do_known} mm and an image at a distance of {di_known} mm, the focal length is {f_calculated:.3f} mm.')