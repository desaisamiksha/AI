
graph = {
    1: [2, 3],
    2: [4],
    3: [2],
    4: [5, 6],
    5: [3, 7],
    6: [],
    7: [6]
}


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  
    
    visited.add(start)
    print(start, end=" ")  
    
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


start_node = 1
print("DFS traversal starting from node", start_node, ":")
dfs(graph, start_node)
