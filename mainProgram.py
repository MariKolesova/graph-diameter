import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, num, tops):
        self.param = [num, tops[num], []]


def edge_switching(gr):
    list_graphs = [gr]


def algorithm_Havel_Hakimi(degrees):
    graph = nx.Graph()
    vertex_degrees = []
    for i in range(len(degrees)):
        graph.add_node(i)
        vertex_degrees.append(degrees[i])
    for i in graph.nodes:
        for k in range(i + 1, len(degrees)):
            if vertex_degrees[i] == 0:
                continue
            vertex_degrees[i] -= 1
            vertex_degrees[k] -= 1
            if vertex_degrees[i] < 0 or vertex_degrees[k] < 0:
                vertex_degrees[i] += 1
                vertex_degrees[k] += 1
                continue
            graph.add_edge(i, k)
    print('последовательность графическая')
    nx.draw(graph)
    plt.show()


def main():
    vertices = '4 3 3 2 2'.split(' ')
    #vertices = '5 4 3 3 2 1'.split(' ')
    #vertices = '7 6 3 3 2 2 1 1'.split(' ')
    #vertices = '4 4 3 3 2 2 1 1'.split(' ')
    for i in range(len(vertices)):
        vertices[i] = int(vertices[i])
    algorithm_Havel_Hakimi(vertices)
    # build_graph(vertices)


if __name__ == "__main__":
    main()