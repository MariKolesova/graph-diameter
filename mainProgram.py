import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    degrees = []

    def __init__(self, num, tops):
        self.param = [num, tops[num], []]


def edge_switching(gr):
    list_graphs = [gr[0]]
    v = gr[0][0]
    c = gr
    l = list(gr[0][0].adj.keys())
    for top in list(gr[0].adj.keys()):
        neighbours_current_vertex = list(gr[0][0].adj[top].keys())
        difference_with_current_neighbour = [h for h in gr[0][0].nodes if h not in neighbours_current_vertex]
        del difference_with_current_neighbour[0]
        for neighbour in neighbours_current_vertex:
            gr[0].remove_edge(top, neighbour)
            for el in difference_with_current_neighbour:
                neighbours = [p for p in gr[0][0].nodes if p in difference_with_current_neighbour]
                neighbours.pop(0)
                gr[0][0].add_edge(top, el)
                for vertex in neighbours:
                    gr[0][0].add_edge(neighbour, vertex)
                    gr[0][0].remove_edge(vertex, el)
                    a = 8


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
    for i in gr.nodes:
        for k in range(i + 1, len(degree[0])):
            if gr.degree[i] < degree[0][i] and gr.degree[k] < degree[0][k]:
                gr.add_edge(i, k)
    return gr


def build_graph(current_tops):
    graph = nx.Graph()
    graph.degrees = current_tops[0]
    for i in range(len(current_tops[0])):
        graph.add_node(i)
    add_edges(graph, current_tops)
    return graph


def main():
    global graphs
    graphs = []
    degrees = [[4, 4, 3, 3, 2, 2, 1, 1], [4, 3, 3, 2, 2], [5, 4, 3, 3, 2, 1], [7, 6, 3, 3, 2, 2, 1, 1]]
    result_graphs_for_degrees = []
    for i in range(len(degrees)):
        answer = algorithm_Havel_Hakimi(degrees[i])
        degrees[i] = (degrees[i], answer)
        if answer:
            gr = build_graph(degrees[i])
            result_graphs_for_degrees.append((gr, degrees[i]))
        else:
            print(f'последовательность {degrees[i][0]} не графична')
    for graph in result_graphs_for_degrees:
        graphs.append(graph[0])
        edge_switching(graphs[0])
        #edge_switching(graph)
        # nx.draw(graph)
        # plt.show()


if __name__ == "__main__":
    main()
