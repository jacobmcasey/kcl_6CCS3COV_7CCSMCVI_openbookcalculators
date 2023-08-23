import numpy as np
from scipy import ndimage

def upsample_bilinear(matrix, scale):
    return ndimage.zoom(matrix, scale)

def upsample_smooth_hue_transition(matrix, scale):
    # Upsample using simple bilinear interpolation
    upsampled = upsample_bilinear(matrix, scale)

    # Apply smooth hue transition interpolation
    smooth_hue = ndimage.gaussian_filter(upsampled, sigma=1)
    return smooth_hue

def upsample_edge_directed(matrix, scale):
    # Upsample using simple bilinear interpolation
    upsampled = upsample_bilinear(matrix, scale)

    # Compute structuring element size
    height, width = upsampled.shape
    se_height = max(3, height // 10)
    se_width = max(3, width // 10)
    size = (se_height, se_width)

    # Apply edge-directed interpolation
    edge_directed = ndimage.grey_dilation(upsampled, size=size)
    return edge_directed

# Example usage
matrix = np.array([[177, 243],
                   [81, 8]])

scale_factor = 1.5

bilinear_result = upsample_bilinear(matrix, scale_factor)
smooth_hue_result = upsample_smooth_hue_transition(matrix, scale_factor)
edge_directed_result = upsample_edge_directed(matrix, scale_factor)

print("Bilinear Interpolation:")
print(bilinear_result)

print("\n\n*Experimental: The below outputs need checking*")
print("\nSmooth Hue Transition Interpolation:")
print(smooth_hue_result)

print("\nEdge-Directed Interpolation:")
print(edge_directed_result)
