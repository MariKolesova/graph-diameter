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
    ans = answers
    ghs = graphs
    mg = meta_graphs
    for i in equiv_graphs.switched:
        for j in equiv_graphs.switched:
            if i != j and not isomorphism.is_isomorphic(i.graph, j.graph):
                meta_graphs[index_meta_g].graph.add_edge(i, j)


def edge_switching(gr, index_meta_graph):  # (граф, номер мета)
    ans = answers
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
                neighbours_x = list(gr.graph.adj[x].keys())
                neighbours_y = list(gr.graph.adj[y].keys())
                neighbours_u = [g for g in gr.graph.nodes if g in list(gr.graph.adj[u].keys())]
                for neighbour in neighbours_u:
                    if neighbour in neighbours_x or neighbour in neighbours_y:
                        neighbours_u.remove(neighbour)

                for v in neighbours_u:
                    copy_gr = Graph()
                    copy_gr.degrees = gr.degrees
                    copy_gr.switched = []
                    copy_gr.flag_switching = False
                    copy_gr.graph = copy.deepcopy(gr.graph)
                    if x != u and y != v:
                        copy_gr.graph.remove_edge(x, y)
                        copy_gr.graph.remove_edge(u, v)
                        copy_gr.graph.add_edge(x, u)
                        copy_gr.graph.add_edge(y, v)

                        sum_degrees = count_sum(copy_gr)

                        #  графы изоморфны
                        #  сумма степеней вершин == заявленной для построения
                        #  флаг, что copy_gr не изоморфен всем верщинам метаграфа
                        #  граф и переключенный не равны
                        if not isomorphism.is_isomorphic(gr.graph, copy_gr.graph) \
                                and sum(copy_gr.degrees) == sum_degrees \
                                and not flag_checked(copy_gr, index_meta_graph) \
                                and not equals_graphs(gr, copy_gr):
                            gr.switched.append(copy_gr)
                            copy_gr.switched.append(gr)

    check_exist_nodes_with_added(gr, index_meta_graph)
    # connect_graphs(gr, index_meta_graph)  # ????????? выше соединили уже
    if get_diameter(index_meta_graph):
        calculate_diameter(index_meta_graph)


def equals_graphs(g1, g2):
    ans = answers
    ghs = graphs
    mg = meta_graphs
    for el in g1.switched:
        if el.graph.edges == g2.graph.edges:
            g1.switched.remove(el)
    return False


def check_exist_nodes_with_added(gr, index):
    ans = answers
    ghs = graphs
    mg = meta_graphs
    # for i in range(len(meta_graphs[index].graph.nodes)):
    #     for j in range(len(gr.switched)):
    #         if len(meta_graphs[index].graph.nodes) != 1:
    #             if not isomorphism.is_isomorphic(list(meta_graphs[index].graph.nodes)[i].graph, gr.switched[j].graph):
    #                 meta_graphs[index].graph.add_edge(list(meta_graphs[index].graph.nodes)[i], gr.switched[j])
    #                 graphs[index].append(gr.switched[j])
    for i in range(len(meta_graphs[index].graph.nodes)):
        for j in range(len(gr.switched)):
            if gr.switched[j] not in graphs[index] and \
                    not isomorphism.is_isomorphic(list(meta_graphs[index].graph.nodes)[i].graph, gr.switched[j].graph):
                meta_graphs[index].graph.add_edge(list(meta_graphs[index].graph.nodes)[i], gr.switched[j])
                graphs[index].append(gr.switched[j])


def get_diameter(index):
    all_nodes = list(meta_graphs[index].graph.nodes)
    for node in all_nodes:
        if not node.flag_switching:
            return
    return True


def flag_checked(gr, index):
    gphs = graphs
    mg = meta_graphs
    ans = answers
    for g in graphs[index]:
        if equals_graphs(g, gr):
            return True
        else:
            return False


def count_sum(graph):
    my_s = 0
    for s in graph.graph.degree:
        my_s += s[1]
    return my_s


def calculate_diameter(number):
    ans = answers
    cnt = count
    answer = nx.diameter(meta_graphs[number].graph)
    count[number] = True
    answers[number] = (answers[0][0], answer)


def build_meta_graph(initial_graph, index_meta_graph):
    mg = meta_graphs
    ans = answers
    ghs = graphs
    cnt = count
    graphs[index_meta_graph].append(initial_graph)
    meta_graphs[index_meta_graph].graph.add_node(initial_graph)

    i = 0
    while not count[index_meta_graph]:
        edge_switching(list(meta_graphs[index_meta_graph].graph.nodes)[i], index_meta_graph)
        i += 1


def algorithm_havel_hakimi(degrees):
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
    global count
    count = []
    answers = []
    graphs = []
    meta_graphs = []  # список метаграфов
    # degrees = [[4, 3, 3, 2, 2], [3, 2, 2, 1, 1, 1], [7, 6, 3, 3, 2, 2, 1, 1], [5, 4, 3, 3, 2, 1], [4, 4, 3, 3, 2, 2, 1, 1]]
    # degrees = [[4, 3, 3, 2, 2], [7, 6, 3, 3, 2, 2, 1, 1], [5, 4, 3, 3, 2, 1]]
    degrees = [[4, 3, 3, 2, 1, 1]]
    result_graphs_for_degrees = []
    for i in range(len(degrees)):
        answer = algorithm_havel_hakimi(degrees[i])
        if answer:
            gr = build_graph(degrees[i])
            result_graphs_for_degrees.append(gr)
        else:
            print(f'последовательность {degrees[i]} не графична')
    for i in range(len(result_graphs_for_degrees)):
        meta_graphs.append(Graph())
        graphs.append([])
        count.append(False)
        answers.append((result_graphs_for_degrees[i].degrees, 0))
    for i in range(len(result_graphs_for_degrees)):
        build_meta_graph(result_graphs_for_degrees[i], i)  # граф, номер в листе метаграфа
    for i in range(len(answers)):
        print('диаметр', result_graphs_for_degrees[i].degrees, '-', answers[i][1])


if __name__ == "__main__":
    main()
