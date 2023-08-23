# Given variables
camera_movement_speed = 0.4  # m/s along the z-axis
centre_of_image = (50, 50)  # pixel coordinates

# Initial and final positions of the point in image
initial_position = (64, 57)  # pixel
final_position = (90, 70)  # pixel

# Calculate position relative to the center of the image
relative_initial_position = (initial_position[0] - centre_of_image[0], initial_position[1] - centre_of_image[1])
relative_final_position = (final_position[0] - centre_of_image[0], final_position[1] - centre_of_image[1])

print(f"Relative initial position of the point: {relative_initial_position}")
print(f"Relative final position of the point: {relative_final_position}\n")

# Time difference between the two frames
time_difference = 0.5  # s  (1ms = 0.01)

# Calculate velocity of the image point in pixels per second
velocity_pixels_per_s = (relative_final_position[0] - relative_initial_position[0]) / time_difference  # pixels/s

print(f"Velocity of the image point: {velocity_pixels_per_s} pixels/s\n")

# Calculate depth using provided formula
depth = relative_initial_position[0] * camera_movement_speed / velocity_pixels_per_s  # m

print(f"The depth of the scene point is: {depth} meters")

# Calculate time-to-collision using provided formula
time_to_collision = relative_initial_position[0] / velocity_pixels_per_s  # s

print(f"The time-to-collision is: {time_to_collision} seconds")