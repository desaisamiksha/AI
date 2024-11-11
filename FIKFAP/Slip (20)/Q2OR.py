
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            return True
        return False

def kruskal(n, edges):
    
    edges.sort(key=lambda edge: edge.weight)
    ds = DisjointSet(n)

    mst_weight = 0
    mst_edges = []

    for edge in edges:
        if ds.union(edge.u, edge.v):  
            mst_weight += edge.weight
            mst_edges.append((edge.u, edge.v, edge.weight))

    return mst_weight, mst_edges


# a=0, b=1, c=2, d=3, e=4
edges = [
    Edge(1, 2, 1),    
    Edge(3, 4, 2),    
    Edge(1, 3, 3),    
    Edge(2, 3, 4),    
    Edge(0, 1, 5),    
    Edge(0, 3, 6),    
    Edge(2, 4, 6)     
]


n = 5


mst_weight, mst_edges = kruskal(n, edges)

print("Minimum Cost to Connect All Cities:", mst_weight)
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst_edges:
    print(f"{chr(u + 97)} - {chr(v + 97)}: {weight}")
