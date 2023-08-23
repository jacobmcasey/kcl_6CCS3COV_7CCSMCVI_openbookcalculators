# Given parameters
f = 20  # Focal length in mm
ccd_width = 12  # CCD array width in mm
ccd_height = 12  # CCD array height in mm
pixels_x = 800  # Number of pixels in x-direction
pixels_y = 600  # Number of pixels in y-direction

# Calculate pixel sizes
s_x = ccd_width / pixels_x
s_y = ccd_height / pixels_y

# Calculate magnification factors
alpha = -f / s_x
beta = -f / s_y

print(f"Answer:")
print(f"Pixel size in x and y directions are:")
print(f"s_x = {ccd_width} / {pixels_x} = {s_x:.3f}mm/pixel")
print(f"s_y = {ccd_height} / {pixels_y} = {s_y:.3f}mm/pixel\n")

print(f"Magnification factor = -f / s.")
print(f"Hence:")
print(f"α = -f / s_x = -{f} / {s_x:.3f} = {alpha:.1f}")
print(f"β = -f / s_y = -{f} / {s_y:.3f} = {beta:.1f}")
