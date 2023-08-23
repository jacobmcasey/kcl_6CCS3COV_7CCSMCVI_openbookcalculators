##Jacob Casey KCL MSc Artificial Intelligence

def calculate_image_coordinates(point_3d, principal_point, magnification_factors):
    x_mm, y_mm, z_mm = point_3d
    pp_x, pp_y = principal_point
    mag_x, mag_y = magnification_factors

    x_pixel = round(pp_x + (x_mm / z_mm) * mag_x)
    y_pixel = round(pp_y + (y_mm / z_mm) * mag_y)

    # Print working out
    print(f"Working out:\n")
    print(f"X_pixel = Principal_Point_X + (X_mm / Z_mm) * Magnification_X")
    print(f"X_pixel = {pp_x} + ({x_mm} / {z_mm}) * {mag_x}")
    print(f"X_pixel = {pp_x} + {x_mm / z_mm} * {mag_x}")
    print(f"X_pixel = {pp_x + (x_mm / z_mm) * mag_x}")

    print(f"\nY_pixel = Principal_Point_Y + (Y_mm / Z_mm) * Magnification_Y")
    print(f"Y_pixel = {pp_y} + ({y_mm} / {z_mm}) * {mag_y}")
    print(f"Y_pixel = {pp_y} + {y_mm / z_mm} * {mag_y}")
    print(f"Y_pixel = {pp_y + (y_mm / z_mm) * mag_y}")

    return x_pixel, y_pixel

# Input values
point_3d = [50, 50, 500]  # Point coordinates in mm
principal_point = [400, 300]  # Principal point coordinates in pixels
magnification_factors = [-1333.3, -1000.0]  # Magnification factors in x and y directions

# Calculate image coordinates
x_pixel, y_pixel = calculate_image_coordinates(point_3d, principal_point, magnification_factors)

# Print the result
print(f"\nThe location of the point in the image is ({x_pixel}, {y_pixel}) pixels.")

