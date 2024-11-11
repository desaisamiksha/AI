def dfs_recursive(graph, vertex, visited):
    
    visited.add(vertex)
    print(vertex)  

    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs(graph):
 
    visited = set()
    
    for vertex in graph:
        if vertex not in visited:
            dfs_recursive(graph, vertex, visited)


if __name__ == "__main__":
    
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Depth-First Search (DFS) of the graph:")
    dfs(graph)