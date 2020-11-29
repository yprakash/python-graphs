"""
@author: Prakash Yenugandula
Date   : 2020-11-27
Topological_sorting of DAG # Established precedence relationship
"""

from queue import Queue
from graph import *


def topological_sort(graph):
    queue = Queue() # holds all vertices with indegree 0, can be visited next
    indegree_map = {} # holds vertex->indegree key, val pairs

    for i in range(graph.num_vertices):
        indegree_map[i] = graph.get_indegree(i)
        # Queue all nodes which have no dependencies i.e. No edges coming in
        if indegree_map[i] == 0:
            queue.put(i)

    sorted_list = []
    while not queue.empty():
        vertex = queue.get()
        sorted_list.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            indegree_map[v] -= 1
            if indegree_map[v] == 0:
                queue.put(v)

    if len(sorted_list) != graph.num_vertices:
        print(sorted_list)
        raise ValueError("This graph with %d vertices has a cycle. len(sorted_list)= %d" % (graph.num_vertices, len(sorted_list)))

    return sorted_list


g = AdjacencyMatrixGraph(9, directed=True)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(3, 6)
g.add_edge(3, 4)
g.add_edge(6, 8)

sorted = topological_sort(g)
print(sorted)
