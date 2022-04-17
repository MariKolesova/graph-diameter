import networkx as nx
from networkx.algorithms import isomorphism
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
    for i in equiv_graphs.switched:
        for j in equiv_graphs.switched:
            if i != j and not isomorphism.is_isomorphic(i.graph, j.graph):
                meta_graphs[index_meta_g].graph.add_edge(i, j)


def edge_switching(gr, index_meta_graph):  # (граф, номер мета)
    ghs = graphs
    mg = meta_graphs
    if not gr.flag_switching:
        gr.flag_switching = True
    else:
        return
    if gr not in meta_graphs[index_meta_graph].graph.nodes:
        meta_graphs[index_meta_graph].graph.add_node(gr)
    for x in list(gr.graph.nodes):
        for y in list(gr.graph.adj[x].keys()):
            different = [h for h in gr.graph.nodes if h not in list(gr.graph.adj[x].keys()) and h != x]
            for u in different:
                neighbours_u = [g for g in gr.graph.nodes if g in list(gr.graph.adj[u].keys())]

                for v in neighbours_u:
                    copy_gr = get_copy_graph(gr)
                    copy_gr.switched = []
                    copy_gr.flag_switching = False
                    if x != u and y != v:
                        copy_gr.graph.remove_edge(x, y)
                        copy_gr.graph.remove_edge(u, v)
                        copy_gr.graph.add_edge(x, u)
                        copy_gr.graph.add_edge(y, v)

                        sum_degrees = count_sum(copy_gr)

                        if not isomorphism.is_isomorphic(gr.graph, copy_gr.graph) \
                                and sum(copy_gr.degrees) == sum_degrees \
                                and not flag_checked(copy_gr, index_meta_graph):
                            gr.switched.append(copy_gr)
                            copy_gr.switched.append(gr)
                            meta_graphs[index_meta_graph].graph.add_edge(gr, copy_gr)
                            graphs[index_meta_graph].append(copy_gr)

    connect_graphs(gr, index_meta_graph)


def flag_checked(gr, index):
    gphs = graphs
    mg = meta_graphs
    for g in graphs[index]:
        if g.graph == gr.graph:
            return True
        else:
            return False


def count_sum(graph):
    my_s = 0
    for s in graph.graph.degree:
        my_s += s[1]
    return my_s


def check_result_nodes(index_meta_graph):
    mg = meta_graphs
    ghs = graphs
    for k in meta_graphs[index_meta_graph].graph.nodes:
        for l in meta_graphs[index_meta_graph].graph.nodes:
            if k != l and k not in l.switched and not isomorphism.is_isomorphic(k.graph, l.graph):
                meta_graphs[index_meta_graph].graph.add_edge(k, l)
    calculate_diameter(index_meta_graph)


def calculate_diameter(number):
    answer = nx.diameter(meta_graphs[number].graph)
    answers.append((number, answer))


def build_meta_graph(initial_graph, index_meta_graph):
    mg = meta_graphs
    ghs = graphs
    graphs[index_meta_graph].append(initial_graph)
    meta_graphs[index_meta_graph].graph.add_node(initial_graph)

    # for gr in meta_graphs[index_meta_graph].graph.nodes:
    #     edge_switching(gr, index_meta_graph)
    #     for g in gr.switched:
    #         edge_switching(g, index_meta_graph)
    current_size_list = copy.deepcopy(meta_graphs[index_meta_graph].graph.nodes)
    for gr in current_size_list:
        edge_switching(gr, index_meta_graph)
        for g in gr.switched:
            edge_switching(g, index_meta_graph)

    check_result_nodes(index_meta_graph)


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
    # degrees = [[4, 3, 3, 2, 2], [7, 6, 3, 3, 2, 2, 1, 1], [5, 4, 3, 3, 2, 1], [4, 4, 3, 3, 2, 2, 1, 1]]
    degrees = [[3, 2, 2, 1, 1, 1]]
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
    for i in range(len(answers)):
        print('диаметр', result_graphs_for_degrees[i].degrees, '-', answers[i][1])


if __name__ == "__main__":
    main()
