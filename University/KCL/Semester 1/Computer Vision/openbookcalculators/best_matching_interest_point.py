# Define the feature values for the points
left_points = {
    "L1": (1, 2, 4, 2),
}

right_points = {
    "R1": (2, 3, 2, 2),
    "R2": (1, 2, 1, 0),
    "R3": (1, 5, 4, 1),
}

# Function to calculate SAD
def calculate_sad(left_point, right_point):
    return sum(abs(l-r) for l, r in zip(left_point, right_point))

# Iterate through the left points and find the best matching right point(s)
for left_key, left_point in left_points.items():
    min_sad = float('inf')
    best_matches = []

    print(f"\nFor {left_key}, SAD:")

    # Iterate through the right points and calculate SAD
    for right_key, right_point in right_points.items():
        sad = calculate_sad(left_point, right_point)
        print(f"{right_key}:{sad};\t", end=" ")

        if sad < min_sad:
            min_sad = sad
            best_matches = [right_key]
        elif sad == min_sad:
            best_matches.append(right_key)

    matches_str = ", ".join(best_matches)
    print(f"\nTherefore best match(es) is/are {matches_str}.\n")
