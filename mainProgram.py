import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, num, tops):
        self.param = [num, tops[num], []]


def edge_switching(gr):
    list_graphs = [gr]


def algorithm_Havel_Hakimi(degrees):
    graph = nx.Graph()
    for i in range(len(degrees)):
        graph.add_node(i)
    while True:
        degrees = sorted(degrees, reverse=True)
        if degrees[0] == 0 and degrees[len(degrees) - 1] == 0:
            return graph
        v = degrees[0]
        degrees = degrees[1:]
        if v > len(degrees):
            return graph
        for i in range(v):
            degrees[i] -= 1
            if degrees[i] < 0:
                return graph



def main():
    vertices = '4 3 3 2 2'.split(' ')
    #vertices = '5 4 3 3 2 1'.split(' ')
    #vertices = '7 6 3 3 2 2 1 1'.split(' ')
    #vertices = '4 4 3 3 2 2 1 1'.split(' ')
    for i in range(len(vertices)):
        vertices[i] = int(vertices[i])
    graph = algorithm_Havel_Hakimi(vertices)
    nx.draw(graph)
    plt.show()
    # build_graph(vertices)


if __name__ == "__main__":
    main()