from collections import deque

class State:
    def __init__(self, m_left, c_left, m_right, c_right, boat):
        self.m_left = m_left  
        self.c_left = c_left  
        self.m_right = m_right  
        self.c_right = c_right  
        self.boat = boat  

    def is_valid(self):
        
        if (self.m_left < 0 or self.c_left < 0 or 
            self.m_right < 0 or self.c_right < 0 or 
            (self.m_left > 0 and self.c_left > self.m_left) or 
            (self.m_right > 0 and self.c_right > self.m_right)):
            return False
        return True

    def is_goal(self):
        
        return self.m_left == 0 and self.c_left == 0

    def __hash__(self):
        return hash((self.m_left, self.c_left, self.boat))

    def __eq__(self, other):
        return (self.m_left, self.c_left, self.boat) == (other.m_left, other.c_left, other.boat)

def get_next_states(state):
    next_states = []
    if state.boat == 'left':
        direction = -1
    else:
        direction = 1

    for m in range(3):  
        for c in range(3):  
            if m + c >= 1 and m + c <= 2:  
                new_state = State(
                    state.m_left + direction * m,
                    state.c_left + direction * c,
                    state.m_right - direction * m,
                    state.c_right - direction * c,
                    'right' if state.boat == 'left' else 'left'
                )
                if new_state.is_valid():
                    next_states.append(new_state)
    return next_states

def bfs():
    initial_state = State(3, 3, 0, 0, 'left')
    queue = deque([initial_state])
    visited = set()
    
    while queue:
        current_state = queue.popleft()
        
        if current_state.is_goal():
            return True
        
        visited.add(current_state)
        
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append(next_state)
    
    return False

if __name__ == "__main__":
    if bfs():
        print("Solution found!")
    else:
        print("No solution exists.")