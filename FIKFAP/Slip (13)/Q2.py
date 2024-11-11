class Node:
    def __init__(self, name, heuristic):
        self.name = name  
        self.heuristic = heuristic  
        self.children = []  
        self.cost = float('inf')  
        self.solved = False  

    def add_child(self, child_node):
        self.children.append(child_node)

class AOStar:
    def __init__(self, root):
        self.root = root

    def search(self):
        self.root.cost = 0  
        return self.ao_star(self.root)

    def ao_star(self, node):
        if node.solved:
            return node.cost
        
        print(f"Processing Node: {node.name} with heuristic: {node.heuristic}")

        
        if not node.children:
            node.solved = True
            return node.cost
        
        total_costs = []
        
        for child in node.children:
            cost_to_child = self.ao_star(child) + child.heuristic
            
            if cost_to_child < child.cost:  
                child.cost = cost_to_child
            
            total_costs.append(child.cost)

        if all(child.solved for child in node.children):  
            node.solved = True
            node.cost = min(total_costs)  

        return node.cost

def create_graph():
    
    A = Node('A', 10)
    B = Node('B', 6)
    C = Node('C', 2)
    D = Node('D', 12)
    E = Node('E', 2)
    
    
    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    B.add_child(E)

    return A

if __name__ == "__main__":
    root_node = create_graph()  
    ao_star_search = AOStar(root_node)  
    result_cost = ao_star_search.search()  

    print(f"Minimum Cost to reach goal from Node {root_node.name}: {result_cost}")