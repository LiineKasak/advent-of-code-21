from functools import reduce


def get_input():
    # return [
    #     '2199943210',
    #     '3987894921',
    #     '9856789892',
    #     '8767896789',
    #     '9899965678'
    # ]
    file = open('input/09.txt')
    return [line.replace('\n', '') for line in file.readlines()]


def padded_input(pad_value: str) -> list:
    heightmap = get_input()
    zero_line = pad_value * len(heightmap[0])
    vertically_padded = [zero_line] + heightmap + [zero_line]
    horizontally_padded = [pad_value + line + pad_value for line in vertically_padded]
    int_map = [[int(x) for x in line] for line in horizontally_padded]
    return int_map


def is_low_point(map: list, x: int, y: int):
    val = map[x][y]
    return val < map[x - 1][y] and val < map[x + 1][y] and val < map[x][y - 1] and val < map[x][y + 1]


def get_low_points(height_map: list) -> list:
    vals = []
    for x in range(1, len(height_map) - 1):
        for y in range(1, len(height_map[0]) - 1):
            # print(f'({x, y}): {height_map[x][y]}   is_low {is_low_point(height_map, x, y)}')
            if is_low_point(height_map, x, y):
                vals.append((x, y))
    return vals


def part1():
    height_map = padded_input(pad_value='9')
    points = get_low_points(height_map)

    values = [height_map[x][y] + 1 for x, y in points]
    print(sum(values))


def get_basin_size(x: int, y: int, height_map: list, visited_map: list = None) -> int:
    if visited_map is None:
        visited_map = [[False for _ in line] for line in height_map]

    if visited_map[x][y] or height_map[x][y] == 9:
        return 0

    visited_map[x][y] = True
    basin_size = 1
    for x_new in [x + 1, x - 1]:
        basin_size += get_basin_size(x_new, y, height_map, visited_map)
    for y_new in [y + 1, y - 1]:
        basin_size += get_basin_size(x, y_new, height_map, visited_map)
    return basin_size


def part2():
    height_map = padded_input(pad_value='9')
    points = get_low_points(height_map)

    basin_sizes = [get_basin_size(x, y, height_map) for x, y in points]
    largest_3 = sorted(basin_sizes)[-3:]

    largest_3_mult = reduce(lambda x, y: x * y, largest_3, 1)
    print(largest_3_mult)


if __name__ == '__main__':
    part1()
    part2()
