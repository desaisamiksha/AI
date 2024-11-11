from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    
    visited = set()
    
    queue = deque()

    
    initial_state = (0, 0)  
    queue.append(initial_state)
    visited.add(initial_state)

    
    while queue:
        amount_in_jug1, amount_in_jug2 = queue.popleft()

        print(f"Exploring state: ({amount_in_jug1}, {amount_in_jug2})")

        
        if amount_in_jug1 == target or amount_in_jug2 == target:
            return True

        
        next_states = set()

        
        next_states.add((jug1_capacity, amount_in_jug2))

        
        next_states.add((amount_in_jug1, jug2_capacity))

        
        next_states.add((0, amount_in_jug2))

        
        next_states.add((amount_in_jug1, 0))

        
        transfer = min(amount_in_jug1, jug2_capacity - amount_in_jug2)
        next_states.add((amount_in_jug1 - transfer, amount_in_jug2 + transfer))

        
        transfer = min(amount_in_jug2, jug1_capacity - amount_in_jug1)
        next_states.add((amount_in_jug1 + transfer, amount_in_jug2 - transfer))

        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    
    return False


jug1_capacity = 4
jug2_capacity = 3
target = 2

if water_jug_bfs(jug1_capacity, jug2_capacity, target):
    print("Solution found!")
else:
    print("Solution not possible.")