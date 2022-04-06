import networkx as nx
from networkx.algorithms import isomorphism
import matplotlib.pyplot as plt
import copy


class Graph:
    degrees = []
    flag_switching = False
    switched = []

    def __init__(self):
        self.graph = nx.Graph()


def connect_graphs(equiv_graphs, index_meta_g):
    ghs = graphs
    mg = meta_graphs
    for gr in equiv_graphs.switched:
        meta_graphs[index_meta_g].graph.add_node(gr)
    a = list(meta_graphs[index_meta_g].graph.nodes)
    for i in meta_graphs[index_meta_g].graph.nodes:
        for j in meta_graphs[index_meta_g].graph.nodes:
            if i != j and not isomorphism.is_isomorphic(i.graph, j.graph):
                meta_graphs[index_meta_g].graph.add_edge(i, j)


def edge_switching(gr, index_meta_graph):  # (граф, номер мета)
    ghs = graphs
    mg = meta_graphs
    if not gr.flag_switching:
        gr.flag_switching = True
        gr.add_node(gr)
        # meta_graphs[index_meta_graph].flag_switching = True
    else:
        return
    for x in list(gr.graph.adj.keys()):
        for y in list(gr.graph.adj[x].keys()):
            different = [h for h in gr.graph.nodes if h not in list(gr.graph.adj[x].keys()) and h != x]
            for u in different:
                neighbours_u = [g for g in gr.graph.nodes if g in list(gr.graph.adj[u].keys())]

                for v in neighbours_u:
                    copy_gr = get_copy_graph(gr)
                    copy_gr.switched = []
                    copy_gr.flag_switching = False
                    copy_gr.graph.remove_edge(x, y)
                    copy_gr.graph.remove_edge(u, v)
                    copy_gr.graph.add_edge(x, u)
                    copy_gr.graph.add_edge(y, v)

                    if not isomorphism.is_isomorphic(gr.graph, copy_gr.graph):
                        gr.switched.append(copy_gr)
                        graphs[index_meta_graph].append(copy_gr)

    connect_graphs(gr, index_meta_graph)


def make_part_meta_graph(gr, index_meta_graph):
    mg = meta_graphs
    edge_switching(gr, index_meta_graph)
    for g in gr.switched:
        make_part_meta_graph(g, index_meta_graph)
    check_result_nodes(index_meta_graph)


def check_result_nodes(index_meta_graph):
    mg = meta_graphs
    for k in meta_graphs[index_meta_graph].graph.nodes:
        for l in meta_graphs[index_meta_graph].graph.nodes:
            if k != l and k not in l.switched and not isomorphism.is_isomorphic(k.graph, l.graph):
                meta_graphs[index_meta_graph].add_edge(k, l)
    calculate_diameter(index_meta_graph)


def calculate_diameter(number):
    answer = nx.diameter(meta_graphs[number])
    answers.append(answer)


def build_meta_graph(initial_graph, index_meta_graph):
    mg = meta_graphs
    ghs = graphs
    graphs[index_meta_graph].append(initial_graph)
    meta_graphs[0].graph.add_node(initial_graph)
    edge_switching(initial_graph, index_meta_graph)
    for gr in meta_graphs[index_meta_graph].graph.nodes:
        make_part_meta_graph(gr, index_meta_graph)  # граф, номер в листе метаграфа
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
    global answers
    global graphs  # [] список всех вершин мета графа, по номеру мета графа
    global meta_graphs
    answers = []
    graphs = []
    meta_graphs = []  # список метаграфов
    # degrees = [[4, 4, 3, 3, 2, 2, 1, 1], [7, 6, 3, 3, 2, 2, 1, 1], [4, 3, 3, 2, 2], [5, 4, 3, 3, 2, 1]]
    degrees = [[4, 3, 3, 2, 2]]
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
        graphs.append([])
    for i in range(len(result_graphs_for_degrees)):
        build_meta_graph(result_graphs_for_degrees[i], i)  # граф, номер в листе метаграфа
    for a in answers:
        z = 0
        print(a)


if __name__ == "__main__":
    main()
