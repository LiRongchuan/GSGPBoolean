import random

def fbm(P, B):
    """
    Parameters:
        P : parent program, a function from {0,1}^n -> {True, False}
        B : list of variable indices to mutate over (subset of {0, ..., n-1})

    Returns:
        A new mutated Boolean function: {0,1}^n -> {True, False}
    """
    # Build the mask M(x): {0,1}^n → {True, False}, representing a combination of variables in B
    mask = [random.randint(0, 1) for _ in range(len(B))]
    def M(x):
        return all(x[i] if m else not x[i] for i, m in zip(B, mask))
    # Add the combination to parent program
    positive = random.random() < 0.5
    if positive:
        return lambda x: P(x) or M(x)
    else:
        return lambda x: P(x) and not M(x)

if __name__ == '__main__':
    def P(x):
        return x[0] == 1 and x[1] == 0
    B = [1]
    P_prime = fbm(P, B)
    x_1 = (0, 1)
    x_2 = (1, 0)
    print("P(x):", P(x_1))
    print("P'(x):", P_prime(x_1))
