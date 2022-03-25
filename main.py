import sys

import graph
import helpers


def main():
    args = helpers.parse_arguments().parse_args()
    local_graph = graph.Graph()
    helpers.generate_vertices(args.nodes, local_graph)
    helpers.generate_edges(args.edges, local_graph)
    try:
        path = graph.astar(local_graph, start_vertex=0, end_vertex=args.nodes - 1)
        helpers.plot_path(local_graph, path)
        print('A* Path')
        helpers.print_path(path)
        print('-'*50)

        # Modified A*
        print('Modified A* Path')
        path_modified_a_star = graph.modified_astar(local_graph, start_vertex=0, end_vertex=args.nodes - 1)
        helpers.plot_path(local_graph, path_modified_a_star)
        helpers.print_path(path_modified_a_star)
        print('-'*50)

        # Dijkstra Search
        print('Dijkstra Search')
        path_dijkstra = graph.dijkstra_search(local_graph, start_vertex=0, end_vertex=args.nodes - 1)
        helpers.plot_path(local_graph, path_dijkstra)
        helpers.print_path(path_dijkstra)

    except Exception as e:
        print('Error:', e, file=sys.stderr)
        helpers.plot_graph(local_graph)


if __name__ == '__main__':
    main()
