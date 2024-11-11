from collections import deque

class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1  
        self.jug2 = jug2  

    def __hash__(self):
        return hash((self.jug1, self.jug2))

    def __eq__(self, other):
        return (self.jug1, self.jug2) == (other.jug1, other.jug2)

def bfs(capacity1, capacity2, target):
    initial_state = State(0, 0)
    queue = deque([initial_state])
    visited = set()
    
    while queue:
        current_state = queue.popleft()

        
        if current_state.jug1 == target or current_state.jug2 == target:
            return True

        
        visited.add(current_state)

        
        possible_states = [
            State(capacity1, current_state.jug2),  
            State(current_state.jug1, capacity2),  
            State(0, current_state.jug2),          
            State(current_state.jug1, 0),          
            State(max(0, current_state.jug1 - (capacity2 - current_state.jug2)),
                  min(capacity2, current_state.jug2 + current_state.jug1)),  
            State(min(capacity1, current_state.jug1 + current_state.jug2),
                  max(0, current_state.jug2 - (capacity1 - current_state.jug1)))   
        ]

        for state in possible_states:
            if state not in visited:
                queue.append(state)

    return False

if __name__ == "__main__":
    capacity_jug1 = 4  
    capacity_jug2 = 3  
    target_amount = 2  

    if bfs(capacity_jug1, capacity_jug2, target_amount):
        print(f"Target amount {target_amount} can be measured.")
    else:
        print(f"Target amount {target_amount} cannot be measured.")