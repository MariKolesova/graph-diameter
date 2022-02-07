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
    # graph.add_edge(1, 2)
    # print(graph.nodes())
    # print(graph.edges())
    # nx.draw(graph)
    # plt.show()
    add_count_edges(graph, degrees)
    g = 9
   # add_edges(degrees, graph)


def add_count_edges(gr, deg):
    for i in gr.nodes:
        for k in range(i + 1, len(deg)):
            if gr.degree[i] < deg[i]:
                gr.add_edge(i, k)

# def add_edges(degrees, gr):
#     for node in gr.nodes:
#         count = degrees[node]
#         del node
#         for i in count:
#             gr.add_edge()



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
    global vertices
    with open('data.txt', 'r') as file:
        vertices = file.read().split(' ')
        for i in range(len(vertices)):
            vertices[i] = int(vertices[i])
    algorithm_Havel_Hakimi(vertices)
    build_graph(vertices)


if __name__ == "__main__":
    main()
