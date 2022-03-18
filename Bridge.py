from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0
        self.number = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridgeUtil(self, u, visited, parent, low, disc):

        visited[u] = True

        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    self.number += 1


            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def bridge(self):

        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)

        for i in range(self.V):
            if visited[i] == False:
                self.bridgeUtil(i, visited, parent, low, disc)
        return self.number


def convert(str_graph):
    byte = str_graph.encode('UTF-8')
    n = byte[0] - 63
    graph = {i: [] for i in range(n)}
    code_string = ""
    for i in range(1, len(byte)):
        code_string += format(byte[i] - 63, '06b')
    counter = 0
    for i in range(1, n):
        for j in range(i):
            if code_string[counter] == "1":
                graph[j].append(i)
                graph[i].append(j)
            counter += 1
    edges = []
    vertix = len(graph)
    for i in range(len(graph)):
        for j in graph[i]:
            if [j, i] not in edges:
                edges.append([i, j])
    return vertix, edges


def bridges(graph):
    v, e = convert(graph)
    g = Graph(v)
    for edge in e:
        g.addEdge(edge[0], edge[1])
    return g.bridge()
