import networkx as nx
from networkx.algorithms import isomorphism
import matplotlib.pyplot as plt
import copy


class Graph:
    degrees = []
    switched = []
    flag_switching = False

    def __init__(self):
        self.graph = nx.Graph()


def connect_graphs(equiv_graphs, index):
    for gr in equiv_graphs:
                meta_graph.add_node(gr[0])
    for i in meta_graph.nodes:
        for j in meta_graph.nodes:
            if i != j and not isomorphism.is_isomorphic(i, j):
                meta_graph.add_edge(i, j)


def edge_switching(gr):
    gr.flag_switching = True
    for x in list(gr.graph.adj.keys()):
        for y in list(gr.graph.adj[x].keys()):
            different = [h for h in gr.graph.nodes if h not in list(gr.graph.adj[x].keys()) and h != x]
            for u in different:
                neighbours_u = [g for g in gr.graph.nodes if g in list(gr.graph.adj[u].keys())]

                for v in neighbours_u:
                    copy_gr = get_copy_graph(gr)
                    copy_gr.flag_switching = False
                    copy_gr.graph.remove_edge(x, y)
                    copy_gr.graph.remove_edge(u, v)
                    copy_gr.graph.add_edge(x, u)
                    copy_gr.graph.add_edge(y, v)
                    if not isomorphism.is_isomorphic(gr.graph, copy_gr.graph):
                        gr.switched.append(copy_gr)
                        copy_gr.switched.append(gr)

    connect_graphs(gr, index)
    # return switched_graphs


def make_part_meta_graph(gr):
    switching_graphs = edge_switching(gr)
    for g in switching_graphs:
        for k in graphs:
            if not isomorphism.is_isomorphic(g, k):
                graphs += g
    for el in switching_graphs:
        make_part_meta_graph(el)


def build_meta_graph(initial_graph):
    edge_switching(initial_graph)
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


def add_edges(gr):
    for i in gr.graph.nodes:
        for k in range(i + 1, len(gr.degrees)):
            if gr.graph.degree[i] < gr.degrees[i] and gr.graph.degree[k] < gr.degrees[k]:
                gr.graph.add_edge(i, k)
    return gr


def build_graph(current_tops):
    graph = Graph()
    graph.degrees = current_tops
    for i in range(len(current_tops)):
        graph.graph.add_node(i)
    add_edges(graph)
    return graph


def main():
    global graphs # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    global meta_graphs
    meta_graphs = []
    degrees = [[4, 4, 3, 3, 2, 2, 1, 1], [7, 6, 3, 3, 2, 2, 1, 1], [4, 3, 3, 2, 2], [5, 4, 3, 3, 2, 1]]
    result_graphs_for_degrees = []
    for i in range(len(degrees)):
        answer = algorithm_Havel_Hakimi(degrees[i])
        if answer:
            gr = build_graph(degrees[i])
            result_graphs_for_degrees.append(gr)
        else:
            print(f'последовательность {degrees[i]} не графична')
    for i in range(len(result_graphs_for_degrees)):
        meta_graphs.append(Graph())
    for i in range(len(result_graphs_for_degrees)):
        build_meta_graph(result_graphs_for_degrees[i])


if __name__ == "__main__":
    main()
