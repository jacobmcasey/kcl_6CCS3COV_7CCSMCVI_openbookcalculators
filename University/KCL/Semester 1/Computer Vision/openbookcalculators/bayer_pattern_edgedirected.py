def create_bayer_matrix(n, R_values, G_values, B_values):
    """Create a Bayer matrix of size n x n"""
    bayer_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Filling R values
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            bayer_matrix[i][j] = R_values.pop(0)

    # Filling B values
    for i in range(1, n, 2):
        for j in range(1, n, 2):
            bayer_matrix[i][j] = B_values.pop(0)

    # Filling G values
    g_index = 0
    for i in range(n):
        for j in range(n):
            if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                bayer_matrix[i][j] = G_values[g_index]
                g_index += 1

    return bayer_matrix


def interpolate_at_point(matrix, x, y):
    """Perform bilinear interpolation at point (x, y) based on the pixel's color in the Bayer matrix"""
    
    if x % 2 == 0 and y % 2 == 0:  # Red (R) pixel
        R_value = matrix[x][y]
        
        g_values = [matrix[x][y-1] if y-1 >= 0 else 0,
                    matrix[x-1][y] if x-1 >= 0 else 0,
                    matrix[x][y+1] if x-1 >= 0 else 0,
                    matrix[x+1][y] if x-1 >= 0 else 0,]
        G_value = sum(g_values) / 4
        
        B_values = [matrix[x-1][y-1] if x-1 >= 0 and y-1 >= 0 else 0,
                    matrix[x+1][y-1] if x-1 >= 0 and y-1 >= 0 else 0,
                    matrix[x-1][y+1] if x-1 >= 0 and y-1 >= 0 else 0,
                    matrix[x+1][y+1] if x-1 >= 0 and y-1 >= 0 else 0,]
        print(b_values)
        B_value = sum(b_values) / 4
        
        return (R_value, G_value, B_value)
    
    elif x % 2 == 1 and y % 2 == 1:  # Blue (B) pixel
        B_value = matrix[x][y]
        
        delta_H = abs(matrix[x][y+1] - matrix[x][y-1])
        delta_V = abs(matrix[x-1][y] - matrix[x+1][y])
        print(f"deltaH {delta_H}")
        
        g_values = [matrix[x][y-1] if y-1 >= 0 else 0,
                    matrix[x-1][y] if x-1 >= 0 else 0,
                    matrix[x][y+1] if x-1 >= 0 else 0,
                    matrix[x+1][y] if x-1 >= 0 else 0,]
        G_value = sum(g_values) / 4
        
        r_values = [matrix[x-1][y-1] if x-1 >= 0 and y-1 >= 0 else 0,
                    matrix[x+1][y-1] if x-1 >= 0 and y-1 >= 0 else 0,
                    matrix[x-1][y+1] if x-1 >= 0 and y-1 >= 0 else 0,
                    matrix[x+1][y+1] if x-1 >= 0 and y-1 >= 0 else 0,]
        print(r_values)
        R_value = sum(r_values) / 4
        
        return (R_value, G_value, B_value)
    
    else:  # Green (G) pixel
        G_value = matrix[x][y]

        r_values = [matrix[x-1][y] if x-1 >= 0 else 0,
                    matrix[x+1][y] if x+1 < len(matrix) else 0]
        R_value = sum(r_values) / 4
        
        b_values = [matrix[x][y-1] if y-1 >= 0 else 0,
                    matrix[x][y+1] if y+1 < len(matrix[0]) else 0]
        B_value = sum(b_values) / 4

        return (R_value, G_value, B_value)

# Example usage
R_values = [0.2, 0.3, 0.4, 0.3]
G_values = [0.7, 0.6, 0.1, 0.6, 0.8, 0.9, 0.4, 0.1]
B_values = [0.2, 0.3, 0.4, 0.6]

bayer = create_bayer_matrix(4, R_values, G_values, B_values)

print(bayer)

### input is zero indexed.
print("Interpolated RGB at (2,2):", interpolate_at_point(bayer, 1, 1))
