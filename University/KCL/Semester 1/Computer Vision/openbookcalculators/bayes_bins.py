def bayes_theorem_with_working(ratio_A_to_B, P_Ori_given_A, P_Ori_given_B):
    # Calculate the probabilities of objA and objB based on the given ratio
    P_A = 0.5
    P_B = 0.25

    # Calculate total probability
    P_I_value = P_Ori_given_A * P_A + P_Ori_given_B * P_B

    # Constructing the workings based on provided format
    workings = [
        f"p(objA)={P_A:.5f}",
        f"p(objB)={P_B:.5f}",
        f"p(I|objA)={P_Ori_given_A:.5f}",
        f"p(I|objB)={P_Ori_given_B:.5f}",
        f"p(objA|I)=p(I|objA)p(objA) p(I) =k({P_Ori_given_A:.5f}×{P_A:.5f})={(P_Ori_given_A * P_A):.5f}k",
        f"p(objB|I)=p(I|objB)p(objB) p(I) =k({P_Ori_given_B:.5f}×{P_B:.5f})={(P_Ori_given_B * P_B):.5f}k"
    ]

    # Add conclusion based on computed probabilities
    conclusion = "*Hence, indistinguishable images are most likely to contain objA." if P_Ori_given_A * P_A > P_Ori_given_B * P_B else "Hence, indistinguishable images are most likely to contain objB."
    workings.append(conclusion)

    # Further workings and explanations
    workings.extend([
        f"\nNote k = 1/p(I) which is the same for both possibilities, so its value is not important to answer this particular question. However, if we needed to calculate the absolute posteriors then we would need to calculate p(I).\n",
        f"p(I)=p(I|objA)p(objA)+p(I|objB)p(objB)=({P_Ori_given_A:.5f}×{P_A:.5f})+({P_Ori_given_B:.5f}×{P_B:.5f})={P_I_value:.5f}",
        f"So:\np(objA|I)={(P_Ori_given_A * P_A):.5f} / {P_I_value:.5f}={(P_Ori_given_A * P_A) / P_I_value:.5f}",
        f"p(objB|I)={(P_Ori_given_B * P_B):.5f} / {P_I_value:.5f}={(P_Ori_given_B * P_B) / P_I_value:.5f}\n"
    ])

    return "\n".join(workings)

# Example usage:
print(bayes_theorem_with_working(3, 0.27, 0.44))  # Given: 3 times as many objA as objB, P_Ori_given_A = 0.1, P_Ori_given_B = 0.2
