import random
T, C = list("AI_EVOLUTION"), "AI_EVOLUTION_XYZ" # Target & Charset
P = [random.choices(C, k=len(T)) for _ in range(100)] # Init Population

for g in range(5000):
    P.sort(key=lambda p: sum(a==b for a,b in zip(p, T)), reverse=True) # Fitness Sort
    if P[0] == T: print(f"Gen {g}: {''.join(P[0])}"); break
    
    # Selection (Top 10) + Crossover + Mutation (All in one structure)
    P = P[:10] + [
        [c if random.random() > 0.1 else random.choice(C) 
         for c in (random.choice(P[:10])[:i] + random.choice(P[:10])[i:])]
        for _ in range(90) for i in [random.randint(0, len(T))]
    ]