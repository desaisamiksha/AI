import heapq

class Node:
    def __init__(self, name, heuristic=0):
        self.name = name  
        self.heuristic = heuristic  
        self.g = float('inf')  
        self.f = float('inf')  
        self.parent = None  

    def __lt__(self, other):
        return self.f < other.f  

class AStar:
    def __init__(self):
        self.graph = {}  

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  

    def heuristic(self, node_name):
        
        heuristics = {
            'A': 6,
            'B': 4,
            'C': 2,
            'D': 1,
            'E': 0,
            'F': 3
        }
        return heuristics.get(node_name, float('inf'))

    def a_star_search(self, start, goal):
        open_list = []
        closed_set = set()

        start_node = Node(start, self.heuristic(start))
        start_node.g = 0
        start_node.f = start_node.heuristic
        heapq.heappush(open_list, start_node)

        while open_list:
            current_node = heapq.heappop(open_list)

            if current_node.name == goal:
                return self.reconstruct_path(current_node)

            closed_set.add(current_node.name)

            for neighbor_name, weight in self.graph.get(current_node.name, []):
                if neighbor_name in closed_set:
                    continue

                tentative_g_score = current_node.g + weight

                neighbor_node = Node(neighbor_name, self.heuristic(neighbor_name))
                if tentative_g_score < neighbor_node.g:
                    neighbor_node.parent = current_node
                    neighbor_node.g = tentative_g_score
                    neighbor_node.f = neighbor_node.g + neighbor_node.heuristic

                    if neighbor_node not in open_list:
                        heapq.heappush(open_list, neighbor_node)

        return None  

    def reconstruct_path(self, node):
        path = []
        while node:
            path.append(node.name)
            node = node.parent
        return path[::-1]  

if __name__ == "__main__":
    astar = AStar()
    astar.add_edge('A', 'B', 1)
    astar.add_edge('A', 'C', 4)
    astar.add_edge('B', 'D', 3)
    astar.add_edge('B', 'E', 5)
    astar.add_edge('C', 'F', 2)
    astar.add_edge('D', 'F', 1)
    astar.add_edge('D', 'E', 1)
    astar.add_edge('E', 'F', 2)

    start_node = 'A'
    goal_node = 'E'
    
    path = astar.a_star_search(start_node, goal_node)

    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found.")



        