import numpy as np

# Given data
I = np.array([-5,-3,2])
H = np.array([0.9, 0.5, 0.8]).reshape(3, 1)

# Convolution
result = np.outer(I, H).T

print(result)

# Given data
I = np.array([1,0.5,0.1])
H = I.reshape(3, 1)

# Convolution
result = np.outer(I, H).T

print(result)
