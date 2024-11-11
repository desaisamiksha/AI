class Node:
    def __init__(self, name):
        self.name = name
        self.children = []  
        self.cost = float('inf')  
        self.is_goal = False  

    def add_child(self, child_node):
        self.children.append(child_node)


class AOStar:
    def __init__(self):
        self.open_list = []  
        self.closed_list = []  

    def search(self, start_node):
        self.open_list.append(start_node)

        while self.open_list:
            current_node = self.get_best_node()

            if current_node.is_goal:
                return self.reconstruct_path(current_node)

            self.open_list.remove(current_node)
            self.closed_list.append(current_node)

            for child in current_node.children:
                if child not in self.closed_list:
                    cost = current_node.cost + 1  
                    if cost < child.cost:
                        child.cost = cost
                        child.parent = current_node
                        if child not in self.open_list:
                            self.open_list.append(child)

        return None  

    def get_best_node(self):
        
        return min(self.open_list, key=lambda node: node.cost)

    def reconstruct_path(self, node):
        path = []
        while node:
            path.append(node.name)
            node = getattr(node, 'parent', None)  
        return path[::-1]  


if __name__ == "__main__":
    
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    
    
    E.is_goal = True

    
    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    C.add_child(E)

    
    ao_star = AOStar()
    
    
    A.cost = 0
    
    
    result_path = ao_star.search(A)

    if result_path:
        print("Path found:", " -> ".join(result_path))
    else:
        print("No path found.")