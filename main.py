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
        path_modified_a_star = graph.modified_astar(local_graph, start_vertex=0, end_vertex=args.nodes - 1)
        helpers.plot_path(local_graph, path)
        helpers.plot_path(local_graph, path_modified_a_star)
    except Exception as e:
        print('Error:', e, file=sys.stderr)
        helpers.plot_graph(local_graph)


if __name__ == '__main__':
    main()
