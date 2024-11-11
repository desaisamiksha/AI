from collections import deque

def water_jug_bfs(x_capacity, y_capacity, target):
    
    visited = set()  
    q = deque()      

    
    q.append((0, 0))  

    while q:
        curr_x, curr_y = q.popleft()

        
        if (curr_x, curr_y) in visited:
            continue

        
        visited.add((curr_x, curr_y))

        
        if curr_x == target or curr_y == target:
            print(f"Solution found: (Jug X: {curr_x} gallons, Jug Y: {curr_y} gallons)")
            return True

        
        
        
        q.append((x_capacity, curr_y))
        
        
        q.append((curr_x, y_capacity))
        
        
        q.append((0, curr_y))
        
        
        q.append((curr_x, 0))
        
        
        transfer = min(curr_x, y_capacity - curr_y)
        q.append((curr_x - transfer, curr_y + transfer))
        
        
        transfer = min(curr_y, x_capacity - curr_x)
        q.append((curr_x + transfer, curr_y - transfer))

    print("No solution possible.")
    return False


x_capacity = 4  
y_capacity = 3  
target = 2      

water_jug_bfs(x_capacity, y_capacity, target)