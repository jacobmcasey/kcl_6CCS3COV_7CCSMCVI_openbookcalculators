
    return dot_product / (norm_A * norm_B)

ClassA = np.array([2.5, 3.5, 0.5, 2])
ClassB = np.array([0.5, 1.5, 3.5, 1])
New = np.array([2, 1, 2, 3])

similarity_A = cosine_similarity(ClassA, New)
similarity_B = cosine_similarity(ClassB, New)
print("Similarity with ClassA:", similarity_A)
print("Similarity with ClassB:", similarity_B)
