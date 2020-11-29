"""
@author: Prakash Yenugandula
Date   : 2020-11-29
Class to test Graph's functionalities
"""

from graph import *


def test_graph(g):
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)

    for i in range(n):
        print("Adjacent to ", i, g.get_adjacent_vertices(i))

    for i in range(n):
        print("Indegree ", i, g.get_indegree(i))

    for i in range(n):
        for j in g.get_adjacent_vertices(i):
            print("Edge weight ", i, " ", j, g.get_edge_weight(i, j))

    g.display()


n = 4
g = AdjacencyMatrixGraph(n, directed=True)
test_graph(g)
g = AdjacencySetGraph(n, directed=True)
test_graph(g)
