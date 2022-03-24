import argparse
import random

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
    """

    for node in range(num_of_vertices):
        while True:
            x_cor = generate_random_number()
            y_cor = generate_random_number()

            vertex = graph.Vertex(node, x_cor, y_cor)
            if local_graph.check_if_vertex_exists(vertex) is False:
                local_graph.add_vertex(node, x_loc=x_cor, y_loc=y_cor)
                break
