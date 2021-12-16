def get_input():
    file = open('input/05.txt')
    return file.readlines()


def get_coords_on_path(pos1: tuple, pos2: tuple, with_diag: bool = True) -> list:
    [x1, y1], [x2, y2] = pos1, pos2
    coords = []
    x_change, y_change = x2 - x1, y2 - y1

    x_dir = 1 if x_change > 0 else -1
    y_dir = 1 if y_change > 0 else -1
    x_range = range(0, x_change + x_dir, x_dir)
    y_range = range(0, y_change + y_dir, y_dir)

    if not with_diag and x_change != 0 and y_change != 0:
        return []
    elif x_change != 0 and y_change != 0:
        coords += [(x1 + x_step, y1 + y_step) for x_step, y_step in zip(x_range, y_range)]
    elif x_change != 0:
        coords += [(x1 + x_step, y1) for x_step in x_range]
    else:
        coords += [(x1, y1 + y_step) for y_step in y_range]
    # print(f'from {pos1} to {pos2} = {coords}')
    return coords


def solve(with_diag: bool = True) -> None:
    lines = get_input()
    vents = [[list(map(int, coords.split(','))) for coords in line.split(' -> ')] for line in lines]

    nr_lines_in_coord = dict()
    for pos1, pos2 in vents:
        path_coords = get_coords_on_path(pos1, pos2, with_diag=with_diag)

        for coords in path_coords:
            if coords not in nr_lines_in_coord:
                nr_lines_in_coord[coords] = 0
            nr_lines_in_coord[coords] += 1

    nr_at_least_2 = len(list(filter(lambda nr_lines: nr_lines >= 2, nr_lines_in_coord.values())))
    print(nr_at_least_2)


def part1():
    solve(with_diag=False)


def part2():
    solve(with_diag=True)


if __name__ == '__main__':
    part1()
    part2()
