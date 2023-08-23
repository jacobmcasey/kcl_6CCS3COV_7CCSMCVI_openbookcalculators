import numpy as np

def dI(edge_image, point):
    # Calculate the minimum distance from point to the nearest edge point in edge_image
    distances = []
    for i in range(edge_image.shape[0]):
        for j in range(edge_image.shape[1]):
            if edge_image[i, j] == 1:
                dist = np.sqrt((i - point[0]) ** 2 + (j - point[1]) ** 2)
                distances.append(dist)
    return min(distances)

def edge_matching(template, image):
    template_height, template_width = template.shape
    image_height, image_width = image.shape
    
    min_distance = float('inf')
    best_location = None
    results = []

    # Iterate over all possible positions where the template fits entirely within the image
    for i in range(image_height - template_height + 1):
        for j in range(image_width - template_width + 1):
            current_distance = 0
            distances = []
            
            # For every point in the template
            for x in range(template_height):
                for y in range(template_width):
                    if template[x, y] == 1:  # edge point in the template
                        dist = dI(image[i:i+template_height, j:j+template_width], (x, y))
                        distances.append(dist)
                        current_distance += dist
            
            # Compute average distance
            current_distance /= np.sum(template)
            
            results.append((current_distance, (i, j), distances))

            # Update the minimum distance and best location
            if current_distance < min_distance:
                min_distance = current_distance
                best_location = (i, j)

    # Format the results
    output = ""
    for avg_distance, location, dist_list in results:
        formatted_distances = '+'.join(['√{:.0f}'.format(dist ** 2) if dist % 1.0 else str(int(dist)) for dist in dist_list])
        output += "At pixel{} Distance= 1/{} [{}]={:.3f}\n".format(location, len(dist_list), formatted_distances, avg_distance)
    
    output += "\nHence, object at location{}.".format(best_location)
    return output

# Provided binary edge template and image
T = np.array([[1, 1, 1], 
              [1, 0, 1], 
              [1, 1, 1]])

I = np.array([[0, 0, 0, 0], 
              [1, 1, 1, 0], 
              [0, 0, 1, 0], 
              [1, 1, 1, 0]])

print(edge_matching(T, I))
