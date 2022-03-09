import networkx as nx
from networkx.algorithms import isomorphism
import matplotlib.pyplot as plt
import copy


class Graph:
    degrees = []

    def __init__(self, num, tops):
        self.param = [num, tops[num], []]


def connect_graphs(equiv_graphs):
    mg = meta_graph  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for gr in equiv_graphs:
        if gr not in meta_graph.adj.keys():
            meta_graph.add_node(gr)
    all_nodes = list(meta_graph.adj.keys())
    while len(all_nodes) != 0:
        current_top = all_nodes.pop(0)
        for vertex in meta_graph.nodes:
            if vertex != current_top:
                meta_graph.add_node(current_top, vertex)


def edge_switching(gr):
    mg = meta_graph  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    switched_graphs = [gr]
    for x in list(gr.adj.keys()):
        for y in list(gr.adj[x].keys()):
            different = [h for h in gr.nodes if h not in list(gr.adj[x].keys()) and h != x]
            for u in different:
                neighbours_u = [g for g in gr.nodes if g in list(gr.adj[u].keys())]

                for v in neighbours_u:
                    copy_gr = get_copy_graph(gr)
                    copy_gr.remove_edge(x, y)
                    copy_gr.remove_edge(u, v)
                    copy_gr.add_edge(x, u)
                    copy_gr.add_edge(y, v)
                    not_isom_graph = []
                    for el in switched_graphs:
                        if not isomorphism.is_isomorphic(copy_gr, el):
                            not_isom_graph.append(el)
                    switched_graphs += not_isom_graph

    connect_graphs(switched_graphs)
    return switched_graphs


def build_meta_graph(initial_graph):
    mg = meta_graph  # !!!!!!!!!!!!!!!!!!!!!!!!!111111111

    meta_graph.add_node(initial_graph)
    equivalent_graphs = edge_switching(initial_graph)
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
    global meta_graph
    meta_graph = nx.Graph()
    graphs = []
    degrees = [[4, 4, 3, 3, 2, 2, 1, 1], [7, 6, 3, 3, 2, 2, 1, 1], [4, 3, 3, 2, 2], [5, 4, 3, 3, 2, 1]]
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
        build_meta_graph(graph[0])


if __name__ == "__main__":
    main()
