class DisjointSetForest:
    def __init__(self, vertices):
        self.forest = [i for i in range(vertices)]

    def find_loop(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self._find(p)
        q_root = self._find(q)

        if p_root == q_root:
            return
        self.forest[p_root] = q_root

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.forest[a] < 0:
            return a

        return self.find(self.forest[a])

    def __str__(self):
        return str(self.forest)

def kruskal_am(graph):
    edges = set()
    MST = set()

    for i in range(len(graph.am)): 
        for j in range(len(graph.am[i])):
            if graph.am[i][j] != 0 and (j, i) not in edges:
                edges.add((i, j))

    sorted_edges = sorted(edges, key = lambda edge:graph.am[edge[0]][edge[1]])
    dsf = DisjointSetForest(graph.vertices)
    
    for i in sorted_edges: 
        u, v = i
        if dsf.find_loop(u, v):
            continue
        dsf.union(u, v)
        MST.add(i)

    return MST 