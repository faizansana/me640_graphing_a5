import sys

import graph
import helpers


def main():
    args = helpers.parse_arguments().parse_args()
    local_graph = graph.Graph()
    helpers.generate_vertices(args.nodes, local_graph)
    helpers.generate_edges(args.edges, local_graph)
    for edge in local_graph:
        for w in edge.get_connections():
            vid = edge.get_id()
            wid = w.get_id()
            print(f'( {vid}, {wid}, {edge.get_weight(w)}')

    for edge in local_graph:
        print(f'g.vert_dict[{edge.get_id()}]={local_graph.vert_dict[edge.get_id()]}')

    try:
        path = graph.astar(local_graph, start_vertex=1, end_vertex=args.nodes - 1)
        print(path)
    except Exception as e:
        print('Error:', e, file=sys.stderr)

    helpers.plot_graph(local_graph)


if __name__ == '__main__':
    main()
