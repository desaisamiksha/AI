
graph = {
    1: [2, 4],
    2: [3],
    3: [4, 5, 6],
    4: [2],
    5: [7, 8],
    6: [8],
    7: [8],
    8: []
}


def find_all_paths(graph, start, goal, path=[]):
    path = path + [start]  
    
    if start == goal:
        return [path]  
    
    if start not in graph:
        return []  
    
    paths = []  
    for neighbor in graph[start]:
        if neighbor not in path:  
            new_paths = find_all_paths(graph, neighbor, goal, path)
            for new_path in new_paths:
                paths.append(new_path)
    
    return paths


start_node = 1
goal_node = 8
all_paths = find_all_paths(graph, start_node, goal_node)


print(f"All paths from node {start_node} to node {goal_node}:")
for path in all_paths:
    print(" → ".join(map(str, path)))
