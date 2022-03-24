"""
Inspired from https://www.bogotobogo.com/python/python_graph_data_structures.php
"""
from __future__ import annotations

import math
import queue
from typing import Dict, List, Tuple, Union


def calculate_euclidean_distance(first_vertex: Vertex, second_vertex: Vertex):
    x1, y1 = first_vertex.x_loc, first_vertex.y_loc
    x2, y2 = second_vertex.x_loc, second_vertex.y_loc
    distance = math.dist([x1, y1], [x2, y2])
    return int(distance)


class Vertex:
    def __init__(self, node: int, x_loc: int, y_loc: int):
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

    def add_vertex(self, node: int, x_loc: int, y_loc: int):
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
        return self.vert_dict.values()

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

        vertex = self.vert_dict[second_node]

        for vertices in vertex.adjacent.keys():
            if first_node == vertices.get_id():
                return True

        return False


def construct_path(came_from: Dict[Vertex, Vertex], current: Vertex) -> List[Vertex]:
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path


def astar(local_graph: Graph, start_vertex: int, end_vertex: int):
    open_queue: queue.PriorityQueue[Tuple[int, Vertex]] = queue.PriorityQueue()
    open_queue.put((0, local_graph.get_vertex(start_vertex)))

    came_from: Dict[Vertex, Union[Vertex, None]] = {}
    cost_so_far: Dict[Vertex, int] = {}

    cost_so_far[local_graph.get_vertex(start_vertex)] = 0

    while not open_queue.empty():
        current = open_queue.get()[1]

        if current.id == end_vertex:
            return construct_path(came_from, current)

        for adj_vertex in current.get_connections():
            new_cost = cost_so_far[current] + current.get_weight(adj_vertex)
            if adj_vertex not in cost_so_far or new_cost < cost_so_far[adj_vertex]:
                cost_so_far[adj_vertex] = new_cost
                priority = new_cost + calculate_euclidean_distance(adj_vertex, local_graph.get_vertex(end_vertex))
                open_queue.put((priority, adj_vertex))
                came_from[adj_vertex] = current

    raise Exception('No path found')


if __name__ == '__main__':

    graph = Graph()

    graph.add_vertex(0, 3, 1)
    graph.add_vertex(1, 4, 1)
    graph.add_vertex(2, 5, 6)
    graph.add_vertex(3, 5, 1)
    graph.add_vertex(4, 2, 2)
    graph.add_vertex(5, 4, 5)

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
