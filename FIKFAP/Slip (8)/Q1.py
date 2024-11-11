import heapq

def best_first_search(graph, start, goal, heuristic):
    
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start))
    
    
    visited = set()
    
    
    came_from = {}
    
    while open_set:
        
        current_heuristic, current_node = heapq.heappop(open_set)

        
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path

        
        visited.add(current_node)

        
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                
                came_from[neighbor] = current_node
                
                heapq.heappush(open_set, (heuristic[neighbor], neighbor))
    
    
    return []


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}


heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 2,
    'F': 1,
    'G': 0
}

start = 'A'
goal = 'G'

path = best_first_search(graph, start, goal, heuristic)
print("Path found:", path)