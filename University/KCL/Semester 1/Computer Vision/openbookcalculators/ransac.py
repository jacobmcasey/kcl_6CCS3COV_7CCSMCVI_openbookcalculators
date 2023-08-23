def calculate_distance(p1, p2):
    """Compute Euclidean distance between two points."""
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# ... [rest of the code remains unchanged]

def sad(descriptor1, descriptor2):
    """Compute Sum of Absolute Differences between two descriptors."""
    return sum(abs(a - b) for a, b in zip(descriptor1, descriptor2))

def find_best_match_for_point(descriptor, descriptorsB):
    """Find the best match for a given descriptor in Image A among descriptors in Image B."""
    best_match_index = None
    best_match_value = float('inf')
    for i, descriptorB in enumerate(descriptorsB):
        current_sad = sad(descriptor, descriptorB)
        if current_sad < best_match_value:
            best_match_value = current_sad
            best_match_index = i
    return best_match_index

def apply_ransac(pointsA, pointsB, matches, threshold=20.0):
    best_consensus = -1
    best_translation = (0, 0)
    for i, match in enumerate(matches):
        dx = pointsB[match][0] - pointsA[i][0]
        dy = pointsB[match][1] - pointsA[i][1]
        consensus_set = 0
        for j, inner_match in enumerate(matches):
            model_prediction = (pointsA[j][0] + dx, pointsA[j][1] + dy)
            distance = calculate_distance(model_prediction, pointsB[inner_match])
            if distance < threshold:
                consensus_set += 1
        if consensus_set > best_consensus:
            best_consensus = consensus_set
            best_translation = (dx, dy)
    return best_translation

pointsA = [(47,21), (51,34), (92,58)]
pointsB = [(49,45), (27,9), (58,57), (88,54), (7,77)]
descriptorsA = [(1.0,0.5,1.0), (0.3,0.5,0.0), (0.8,0.9,0.7)]
descriptorsB = [(0.2,0.7,0.4), (0.4,0.7,0.6), (0.2,1.0,0.3), (0.9,0.7,0.4), (1.0,0.6,0.4)]

matches = [find_best_match_for_point(descriptor, descriptorsB) for descriptor in descriptorsA]
ransac_translation = apply_ransac(pointsA, pointsB, matches)

answers = ["b" + str(matches[i] + 1) for i in range(3)]
answers.append(ransac_translation[0])
answers.append(ransac_translation[1])

print("Best matching point for a1:", answers[0])
print("Best matching point for a2:", answers[1])
print("Best matching point for a3:", answers[2])
print("Estimation of the translation from A to B determined by RANSAC:", (answers[3], answers[4]))
print("In a sentence or two, briefly describe what steps you used to determine the best matching interest point in image B for each interest point in image A.")
print("The best matching point in image B for each interest point in image A was determined by calculating the sum of absolute differences (SAD) of their descriptors. The point with the lowest SAD value was considered the best match.")
