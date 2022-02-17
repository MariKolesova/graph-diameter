import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, num, tops):
        self.param = [num, tops[num], []]


def edge_switching(gr):
    list_graphs = [gr]


def algorithm_Havel_Hakimi(degrees):
    while True:
        degrees = sorted(degrees, reverse=True)
        if degrees[0] == 0 and degrees[len(degrees) - 1] == 0:
            return True
        current_vertex = degrees[0]
        degrees = degrees[1:]
        if current_vertex > len(degrees):
            return False
        for i in range(current_vertex):
            degrees[i] -= 1
            if degrees[i] < 0:
                return False


def add_edges(gr, degree):
    count = 0
    for i in gr.nodes:
        for k in range(i + 1, len(degree)):
            if gr.degree[i] < degree[i] and gr.degree[k] < degree[k]:
                gr.add_edge(i, k)
                count += 1
    return gr


def build_graph(tops):
    graph = nx.Graph()
    for i in range(len(tops)):
        graph.add_node(i)
    graphs.append(add_edges(graph, tops))
    for gr in graphs:
        nx.draw(gr)
        plt.show()


def main():
    global graphs
    graphs = []
    vertices = '4 3 3 2 2'.split(' ')
    #vertices = '5 4 3 3 2 1'.split(' ')
    #vertices = '7 6 3 3 2 2 1 1'.split(' ')
    
    for i in range(len(vertices)):
        vertices[i] = int(vertices[i])
    answer = algorithm_Havel_Hakimi(vertices)
    if answer:
        build_graph(vertices)
    else:
        print('не графичен')
   # nx.draw(graph)
    #plt.show()


if __name__ == "__main__":
    main()