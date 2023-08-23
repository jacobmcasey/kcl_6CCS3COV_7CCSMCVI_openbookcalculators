import numpy as np
import cv2

# Binary Image Input
img = np.array([[0, 1, 1], 
                [0, 0, 1],
                [0, 1, 0]])

SHAPE = 'cross'  #'cross' for V/H, 'square' for V/H/D

def apply_morphology(image, operation, struct_element):
    image = image.astype(np.uint8)

    # Define the structuring element
    if struct_element == 'cross':
        struct = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    elif struct_element == 'square':
        struct = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    else:
        raise ValueError(f"Invalid structuring element {struct_element}. Choose 'cross' or 'square'")

    # Perform the chosen operation
    if operation == 'dilation':
        result = cv2.dilate(image, struct)
    elif operation == 'erosion':
        result = cv2.erode(image, struct)
    elif operation == 'opening':
        result = cv2.morphologyEx(image, cv2.MORPH_OPEN, struct)
    elif operation == 'closing':
        result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, struct)
    else:
        raise ValueError(f"Invalid operation {operation}. Choose 'dilation', 'erosion', 'opening', or 'closing'")
    
    print(result)
    return result

print("\n---Initial Image---")
print(img)

# Apply dilation on the original image
print("\n---Dilation---")
result_dilation = apply_morphology(img, 'dilation', SHAPE)

# Apply erosion on the original image
print("\n---Erosion---")
result_erosion = apply_morphology(img, 'erosion', SHAPE)

# Perform closing on the original image
print("\n---Closing---")
result_closing = apply_morphology(img, 'closing', SHAPE)

# Perform opening on the original image
print("\n---Opening---")
result_opening = apply_morphology(img, 'opening', SHAPE)
