import networkx as nx


class Graph:
    degrees = []

    def __init__(self, num, tops):
        self.param = [num, tops[num], []]


def edge_switching(gr):
    temp = graphs
    for x in list(gr.adj.keys()):
        for y in list(gr.adj[x].keys()):
            different = [h for h in gr.nodes if h not in list(gr.adj[x].keys())]
            del different[0]
            for u in different:
                neighbours_u = [g for g in gr.nodes if g in list(gr.adj[u].keys())]
                for v in neighbours_u:
                    gr.remove_edge(x, y)
                    gr.remove_edge(u, v)
                    gr.add_edge(x, u)
                    gr.add_edge(y, v)
                    graphs.append(gr)
    d = 0



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
        # nx.draw(graph)
        # plt.show()


if __name__ == "__main__":
    main()
