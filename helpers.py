import argparse
import math
import random

import matplotlib.pyplot as plt

import graph


def parse_arguments():
    parser = argparse.ArgumentParser(prog='A* algorithm', description='Calculates the A* algorithm')
    parser.add_argument('--nodes', '-n', type=int, help='Number of nodes of the graph', default=6)
    parser.add_argument('--edges', '-e', type=int, help='Number of edges of the graph', default=3)
    return parser


def generate_random_number(min: int = 0, max: int = 100):
    """Generates random number between specified minimum and maximum

    Args:
        min (int, optional): Minimum number. Defaults to 0.
        max (int, optional): Maximum value. Defaults to 100.
    """
    random.seed()
    return random.randint(min, max)


def generate_vertices(num_of_vertices: int, local_graph: graph.Graph):
    """Generates specified number of vertices

    Args:
        num_of_vertices (int): Number of vertices
        local_graph (graph.Graph): Graph object instance
    """

    for node in range(num_of_vertices):
        while True:
            x_cor = generate_random_number()
            y_cor = generate_random_number()

            vertex = graph.Vertex(node, x_cor, y_cor)
            if local_graph.check_if_vertex_exists(vertex) is False:
                local_graph.add_vertex(node, x_loc=x_cor, y_loc=y_cor)
                break


def generate_edges(num_of_edges: int, local_graph: graph.Graph):
    """Generates specified number of edges

    Args:
        num_of_edges (int): Number of edges
        local_graph (graph.Graph): Graph object instance
    """
    num_of_vertices = local_graph.get_num_of_vertices()

    for _ in range(num_of_edges):
        while True:
            first_vertex = generate_random_number(max=num_of_vertices-1)
            second_vertex = generate_random_number(max=num_of_vertices-1)
            # Prevent loops
            if first_vertex == second_vertex:
                continue
            if local_graph.check_if_edge_exists(first_vertex, second_vertex) is False:
                # Calculate euclidean distance between vertices and add to graph db
                distance = calculate_euclidean_distance(local_graph.get_vertex(first_vertex), local_graph.get_vertex(second_vertex))
                local_graph.add_edge(first_vertex, second_vertex, cost=distance)
                break


def calculate_euclidean_distance(first_vertex: graph.Vertex, second_vertex: graph.Vertex):
    x1, y1 = first_vertex.x_loc, first_vertex.y_loc
    x2, y2 = second_vertex.x_loc, second_vertex.y_loc
    distance = math.dist([x1, y1], [x2, y2])
    return int(distance)


def plot_graph(local_graph: graph.Graph):

    # Plot nodes
    for vertex in local_graph.get_vertices():
        x_cor, y_cor = vertex.x_loc, vertex.y_loc
        plt.plot(x_cor, y_cor, 'ro')

        # Plot edges
        adj_vertices = vertex.get_connections()
        for adj_vertex in adj_vertices:
            plt.plot([x_cor, adj_vertex.x_loc], [y_cor, adj_vertex.y_loc])

    plt.axes([0, 100, 0, 100])
    plt.show()
