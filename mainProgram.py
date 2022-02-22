import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, num, tops):
        self.param = [num, tops[num], []]


def edge_switching(gr):
    list_graphs = [gr[0]]
    for top in list(gr[0].adj.keys()):
        neighbours_current_vertex = list(gr[0].adj[top].keys())
        difference = [h for h in gr[0].nodes if h not in neighbours_current_vertex]
        difference.remove(top)
        gr[0].remove_edge(top, neighbours_current_vertex[0])
        gr[0].remove_edge(difference[0], list(gr[0].adj[difference[0]].keys())[0])
        gr[0].add_edge(top, difference[0])
        difference.pop(0)
        gr[0].add_edge(neighbours_current_vertex[0], difference[0])
        a = 0

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
    for i in range(len(current_tops[0])):
        graph.add_node(i)
    add_edges(graph, current_tops)
    return graph


def main():
    degrees = [[4, 4, 3, 3, 2, 2, 1, 1], [4, 3, 3, 2, 2], [5, 4, 3, 3, 2, 1], [7, 6, 3, 3, 2, 2, 1, 1]]
    result_graphs = []
    for i in range(len(degrees)):
        answer = algorithm_Havel_Hakimi(degrees[i])
        degrees[i] = (degrees[i], answer)
        if answer:
            gr = build_graph(degrees[i])
            result_graphs.append((gr, degrees[i]))
        else:
            print(f'последовательность {degrees[i]} не графична')
    for graph in result_graphs:
        edge_switching(graph)
        # nx.draw(graph)
        # plt.show()


if __name__ == "__main__":
    main()
