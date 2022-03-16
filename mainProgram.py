import networkx as nx
from networkx.algorithms import isomorphism
import matplotlib.pyplot as plt
import copy


class Graph:
    degrees = []
    switched = []

    def __init__(self):
        self.graph = nx.Graph()


def connect_graphs(equiv_graphs):
    for gr in equiv_graphs:
                meta_graph.add_node(gr[0])
    for i in meta_graph.nodes:
        for j in meta_graph.nodes:
            if i != j and not isomorphism.is_isomorphic(i, j):
                meta_graph.add_edge(i, j)


def edge_switching(gr):
    gr[1] = True
    # switched_graphs = [gr]  # хранить в поле класса
    for x in list(gr[0].adj.keys()):
        for y in list(gr[0].adj[x].keys()):
            different = [h for h in gr[0].nodes if h not in list(gr[0].adj[x].keys()) and h != x]
            for u in different:
                neighbours_u = [g for g in gr[0].nodes if g in list(gr[0].adj[u].keys())]

                for v in neighbours_u:
                    copy_gr = get_copy_graph(gr)
                    copy_gr[1] = False
                    copy_gr[0].remove_edge(x, y)
                    copy_gr[0].remove_edge(u, v)
                    copy_gr[0].add_edge(x, u)
                    copy_gr[0].add_edge(y, v)
                    if not isomorphism.is_isomorphic(gr[0], copy_gr[0]):
                        # switched_graphs.append(copy_gr)
                        gr[0].graph.append(copy_gr)

    connect_graphs(switched_graphs)
    return switched_graphs


def make_part_meta_graph(gr):
    switching_graphs = edge_switching(gr)
    for g in switching_graphs:
        for k in graphs:
            if not isomorphism.is_isomorphic(g, k):
                graphs += g
    for el in switching_graphs:
        make_part_meta_graph(el)


def build_meta_graph(initial_graph, index):
    equivalent_graphs = edge_switching(initial_graph)
    for gr in equivalent_graphs:
        if not gr[1]:
            make_part_meta_graph(gr)
    # nx.draw(graph)
    # plt.show()


def get_copy_graph(original_graph):
    res = copy.deepcopy(original_graph)
    return res


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
    for i in gr.graph.nodes:
        for k in range(i + 1, len(degree[0])):
            if gr.graph.degree[i] < degree[0][i] and gr.graph.degree[k] < degree[0][k]:
                gr.graph.add_edge(i, k)
    return gr


def build_graph(current_tops):
    # graph = nx.Graph()
    graph = Graph()
    graph.degrees = current_tops[0]
    for i in range(len(current_tops[0])):
        graph.graph.add_node(i)
    add_edges(graph, current_tops)
    return graph


def main():
    global graphs
    global meta_graphs
    meta_graphs = []
    # graphs = []  # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& убрать?
    degrees = [[4, 4, 3, 3, 2, 2, 1, 1], [7, 6, 3, 3, 2, 2, 1, 1], [4, 3, 3, 2, 2], [5, 4, 3, 3, 2, 1]]
    result_graphs_for_degrees = []
    for i in range(len(degrees)):
        answer = algorithm_Havel_Hakimi(degrees[i])
        degrees[i] = (degrees[i], answer)
        if answer:
            gr = build_graph(degrees[i])
            # [gr, bool] - граф, сделано ли переключение
            result_graphs_for_degrees.append(([gr, False], degrees[i]))
        else:
            print(f'последовательность {degrees[i][0]} не графична')
    for i in range(len(result_graphs_for_degrees)):
        meta_graphs.append(Graph)
    for i in range(len(result_graphs_for_degrees)):
    #for graph in result_graphs_for_degrees:
        # graph - (0, 1) : 0 - [a, b] - a. граф,
        #                       b. для него edge_swithing вызван ли, получены графы переключением (true/false)
        #                  1 - (c, d) - c. степенная последовательность
        #                       d. графичен ли (true/false)
        # graphs.append(graph[0])  # &&&&&&&&&&&&&&& нужен ли
        build_meta_graph(result_graphs_for_degrees[i][0], i)
        # build_meta_graph(graph[0], )


if __name__ == "__main__":
    main()
