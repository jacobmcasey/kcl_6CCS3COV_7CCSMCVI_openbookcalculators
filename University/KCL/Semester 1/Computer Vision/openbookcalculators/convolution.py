import numpy as np
from scipy.ndimage import rotate
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

# Example usage:
# Define your mask and images here.
# Replace these with the mask, I1 given in the exam.
# Remember to look for rounding to integer

mask = np.array([[0.00563, 0.06654, 0.00563],
            [0.06654, 0.78595, 0.06654],
            [0.00563, 0.06654, 0.00563]])

image_I1 = np.array([[-0.125, -0.125, -0.125],
            [-0.125, 1, -0.125],
            [-0.125, -0.125, -0.125]])

#valid: No padding is applied. The convolution operation is only computed where the input and the filter fully overlap. As a result, the output size is smaller than the input size.
#same: Padding is added to the input so that the output has the same width and height as the original input. This is achieved by padding the input in such a way that the filter fits perfectly when slid on top of the borders. The amount of padding depends on the size of the filter. If the filter is of size F, then the input is padded with F//2 rows/columns on each side.
#full: Padding is added to the input so that every possible overlap between the input and the filter is computed. This results in an output that is larger than the input. If the filter is of size F, then the input is padded with F-1 rows/columns on each side.
padding = 'same'

def flip_mask(mask):
    # Flip vertically then horizontally == rotation 180 degrees.
    flipped_mask = np.flip(np.flip(mask, 0), 1)
    return flipped_mask

def convolve(image, mask, padding='valid'):
    # Perform the convolution
    # Default padding as valid, but will be overridden when called
    if padding == 'same':
        output = convolve2d(image, mask, mode='same')
    elif padding == 'valid':
        output = convolve2d(image, mask, mode='valid')
    elif padding == 'full':
        output = convolve2d(image, mask, mode='full')
    else:
        raise ValueError(f'Invalid padding mode: {padding}. Choose from "same", "valid" or "full".')
    return output

# Verbose output and visualization
print(f"Performing convolution with '{padding}' padding for Image I1:")
result_I1 = convolve(image_I1, mask, padding=padding)

print(f"\nMask H:\n{mask}")
# The mask is rotated and convolution is performed with specified padding.
# The results are printed for both I1
flipped_mask = flip_mask(mask)
print(f"\nFlipped/Rotated mask R(H):")
print(flipped_mask)
print(f"\nInput Image I1:\n{image_I1}")
print()
print(f"\nResult feature map F with '{padding}' padding for Image I1. F=R(H)*I1:\n{result_I1}")
print()
print(f"\nResult rounded feature map F with '{padding}' padding for Image I1. F=R(H)*I1:\n{np.round(result_I1).astype(int)}")

# Plotting example
fig, axs = plt.subplots(1, 3, figsize=(10, 4))
axs[0].imshow(mask, cmap='gray')
axs[0].set_title('Mask H')
axs[1].imshow(image_I1, cmap='gray')
axs[1].set_title('Input Image I1')
axs[2].imshow(result_I1, cmap='gray')
axs[2].set_title(f"Convolution Result F ({padding} padding)")
plt.tight_layout()
plt.show()
