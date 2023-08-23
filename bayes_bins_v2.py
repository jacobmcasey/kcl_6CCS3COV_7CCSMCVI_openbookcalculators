def bayes_theorem_with_working(P_A, P_B, P_Ori1_given_A, P_Ori2_given_B, P_Ori1):
    # Calculate P(Ori2) which is the complement of P(Ori1)
    P_Ori2 = 1 - P_Ori1
    
    # Calculate the posterior probabilities using Bayes' theorem
    P_A_given_Ori1 = (P_Ori1_given_A * P_A) / P_Ori1
    P_B_given_Ori2 = (P_Ori2_given_B * P_B) / P_Ori2
    
    workings = [
        f"P(A) = {P_A}",
        f"P(B) = {P_B}",
        f"P(Ori1|A) = {P_Ori1_given_A}",
        f"P(Ori2|B) = {P_Ori2_given_B}",
        f"P(Ori1) = {P_Ori1}",
        f"P(Ori2) = {P_Ori2}",
        f"P(A|Ori1) = (P(Ori1|A) x P(A)) / P(Ori1) = ({P_Ori1_given_A} x {P_A}) / {P_Ori1} = {round(P_A_given_Ori1, 3)}",
        f"P(B|Ori2) = (P(Ori2|B) x P(B)) / P(Ori2) = ({P_Ori2_given_B} x {P_B}) / {P_Ori2} = {round(P_B_given_Ori2, 3)}",
    ]
    
    return "\n".join(workings)

# Given values
P_A = 0.5
P_B = 0.25
P_Ori1_given_A = 0.27
P_Ori2_given_B = 0.44
P_Ori1 = 0.95

# Using the function to compute and print results
print(bayes_theorem_with_working(P_A, P_B, P_Ori1_given_A, P_Ori2_given_B, P_Ori1))
