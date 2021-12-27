import copy
from queue import PriorityQueue
import numpy as np


def get_input():
    file = open('input/15.txt')
    return list(map(lambda line: list(map(int, list(line.rstrip()))), file.readlines()))


def get_neighbors(x, y, max_x, max_y):
    neighbors = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    return list(filter(lambda coord: 0 <= coord[0] < max_y and 0 <= coord[1] < max_x, neighbors))


def dijkstra(v_costs: list):
    x_len, y_len = len(v_costs[0]), len(v_costs)
    costs = [[float('inf') for _ in range(x_len)] for _ in range(y_len)]
    costs[0][0] = 0

    pq = PriorityQueue()
    pq.put((0, (0, 0)))
    visited = set()

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.add(current_vertex)
        y, x = current_vertex

        for neighbor in get_neighbors(x, y, x_len, y_len):
            ny, nx = neighbor
            distance = v_costs[ny][nx]
            if neighbor not in visited:
                old_cost = costs[ny][nx]
                new_cost = costs[y][x] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    costs[ny][nx] = new_cost
    return costs


def part1():
    costs = get_input()
    total = dijkstra(costs)

    # final cost without starting point cost
    final_cost = total[-1][-1] - total[0][0]
    print(final_cost)


def one_higher_costs(costs: list) -> list:
    for row in range(len(costs)):
        for col in range(len(costs[0])):
            cost = costs[row][col]
            costs[row][col] = cost + 1 if cost < 9 else 1
    return costs


def get_full_map(costs: list) -> list:
    upped_costs = [costs]
    for _ in range(8):
        upped_costs.append(one_higher_costs(copy.deepcopy(upped_costs[-1])))

    rows_of_full_map = np.empty((0, len(costs[0] * 5)))
    for i_row in range(5):

        row = np.empty((len(costs), 0))
        for i_col in range(5):
            row = np.append(row, np.array(upped_costs[i_col + i_row]), axis=1)

        rows_of_full_map = np.append(rows_of_full_map, row, axis=0)

    return [list(map(int, row)) for row in rows_of_full_map]


def part2():
    costs = get_input()
    full_costs = get_full_map(costs)
    total = dijkstra(full_costs)

    # final cost without starting point cost
    final_cost = total[-1][-1] - total[0][0]
    print(final_cost)


if __name__ == '__main__':
    part1()
    part2()
