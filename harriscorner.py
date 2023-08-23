import numpy as np

def harris_response(Ix, Iy, k, window_size=3):
    rows, cols = Ix.shape
    result = np.zeros((rows, cols))
    offset = window_size // 2

    # Pad the derivatives with zeros to accommodate the window at the edges
    padded_Ix = np.pad(Ix, offset, 'constant')
    padded_Iy = np.pad(Iy, offset, 'constant')

    for i in range(rows):
        for j in range(cols):
            window_Ix = padded_Ix[i:i + window_size, j:j + window_size]
            window_Iy = padded_Iy[i:i + window_size, j:j + window_size]

            I2x = (window_Ix ** 2).sum()
            I2y = (window_Iy ** 2).sum()
            IxIy = (window_Ix * window_Iy).sum()

            R = (I2x * I2y) - (IxIy ** 2) - k * (I2x + I2y) ** 2

            result[i, j] = R

    return result

Ix = np.array([[3, 0.5, -2],
               [0, -0.5, -1],
               [0, 1, 2]])

Iy = np.array([[2, -1, 0],
               [0.5, -1, 1],
               [-1, -1, 2]])

k = 0.05

response = harris_response(Ix, Iy, k)
print("Harris response for all pixels:")
print(response)