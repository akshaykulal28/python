import time

# 1. Environment Setup: Position [x,y], Goal (x,y), Obstacles {set}
pos, goal = [0, 0], (4, 4)
obs = {(1, 0), (1, 1), (2, 3), (3, 2)} 

print(f"Start: {pos} | Goal: {goal}")

# 2. Main Loop (The Agent's Lifecycle)
while tuple(pos) != goal:
    x, y = pos
    
 
    if x < goal[0] and (x + 1, y) not in obs: 
        pos[0] += 1; action = "Right"
  
    elif y < goal[1] and (x, y + 1) not in obs: 
        pos[1] += 1; action = "Down"

    else: 
        print("Obstacle detected. Path blocked."); break
    
    print(f"Action: {action} -> New Pos: {pos}")
    time.sleep(0.5) 

if tuple(pos) == goal: print("Goal Reached!")