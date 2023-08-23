import numpy as np

def downsample_image(image, factor):
    # Input validation
    if factor <= 0 or not isinstance(factor, int):
        raise ValueError("Downsampling factor must be a positive integer.")
    if image.shape[0] < factor or image.shape[1] < factor:
        raise ValueError("Image is smaller than the downsampling factor.")

    # Downsample the image by taking the second element of each block
    downsampled_image = image[1::factor, 1::factor]
    return downsampled_image

# Define the image to downsample
image = np.array([[0.1, 0.7, 1, 1],
            [0.7, 0.4, 0.5, 0.2],
            [0.4, 0.3, 0.4, 0.9],
            [0.8, 0.3, 0.4, 0]])


# Downsample the image
downsampled_image = downsample_image(image, 2)

# Print the downsampled image
print(f"Downsampled image:\n{downsampled_image}")
