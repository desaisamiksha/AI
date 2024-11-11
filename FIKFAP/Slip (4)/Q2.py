class Graph:
    def __init__(self):
        self.nodes = {}  
        self.heuristic_cost = {}  
        self.solutions = {}  

    def add_node(self, node, successors, costs):
        self.nodes[node] = successors
        self.heuristic_cost[node] = costs

    def get_successors(self, node):
        return self.nodes.get(node, [])

    def get_heuristic_cost(self, node):
        return self.heuristic_cost.get(node, [])

    def ao_star(self, node, path):
        print(f'Processing Node: {node}')
        if node in self.solutions:
            return self.solutions[node]

        if node in path:  
            print(f"Cycle detected at node: {node}")
            return (None, float('inf'))

        successors = self.get_successors(node)
        if not successors:  
            self.solutions[node] = ([], self.get_heuristic_cost(node)[0])
            return self.solutions[node]

        min_cost = float('inf')
        best_solution = None
        path.append(node)  

        for successor_nodes, cost in zip(successors, self.get_heuristic_cost(node)):
            solution_cost = sum(self.ao_star(s, path[:])[1] for s in successor_nodes)
            total_cost = solution_cost + cost

            if total_cost < min_cost:
                min_cost = total_cost
                best_solution = successor_nodes

        path.pop()  
        self.solutions[node] = (best_solution, min_cost)
        return self.solutions[node]

    def print_solution(self, start_node):
        solution_nodes, solution_cost = self.ao_star(start_node, [])
        print(f"Optimal Solution Path from node {start_node}: {solution_nodes} with Total Cost: {solution_cost}")



g = Graph()
g.add_node('A', [['B', 'C'], ['D']], [1, 3])
g.add_node('B', [['E'], ['F']], [1, 1])
g.add_node('C', [['G']], [2])
g.add_node('D', [], [0])  
g.add_node('E', [], [0])
g.add_node('F', [], [0])
g.add_node('G', [], [0])

g.print_solution('A')