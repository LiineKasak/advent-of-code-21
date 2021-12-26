def get_input():
    file = open('input/12.txt')
    return [line.strip().split('-') for line in file.readlines()]


def flatten(t):
    return [item for sublist in t for item in sublist]


def get_neighbors(edges: list) -> dict:
    vertices = set(flatten(edges))
    neighbors = {vertex: set() for vertex in vertices}

    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    return neighbors


def dfs(neighbors: dict, path: list = ['start'], allow_twice: bool = True):
    current = path[-1]
    if current == 'end':
        return 1

    nr_paths = 0
    for neighbor in neighbors[current]:
        if neighbor == 'start':
            continue
        if str(neighbor).islower() and neighbor in path:
            if allow_twice:
                nr_paths += dfs(neighbors, path + [neighbor], False)
            continue
        nr_paths += dfs(neighbors, path + [neighbor], allow_twice)

    return nr_paths


def part1():
    graph_edges = get_input()
    neighbor_map = get_neighbors(graph_edges)

    print(dfs(neighbor_map, allow_twice=False))


def part2():
    graph_edges = get_input()
    neighbor_map = get_neighbors(graph_edges)

    print(dfs(neighbor_map, allow_twice=True))


if __name__ == '__main__':
    part1()
    part2()
