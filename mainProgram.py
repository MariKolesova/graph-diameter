import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, num, tops):
        self.param = [num, tops[num], []]


def edge_switching(gr):
    list_graphs = [gr]


def algorithm_Havel_Hakimi(degrees):
    copy_degrees = []
    for el in degrees:
        copy_degrees.append(el)
    graph = nx.Graph()
    for i in range(len(degrees)):
        graph.add_node(i)
    count_tops = 0
    while True:
        copy_degrees = sorted(copy_degrees, reverse=True)
        if copy_degrees[0] == 0 and copy_degrees[len(copy_degrees) - 1] == 0:
            return graph, True
        current_vertex = copy_degrees[0]
        index_current_vertex = degrees.index(current_vertex, count_tops, len(degrees))
        count_tops += 1
        copy_degrees = copy_degrees[1:]
        if current_vertex > len(copy_degrees):
            return graph, False
        for i in range(current_vertex):
            copy_degrees[i] -= 1
            #graph.add_edge(i, index_current_vertex + i)
            if copy_degrees[i] < 0:
                return graph, False



def main():
    vertices = '4 3 3 2 2'.split(' ')
    #vertices = '5 4 3 3 2 1'.split(' ')
    #vertices = '7 6 3 3 2 2 1 1'.split(' ')
    #vertices = '4 4 3 3 2 2 1 1'.split(' ')
    for i in range(len(vertices)):
        vertices[i] = int(vertices[i])
    answer = algorithm_Havel_Hakimi(vertices)
    graph = answer[0]
    nx.draw(graph)
    plt.show()
    # build_graph(vertices)


if __name__ == "__main__":
    main()