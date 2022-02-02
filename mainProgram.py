class Graph:
    def __init__(self, tops):
        self.params = []
        for i in range(0, len(tops)):
            self.params.append([i, tops[i]])


def check_graph(vertices):
    vertices.sort()
    vertices.reverse()
    graphs = []
    graphs.append(Graph(vertices))
    algorithm_Havel_Hakimi(graphs[0])


def algorithm_Havel_Hakimi(graph):
    while True:
        current_degree = graph.params[0][1]
        del graph.params[0]
        for i in range(current_degree):
            graph.params[i][1] -= 1
            if graph.params[i][1] < 0:
                print('bad')
                return
        graph.params.sort(key=lambda number: number[1], reverse=True)
        if all(degree[1] == 0 for degree in graph.params):
            print("good")
            break


def main():
    with open('data.txt', 'r') as file:
        degrees = file.read().split(' ')
        graph_degrees = []
        for top in degrees:
            top = int(top)
            graph_degrees.append(top)
    check_graph(graph_degrees)


if __name__ == "__main__":
    main()
