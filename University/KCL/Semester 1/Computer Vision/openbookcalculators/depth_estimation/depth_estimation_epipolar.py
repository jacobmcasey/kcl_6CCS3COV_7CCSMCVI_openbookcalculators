# Given variables

# Focal length of the camera. The distance from the camera's lens to its image sensor when the subject (in our case, the 3D point) is in focus.
focal_length = 30  # mm

# Displacement of the right camera along the x-axis relative to the left one. This is also known as the "baseline".
# It's the distance between the two camera centers.
displacement = 400  # mm

# The size of each pixel on the camera's image sensor. It determines the resolution at which the camera captures details.
pixel_size = 0.1  # mm/pixel

# Coordinates of point P in the left and right images.

# x-coordinate of the 3D point as seen in the left camera's image.
xL = 231  # from left image

# x-coordinate of the same 3D point but as seen in the right camera's image. 
# It's derived from our previous results.
xR = 45   # from 5.c result

# Calculating depth using the formula derived from the principles of epipolar geometry.
# Depth is inversely proportional to the difference in x-coordinates (disparity) of the point 
# as seen in the left and right images. The larger the disparity, the closer the object is.
depth = (focal_length * displacement) / (pixel_size * (xL - xR))

print(f"The depth of the 3D point P is: {depth} mm")
