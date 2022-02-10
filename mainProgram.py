import itertools
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, num, tops):
        self.param = [num, tops[num], []]


def build_graph(degrees):
    graph = nx.Graph()
    for i in range(len(degrees)):
        graph.add_node(i)
    add_edges(graph, degrees)
    nx.draw(graph)
    plt.show()
    # edge_switching(graph)


def edge_switching(gr):
    list_graphs = [gr]


def add_edges(gr, deg):
    count_edges = sum(deg) // 2
    count = 0
    comp = 1
    for i in gr.nodes:
        for k in range(i + 1, len(deg)):
            if gr.degree[i] < deg[i] and gr.degree[k] < deg[k]:
                gr.add_edge(i, k)
                count += 1



def algorithm_Havel_Hakimi(degrees):
    tops = [degree for degree in degrees]
    while True:
        current_degree = tops[0]
        del tops[0]
        for i in range(current_degree):
            tops[i] -= 1
            if tops[i] < 0:
                print('последовательность не графическая')
                return
        tops.sort()
        tops.reverse()
        if all(tops[i] == 0 for i in tops):
            print("последовательность графическая")
            break


def main():
    with open('data.txt', 'r') as file:
        vertices = file.read().split(' ')
        for i in range(len(vertices)):
            vertices[i] = int(vertices[i])
    algorithm_Havel_Hakimi(vertices)
    build_graph(vertices)


if __name__ == "__main__":
    main()
