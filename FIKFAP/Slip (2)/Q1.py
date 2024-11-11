



graph = {
    1: [2, 3,4],
    2: [1, 5,4],
    3: [1, 4],
    4: [2,3,7],
    5: [2, 6, 7],
    6: [5,7],
    7: [4,5,6]
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  

    
    visited.add(start)
    print(start, end=' ')

    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


print("Depth First Search starting from vertex 1:")
dfs(graph, 1)
