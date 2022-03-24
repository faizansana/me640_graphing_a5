"""
Inspired from https://www.bogotobogo.com/python/python_graph_data_structures.php
"""
from __future__ import annotations
from typing import Dict, Union


class Vertex:
    def __init__(self, node: Union[int, str], x_loc: int, y_loc: int):
        self.id = node
        self.adjacent: Dict[Vertex, int] = {}
        self.x_loc = x_loc
        self.y_loc = y_loc

    def __str__(self):
        return str(self.id) + f' x_cor: {self.x_loc}, y_cor: {self.y_loc}' + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor: Vertex, weight: int = 0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor: Vertex):
        return self.adjacent[neighbor]

    def __eq__(self, other) -> bool:
        if self.x_loc == other.x_loc and self.y_loc == other.y_loc or self.id == other.id:
            return True
        else:
            return False
    
    def __hash__(self) -> int:
        return hash(self.id)


class Graph:
    def __init__(self):
        self.vert_dict: Dict[Union[int, str], Vertex] = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node: Union[int, str], x_loc: int, y_loc: int):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node, x_loc, y_loc)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n: int):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            raise Exception('Vertex does not exist')

    def add_edge(self, frm: Union[int, str], to: Union[int, str], cost: int = 0):
        if frm not in self.vert_dict or to not in self.vert_dict:
            raise Exception('Adding edge for vertex that does not exist!')

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def check_if_vertex_exists(self, vertex: Vertex):
        """Checks if two vertices have the same x and y coordinates

        Args:
            vertex (Vertex): Instance of vertex class

        Returns:
            bool: returns True if vertex overlaps another. Else returns False.
        """
        if vertex in self.vert_dict.values():
            return True
        else:
            return False

    def get_num_of_vertices(self):
        return len(self.vert_dict)

    def check_if_edge_exists(self, first_node: Union[int, str], second_node: Union[int, str]):
        vertex = self.vert_dict[first_node]

        for vertices in vertex.adjacent.keys():
            if second_node == vertices.get_id():
                return True

        return False


if __name__ == '__main__':

    graph = Graph()

    graph.add_vertex('a', 3, 1)
    graph.add_vertex('b', 4, 1)
    graph.add_vertex('c', 5, 6)
    graph.add_vertex('d', 5, 1)
    graph.add_vertex('e', 2, 2)
    graph.add_vertex('f', 4, 5)

    graph.add_edge('a', 'b', 7)
    graph.add_edge('a', 'c', 9)
    graph.add_edge('a', 'f', 14)
    graph.add_edge('b', 'c', 10)
    graph.add_edge('b', 'd', 15)
    graph.add_edge('c', 'd', 11)
    graph.add_edge('c', 'f', 2)
    graph.add_edge('d', 'e', 6)
    graph.add_edge('e', 'f', 9)

    for edge in graph:
        for w in edge.get_connections():
            vid = edge.get_id()
            wid = w.get_id()
            print(f'( {vid}, {wid}, {edge.get_weight(w)}')

    for edge in graph:
        print(f'g.vert_dict[{edge.get_id()}]={graph.vert_dict[edge.get_id()]}')
