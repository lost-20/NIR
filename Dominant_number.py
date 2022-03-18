import random


def converting_graph6(str_graph):
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
    vertex = [i for i in range(len(graph))]
    edges = []
    for i in range(len(graph)):
        for j in graph[i]:
            edges.append((i, j))
    return vertex, edges


def dominant(graph):
    vertex, edges = converting_graph6(graph)

    gVertices = {i for i in vertex}

    #print('Vertices in the Graph = ', gVertices)
    gEdges = edges
    for (a, b) in gEdges:
        if (b, a) in gEdges:
            gEdges.remove((b, a))
    #print('\nEdges in the Graph = ', gEdges)
    yellow = gVertices
    startVer = random.choice(list(gVertices))
    Nbr = set()
    minDOM = set()

    S = set()
    degrees = dict()
    connectedMinSet = []

    while len(gVertices) != 0:

        def findDegrees():
            for vertex in gVertices:
                deg = 0
                for edge in gEdges:
                    if vertex in edge:
                        deg = deg + 1
                    else:
                        None
                degrees[vertex] = deg
            return degrees

        findDegrees()
        maxDegree = max(degrees.values())
        for i in degrees:
            if degrees.get(i) == maxDegree:
                S.add(i)
                maxvertex = i

        nbrmaxvertex = set()
        nbrmaxvertex.add(maxvertex)
        gVerticesNew = set()
        for edg in enumerate(gEdges):

            if edg[1][0] == maxvertex:
                nbrmaxvertex.add(edg[1][1])
            elif edg[1][1] == maxvertex:
                nbrmaxvertex.add(edg[1][0])

        connectedMinSet.append(nbrmaxvertex)
        gVerticesNew = gVertices - nbrmaxvertex
        gVertices = gVerticesNew

        for v in gEdges:
            for e in gEdges:
                if maxvertex in e:
                    gEdges.remove(e)

        degrees = dict()

    return len(connectedMinSet)