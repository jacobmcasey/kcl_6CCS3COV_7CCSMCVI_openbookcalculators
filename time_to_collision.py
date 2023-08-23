# Inputs required:

# relative_initial_position_x: This is the x coordinate of the initial position of the scene point 
# in the first image frame, relative to the center of the image. This value was calculated in the previous script.

# velocity_pixels_per_s: This is the velocity of the scene point in the image frame (in pixels per second),
# which is calculated from the change in the scene point's position over the time difference between frames.

# Replace these inputs with the actual values provided in your exam.

relative_initial_position_x = 40  # x-coordinate relative to center of the image
velocity_pixels_per_s = 125  # velocity of the scene point in pixels per second

# Calculate time-to-collision using the formula: time-to-collision = x1 / x_dot
time_to_collision = relative_initial_position_x / velocity_pixels_per_s

print(f"The time-to-collision is: {time_to_collision} seconds")