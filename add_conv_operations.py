def calculate_DoG_operations(mask_length, image_width, image_height, separable_operations):
    # Convolution with one Gaussian (using separable masks)
    convolve_one_gaussian = separable_operations
    print(f"To convolve the image with one Gaussian (using separable masks) requires {convolve_one_gaussian} floating-point operations \n")
    
    # Convolution with another Gaussian (using separable masks)
    convolve_another_gaussian = separable_operations
    print(f"To convolve the image with another Gaussian (using separable masks) requires {convolve_another_gaussian} floating-point operations \n")
    
    # Subtraction operation
    subtraction_operations = image_width * image_height
    print(f"To subtract one result from the other requires {image_width} x {image_height} = {subtraction_operations} floating-point operations \n")
    
    # Total number of floating-point operations
    total_operations = convolve_one_gaussian + convolve_another_gaussian + subtraction_operations
    print(f"So in total {convolve_one_gaussian} + {convolve_another_gaussian} + {subtraction_operations} = {total_operations} = {total_operations:.1e} floating-point operations \n")

    return total_operations

def calculate_operations(mask_size, image_width, image_height):
    # Number of multiplications for each element in the mask
    multiplications = mask_size[0] * mask_size[1]
    print(f"\nAt each location, {mask_size[0]} x {mask_size[1]} multiplications are performed = {multiplications} multiplications \n")
    
    # Number of additions for each element in the mask (subtracting one for the total number of elements)
    additions = (mask_size[0] * mask_size[1]) - 1
    print(f"At each location, {mask_size[0]} x {mask_size[1]} - 1 additions are performed = {additions} additions \n")

    # Total number of floating-point operations for one element in the output image
    operations_per_pixel = multiplications + additions
    print(f"Total operations at each location = {operations_per_pixel} floating-point operations \n")
    
    # Total number of floating-point operations for the entire output image
    total_operations = operations_per_pixel * image_width * image_height
    print(f"This is repeated for every pixel in the output, i.e., {image_width} x {image_height} x {operations_per_pixel} = {total_operations} floating-point operations \n")

    return total_operations

def calculate_separable_operations(mask_length, image_width, image_height):
    # Number of multiplications and additions for a 1D convolution (mask_length + mask_length - 1)
    operations_per_pixel = (mask_length + mask_length - 1)
    print(f"To convolve the image with a 1D Gaussian requires ({mask_length} + {mask_length} - 1) x {image_width} x {image_height} = {operations_per_pixel * image_width * image_height} floating-point operations \n")
    
    # Total number of floating-point operations for the entire output image (twice for two 1D convolutions)
    total_operations = 2 * operations_per_pixel * image_width * image_height
    print(f"To convolve the result with a 1D Gaussian requires the same, so total is {operations_per_pixel * image_width * image_height} x 2 = {total_operations} floating-point operations \n")

    return total_operations

# Previous code for regular convolution (calculate_operations function)...

mask_size = (11, 11)
image_width = 200
image_height = 300

print("==========================================")
print("Calculating without exploiting separability:")
total_operations = calculate_operations(mask_size, image_width, image_height)
print(f"The total number of floating-point operations is {total_operations} or approximately {total_operations:.1e}\n")
print("==========================================")

mask_length = 11

print("Calculating with exploiting Gaussian separability:")
total_operations_separable = calculate_separable_operations(mask_length, image_width, image_height)
print(f"The total number of floating-point operations (using separability) is {total_operations_separable} or approximately {total_operations_separable:.1e}\n")
print("==========================================")

print("Calculating with exploiting Gaussian separability for DoG mask:")
total_operations_DoG = calculate_DoG_operations(mask_length, image_width, image_height, total_operations_separable)
print(f"The total number of floating-point operations (using separability for DoG mask) is {total_operations_DoG} or approximately {total_operations_DoG:.1e}\n")
print("==========================================")