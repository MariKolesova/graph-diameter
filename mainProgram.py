import networkx as nx
import matplotlib.pyplot as plt
import copy


class Graph:
    degrees = []

    def __init__(self, num, tops):
        self.param = [num, tops[num], []]


# Для базового алгоритма возможных_назначений[i] = диапазон(0,graph.n_vertices). То есть все вершины являются возможными
# Ульманн расширяет этот базовый алгоритм, сужая возможности:
def update_possible_assignments(graph,subgraph,possible_assignments): #########################3
  any_changes=True
  while any_changes:
    any_changes = False
    for i in range(0,len(subgraph.n_vertices)):
      for j in possible_assignments[i]:
        for x in subgraph.adjacencies(i):
          match=False
          for y in range(0,len(graph.n_vertices)):
            if y in possible_assignments[x] and graph.has_edge(j,y):
              match=True
          if not match:
            possible_assignments[i].remove(j)
            any_changes = True


# Идея состоит в том, что если узел i подграфа может соответствовать узлу j графа, то для каждого узла x,
# смежного с узлом i в подграфе, должна быть возможность найти узел y, смежный с узлом j. на графике.
# Этот процесс помогает больше, чем может показаться на первый взгляд очевидным, потому что каждый раз,
# когда мы устраняем возможное назначение, это может привести к исключению других возможных назначений,
# поскольку они взаимозависимы.
def search(graph,subgraph,assignments,possible_assignments): ###################################
    update_possible_assignments(graph,subgraph,possible_assignments)

    i = len(assignments)

    # Make sure that every edge between assigned vertices in the subgraph is also an
    # edge in the graph.
    for edge in subgraph.edges:
        if edge.first < i and edge.second < i:
            if not graph.has_edge(assignments[edge.first], assignments[edge.second]):
                return False

    # If all the vertices in the subgraph are assigned, then we are done.
    if i == subgraph.n_vertices:
        return True

    for j in possible_assignments[i]:
        if j not in assignments:
            assignments.append(j)

        # Create a new set of possible assignments, where graph node j is the only
        # possibility for the assignment of subgraph node i.
        # Создайте новый набор возможных назначений, где узел графа j является единственным
        # возможность назначения узла подграфа i.
            new_possible_assignments = deep_copy(possible_assignments) # copy.deepcopy?
            new_possible_assignments[i] = [j]

            if search(graph,subgraph,assignments,new_possible_assignments):
                return True

            assignments.pop()
        possible_assignments[i].remove(j)
        update_possible_assignments(graph,subgraph,possible_assignments)


def find_isomorphism(graph,subgraph): ############################################3
    assignments = []
    possible_assignments = [[True]*graph.n_vertices for i in range(subgraph.n_vertices)]
    if search(graph, subgraph, assignments, possible_assignments):
        return assignments
    return None


def edge_switching(gr):
    mg = meta_graph  # !!!!!!!!!!!!!!!!!!!!!!1
    grs = graphs  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

    # meta_graph.add_node(gr)
    switched_graphs = [gr]
    for x in list(gr.adj.keys()):
        for y in list(gr.adj[x].keys()):
            different = [h for h in gr.nodes if h not in list(gr.adj[x].keys())]
            del different[0]
            for u in different:
                neighbours_u = [g for g in gr.nodes if g in list(gr.adj[u].keys())]

                for v in neighbours_u:
                    copy_gr = get_copy_graph(gr)
                    copy_gr.remove_edge(x, y)
                    copy_gr.remove_edge(u, v)
                    copy_gr.add_edge(x, u)
                    copy_gr.add_edge(y, v)
                    switched_graphs.append(copy_gr)
                    # meta_graph.add_node(copy_gr)
                    # meta_graph.add_edge(gr, copy_gr)
                    # graphs.append(copy_gr)
    return switched_graphs


def build_meta_graph(initial_graph):
    mg = meta_graph  # !!!!!!!!!!!!!!!!!!!!!!!!!111111111

    meta_graph.add_node(initial_graph)
    equivalent_graphs = edge_switching(initial_graph)

    # while len(equivalent_graphs) != 0:
    #
    #     # проверка на эквивалентность
    #     temp = equivalent_graphs.pop(0)
    #     for node in meta_graph.nodes():
    #         pass


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
    degrees = [[4, 3, 3, 2, 2], [5, 4, 3, 3, 2, 1], [4, 4, 3, 3, 2, 2, 1, 1], [7, 6, 3, 3, 2, 2, 1, 1]]
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
        # nx.draw(graph)
        # plt.show()


if __name__ == "__main__":
    main()
