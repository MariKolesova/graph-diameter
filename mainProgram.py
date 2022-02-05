class Graph:
    def __init__(self, num, tops):
        self.param = [num, tops[num], []]


def check_graph(degrees):
    degrees.sort()
    degrees.reverse()
    graphs = []
    for i in range(len(degrees)):
        graphs.append(Graph(i, degrees))


def algorithm_Havel_Hakimi(degrees):
    tops = [degree for degree in degrees]
    while True:
        current_degree = tops[0]
        del tops[0]
        for i in range(current_degree):
            tops[i] -= 1
            if tops[i] < 0:
                print('последовательность не графическая')
                return
        tops.sort()
        tops.reverse()
        if all(tops[i] == 0 for i in tops):
            print("последовательность графическая")
            break


def main():
    global vertices
    with open('data.txt', 'r') as file:
        vertices = file.read().split(' ')
        for i in range(len(vertices)):
            vertices[i] = int(vertices[i])
    algorithm_Havel_Hakimi(vertices)
    check_graph(vertices)


if __name__ == "__main__":
    main()
