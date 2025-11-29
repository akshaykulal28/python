board = [0] * 9  # 0=Empty, 1=AI(X), -1=Human(O)
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def check(b):
    for x, y, z in wins:
        if abs(b[x] + b[y] + b[z]) == 3: return b[x] # Return 1 or -1
    return 0

def minimax(b, is_max):
    winner = check(b)
    if winner != 0 or 0 not in b: return winner
    
    scores = []
    for i in [i for i, x in enumerate(b) if x == 0]:
        b[i] = 1 if is_max else -1
        scores.append(minimax(b, not is_max))
        b[i] = 0 # Backtrack
        
    return max(scores) if is_max else min(scores)

# --- Game Loop ---
print("You are 'O' (-1). Enter 0-8:")
while 0 in board and check(board) == 0:
    # 1. Human Move
    if board.count(0) % 2 != 0: # AI goes first if you want, currently Human first (9 empties)
        try: board[int(input("Move: "))] = -1
        except: continue
    # 2. AI Move (Minimax)
    else:
        best = -float('inf'); move = -1
        for i in [i for i, x in enumerate(board) if x == 0]:
            board[i] = 1
            score = minimax(board, False)
            board[i] = 0
            if score > best: best = score; move = i
        board[move] = 1
        print(f"AI chose: {move}")

    print(f"Board: {[ 'X' if x==1 else 'O' if x==-1 else '.' for x in board ]}")

print("Result:", "AI Won" if check(board)==1 else "Human Won" if check(board)==-1 else "Draw")