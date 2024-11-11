
class MonkeyBananaProblem:
    def __init__(self):
        
        self.state = ('floor', 'corner', False)
    
    def is_goal(self, state):
        
        return state[2]
    
    def get_successors(self, state):
        successors = []
        monkey, box, has_banana = state
        
        if monkey == 'floor' and box == 'corner':
            
            successors.append(('floor', 'middle', False))
        
        if monkey == 'floor' and box == 'middle':
            
            successors.append(('on_box', 'middle', False))
        
        if monkey == 'on_box' and box == 'middle':
            
            successors.append(('on_box', 'middle', True))
        
        return successors
    
    def solve(self):
        
        stack = [self.state]
        visited = set()
        
        while stack:
            current_state = stack.pop()
            
            if self.is_goal(current_state):
                return current_state
            
            if current_state not in visited:
                visited.add(current_state)
                successors = self.get_successors(current_state)
                stack.extend(successors)
        
        return None


problem = MonkeyBananaProblem()
solution = problem.solve()


if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")
