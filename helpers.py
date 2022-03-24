import argparse
import random


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
