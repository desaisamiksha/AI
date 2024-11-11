import heapq



graph = {
    1: [(28, 2), (10, 6)],
    2: [(28, 1), (16, 3), (14, 7)],
    3: [(16, 2), (12, 4)],
    4: [(12, 3), (18, 7), (22, 5)],
    5: [(22, 4), (25, 6), (24, 7)],
    6: [(10, 1), (25, 5)],
    7: [(14, 2), (18, 4), (24, 5)]
}

def prim(graph, start):
    visited = set()             
    min_cost = 0                
    min_heap = [(0, start)]     

    while min_heap and len(visited) < len(graph):
        cost, node = heapq.heappop(min_heap)
        
        if node in visited:
            continue
        
        min_cost += cost        
        visited.add(node)       
        
        
        for edge_cost, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_cost, neighbor))
                
    return min_cost


minimum_cost = prim(graph, 1)
print("The minimum cost to connect all cities is:", minimum_cost)
