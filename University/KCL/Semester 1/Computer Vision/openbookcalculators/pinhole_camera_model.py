#Be careful here of metrics etc

# Input given values usually (x,y,z)
x_meters, y_meters, z_meters = 0.4, 0.5, 6

# Input focal length
f_mm = 30

# Convert x and y to millimeters
x_mm = x_meters * 1000
y_mm = y_meters * 1000
z_mm = z_meters * 1000

# Apply the pinhole camera model
x_prime = (f_mm * x_mm) / z_mm
y_prime = (f_mm * y_mm) / z_mm

print(f"The image coordinates are: x' = {x_prime}mm, y' = {y_prime}mm")
