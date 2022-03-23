from typing import Dict, Union


class Vertex:
    def __init__(self, node: Union[int, str]):
        self.id = node
        self.adjacent: Dict[Union[int, str], int] = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight: int = 0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict: Dict[Union[int, str], Vertex] = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node: Union[int, str]):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n: int):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm: Union[int, str], to: Union[int, str], cost: int = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


if __name__ == '__main__':

    graph = Graph()

    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')
    graph.add_vertex('d')
    graph.add_vertex('e')
    graph.add_vertex('f')

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
