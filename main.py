import graph
import helpers


def main():
    args = helpers.parse_arguments().parse_args()
    local_graph = graph.Graph()
    helpers.generate_vertices(args.nodes, local_graph)
    helpers.generate_edges(args.edges, local_graph)


if __name__ == '__main__':
    main()
