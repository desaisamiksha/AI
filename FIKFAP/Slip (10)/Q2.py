import heapq


class Node:
    def __init__(self, position, parent, g=0, h=0, f=0):
        self.position = position
        self.parent = parent
        self.g = g  
        self.h = h  
        self.f = f  

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    """Heuristic function for A* (Manhattan distance)"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    """Implementation of the A* algorithm"""
    open_list = []
    closed_list = set()

    start_node = Node(start, None)
    goal_node = Node(end, None)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  

        
        (x, y) = current_node.position
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for next in neighbors:
            
            if (0 <= next[0] < len(grid)) and (0 <= next[1] < len(grid[0])):
                if grid[next[0]][next[1]] == 1:  
                    continue

                
                if next in closed_list:
                    continue

                
                g = current_node.g + 1
                h = heuristic(next, goal_node.position)
                f = g + h
                neighbor = Node(next, current_node, g, h, f)

                
                if any(open_node.position == neighbor.position and open_node.g <= neighbor.g for open_node in open_list):
                    continue

                heapq.heappush(open_list, neighbor)

    return None  


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    path = astar(grid, start, end)
    if path:
        print("Path found:", path)
    else:
        print("No path found")