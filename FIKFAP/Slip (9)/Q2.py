def dfs_limited(graph, start, goal, depth):
    if start == goal:
        return [start]

    if depth == 0:
        return None
    
    for neighbor in graph.get(start, []):
        path = dfs_limited(graph, neighbor, goal, depth - 1)
        if path is not None:
            return [start] + path

    return None

def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching with depth limit: {depth}")
        path = dfs_limited(graph, start, goal, depth)
        if path is not None:
            return path

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': [],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': [],
    'K': []
}


start_node = 'A'
goal_node = 'G'
max_search_depth = 4

path = iddfs(graph, start_node, goal_node, max_search_depth)
if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"Goal node {goal_node} not reachable from {start_node} within depth {max_search_depth}.")