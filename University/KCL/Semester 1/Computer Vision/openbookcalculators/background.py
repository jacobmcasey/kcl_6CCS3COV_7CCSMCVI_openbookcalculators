import numpy as np

# Arrays
I_t1 = np.array([180, 200, 100, 110, 90])
I_t2 = np.array([110, 170, 160, 90, 60])
I_t3 = np.array([100, 70, 170, 200, 80])
I_t4 = np.array([90, 100, 90, 190, 190])

threshold = 30

# Step 1: Calculate background
background = (I_t1 + I_t2 + I_t3 + I_t4) / 4
print(f"Background (B): {background}")

# Step 2 and 3: Subtract background and apply threshold
def bg_subtraction_with_details(frame, bg, threshold):
    difference = np.abs(frame - bg)
    print(f"Difference: {difference}")
    return difference > threshold

print("\nt1 segmentation:")
segmentation_t1 = bg_subtraction_with_details(I_t1, background, threshold)
print(segmentation_t1.astype(int))

print("\nt2 segmentation:")
segmentation_t2 = bg_subtraction_with_details(I_t2, background, threshold)
print(segmentation_t2.astype(int))

print("\nt3 segmentation:")
segmentation_t3 = bg_subtraction_with_details(I_t3, background, threshold)
print(segmentation_t3.astype(int))

print("\nt4 segmentation:")
segmentation_t4 = bg_subtraction_with_details(I_t4, background, threshold)
print(segmentation_t4.astype(int))
