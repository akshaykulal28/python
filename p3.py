# 1. Sample Space (S): The set of all possible outcomes
S = {1, 2, 3, 4, 5, 6}

# 2. Event (E): The subset of outcomes we care about (e.g., Even numbers)
E = {x for x in S if x % 2 == 0}

# 3. Probability P(E): The size of Event divided by size of Sample Space
p_val = len(E) / len(S)

print(f"Sample Space (S): {S}")
print(f"Event (E):        {E}")
print(f"P(E) = |E|/|S|:   {p_val:.2f} (or {p_val:.0%})")