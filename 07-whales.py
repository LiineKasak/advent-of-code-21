from typing import Callable


def get_input():
    # return [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    file = open('input/07.txt')
    return list(map(int, file.readlines()[0].split(',')))


def get_linear_cost(positions: list, chosen_pos: int):
    return sum([abs(pos - chosen_pos) for pos in positions])


cost_arr = []


def get_exp_cost(positions: list, chosen_pos: int):
    global cost_arr
    nr_moves = [abs(pos - chosen_pos) for pos in positions]

    return sum([cost_arr[move] for move in nr_moves])


def get_optimal_cost(positions: list, cost_fun: Callable):
    min_pos, max_pos = min(positions), max(positions)

    while min_pos <= max_pos:

        if min_pos == max_pos:
            return cost_fun(positions, min_pos)

        mid = (min_pos + max_pos) // 2
        mid_cost = cost_fun(positions, mid)
        next_cost = cost_fun(positions, mid + 1)

        if max_pos - min_pos == 1:
            return min(mid_cost, next_cost)

        if mid_cost < next_cost:
            max_pos = mid
        elif mid_cost > next_cost:
            min_pos = mid


def part1():
    positions = get_input()
    print(get_optimal_cost(positions, get_linear_cost))


def build_cost_arr(max_pos: int):
    global cost_arr

    cost_arr = [0]
    for i in range(1, max_pos + 1):
        cost_arr.append(cost_arr[-1] + i)


def part2():
    positions = get_input()
    build_cost_arr(max(positions) - min(positions))
    print(get_optimal_cost(positions, get_exp_cost))


if __name__ == '__main__':
    part1()
    part2()
