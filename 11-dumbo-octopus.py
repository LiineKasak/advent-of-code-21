def get_input():
    file = open('input/11.txt')
    return [[int(x) for x in line.replace('\n', '')] for line in file.readlines()]


def pad_grid(grid: list) -> list:
    empty_line = [0] * (len(grid[0]) + 2)
    return [empty_line] + [[0] + line + [0] for line in grid] + [empty_line]


def print_grid(grid: list) -> None:
    print('\n'.join([''.join(list(map(str, line[1:-1]))) for line in grid[1:-1]]))
    print('-' * len(grid[0]))


def one_step(grid: list) -> tuple:
    grid = [[x + 1 for x in line] for line in grid]

    flashed = set()
    to_flash = set()

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == 10:
                to_flash.add((y, x))

    while len(to_flash) != 0:
        y, x = to_flash.pop()
        flashed.add((y, x))
        grid[y][x] = 0

        for y_new in [y - 1, y, y + 1]:
            for x_new in [x - 1, x, x + 1]:
                if x_new in [0, len(grid[0]) - 1] or y_new in [0, len(grid) - 1]:
                    continue
                new = (y_new, x_new)
                if new not in flashed and new not in to_flash:
                    grid[y_new][x_new] += 1
                    if grid[y_new][x_new] == 10:
                        to_flash.add(new)
    # print_grid(grid)
    return len(flashed), grid


def simulate_steps(grid: list, nr_step: int = 1) -> int:
    nr_flashes = 0

    for _ in range(nr_step):
        step_flashes, grid = one_step(grid)
        nr_flashes += step_flashes

    return nr_flashes


def part1():
    grid = pad_grid(get_input())

    print(simulate_steps(grid, nr_step=100))


def calc_first_all_flash(grid: list) -> int:
    nr_octopuses = (len(grid[0]) - 2) * (len(grid) - 2)

    step_nr = 0
    while True:
        step_nr += 1
        nr_flashes, grid = one_step(grid)
        if nr_octopuses == nr_flashes:
            return step_nr


def part2():
    unpadded_grid = get_input()
    grid = pad_grid(unpadded_grid)

    print(calc_first_all_flash(grid))


if __name__ == '__main__':
    part1()
    part2()
