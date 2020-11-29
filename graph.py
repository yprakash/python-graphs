"""
@author: Prakash Yenugandula
Date   : 2020-11-29
The base/abstract class representation of Graph with all the interface methods
"""

import abc
import numpy as np


class Graph(abc.ABC):
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class AdjacencyMatrixGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)
        self.matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 < 0 or v2 < 0 or v1 >= self.num_vertices or v2 >= self.num_vertices:
            raise ValueError("Vertices %d or %d are out of bounds" % (v1, v2))
        if weight < 1:
            raise ValueError("An edge can't have weight < 1")

        self.matrix[v1][v2] = weight
        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Can't access vertex %d" % v)
        return [i for i in range(self.num_vertices) if self.matrix[v][i] > 0]

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Can't access vertex %d" % v)
        return len([1 for i in range(self.num_vertices) if self.matrix[i][v] > 0])

    def get_edge_weight(self, v1, v2):
        if v1 < 0 or v2 < 0 or v1 >= self.num_vertices or v2 >= self.num_vertices:
            raise ValueError("Vertices %d or %d are out of bounds" % (v1, v2))
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertex_id == v:
            raise ValueError("The vertex %d can not be adjacent to itself" % v)
        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)


class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)

        self.vertex_list = []
        for i in range(num_vertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 < 0 or v2 < 0 or v1 >= self.num_vertices or v2 >= self.num_vertices:
            raise ValueError("Vertices %d or %d are out of bounds" % (v1, v2))
        if weight != 1:
            raise ValueError("An Adjacency Set can NOT represent an edge with weight != 1. It can only be unweighted graph.")

        self.vertex_list[v1].add_edge(v2)
        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Can't access vertex %d" % v)
        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Can't access vertex %d" % v)

        indegree = 0
        for i in range(self.num_vertices):
            if v in self.get_adjacent_vertices(i):
                indegree = indegree + 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return 1 # Adjacency Set can NOT represent an edge with weight != 1

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)
