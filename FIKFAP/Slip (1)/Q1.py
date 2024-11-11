
import heapq

def dijkstra(graph, start):

    queue = [(0, start)]

    distances = {vertex: float('infinity') for vertex in graph}
  
    distances[start] = 0
   
    shortest_path = {vertex: None for vertex in graph}

    while queue:
     
        current_distance, current_vertex = heapq.heappop(queue)

     
        if current_distance > distances[current_vertex]:
            continue

  
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

     
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return distances, shortest_path


graph = {
    'A': {'B': 4, 'C': 5},
    'B': {'A': 4, 'D': 9, 'C': 11},
    'C': {'A': 5, 'B': 11, 'E': 3},
    'D': {'B': 9, 'E': 13, 'F': 2},
    'E': {'C': 3, 'D': 13, 'F': 6},
    'F': {'D': 2, 'E': 6}
}


distances, shortest_path = dijkstra(graph, 'A')


print("Shortest distances from A:")
for vertex, distance in distances.items():
    print(f"Distance to {vertex}: {distance}")
