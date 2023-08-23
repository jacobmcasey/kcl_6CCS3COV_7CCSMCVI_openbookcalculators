# ---- Functions ----

def compute_depth_horizontal(f, Vx, x1, x2, delta_t, pixel_size):
    """Compute depth for horizontal camera movement."""
    x_dot = (x2 - x1) / delta_t
    x_dot_m_per_s = x_dot * pixel_size
    Z = -f * Vx / x_dot_m_per_s
    return Z

def compute_depth_optical(x1_centered, Vz, x1, x2, delta_t):
    """Compute depth when the camera is moving along the optical axis."""
    x_dot = (x2 - x1) / delta_t
    Z2 = x1_centered * Vz / x_dot
    return Z2

def compute_collision_time(x1_centered, x1, x2, delta_t):
    """Compute the time before the camera collides with the scene point."""
    x_dot = (x2 - x1) / delta_t
    ttc = x1_centered / x_dot
    return ttc

# ---- Guidance on setting variables based on the question ----

# For Question 'b':
# This deals with a horizontal camera movement, as evident from "camera is moving along the x-axis".
# Given data:
# Initial point = 110 (from "The point (110,50,t) in the first image")
# Corresponding point in the next frame = 95 (from "correspond to the point (95,50,t+0.04) in the second image")
# Vx (horizontal camera velocity) = 0.5 m/s
# Focal length (f) = 35mm = 0.035 meters
# Pixel size = 0.1mm/pixel = 0.0001 meters/pixel
# Time between frames (delta_t) = 0.04s
depth_a = compute_depth_horizontal(0.035, 0.5, 110, 95, 0.04, 0.0001)
print(f"Depth for part a (horizontal camera movement): {depth_a:.3f} m")

# For Question 'c':
# Here, the camera is moving along its optical axis (z-axis).
# Given data:
# Initial point = 140 (from "The point (140,100,t) in the first image")
# Corresponding point in the next frame = 145
# The camera is moving along its optical axis, so consider its velocity (Vz) = 0.5 m/s
# Image center coordinates = (100,100). So, the x-coordinate relative to the center (x1_centered) = 140 - 100 = 40
depth_b = compute_depth_optical(40, 0.5, 140, 145, 0.04)
print(f"Depth for part b (camera moving along optical axis): {depth_b:.3f} m")

# For Question 'd':
# We need to determine the time until the camera collides with the scene point.
# We can utilize the values from the previous calculation in 'c' since it mentions "the scene point in question 5.c".
collision_time = compute_collision_time(40, 140, 145, 0.04)
print(f"Time-to-collision: {collision_time:.2f} s")
