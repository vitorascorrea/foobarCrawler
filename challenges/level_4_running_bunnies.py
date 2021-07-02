class Graph():
    def __init__(self, matrix):
        self.vertices = len(matrix)
        self.edges = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i != j:
                    edge_1 = (i, j, matrix[i][j])

                    if not edge_1 in self.edges:
                        self.edges.append(edge_1)


def floyd_warshall(graph):
    dist = [[float('inf') for _ in range(graph.vertices)] for _ in range(graph.vertices)]

    for u, v, w in graph.edges:
        dist[u][v] = w

    for v in range(graph.vertices):
        dist[v][v] = 0

    for k in range(graph.vertices):
        for i in range(graph.vertices):
            for j in range(graph.vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in range(graph.vertices):
        if dist[i][i] < 0:
            return None, True

    return dist, False


def save_bunnies(distance, time_limit):
    possible_paths = []
    max_depth = 8 # arbitrary depth
    start_node = 0
    end_node = len(distance) - 1
    build_possible_paths(distance, time_limit, max_depth, start_node, [], possible_paths)

    best_path = get_best_path(possible_paths, end_node)

    return [i for i in best_path if i != start_node and i != end_node]


def build_possible_paths(times, time_limit, counter, current, path, possible_paths):
    # bad path
    if time_limit <= -5:
        return path

    if len(path) > 0 and path[-1] == len(times) - 1 and time_limit >= 0:
        possible_paths.append((time_limit, path))

    if counter <= 0:
        if time_limit >= 0:
            possible_paths.append((time_limit, path))
        return path

    # halt if path is getting too long - completly arbitrary
    if len(path) < 6:
        for i, v in enumerate(times[current]):
            if i != current:
                build_possible_paths(times, time_limit - v, counter - 1, i, path + [i], possible_paths)


def get_best_path(paths, bulkhead_index):
    best_len = float('-inf')
    best_path = None
    for p in paths:
        set_list = list(set([i for i in p[1] if i != 0 and i != bulkhead_index]))
        if len(set_list) > best_len:
            best_len = len(set_list)
            best_path = set_list

    return best_path


def solution(times, time_limit):
    if len(times) <= 2:
        return []

    graph = Graph(times)
    distance, negative_cycle = floyd_warshall(graph)

    if negative_cycle:
        return [i for i in range(len(times) - 2)]

    saved_bunnies = save_bunnies(distance, time_limit)

    return sorted([i - 1 for i in saved_bunnies])
