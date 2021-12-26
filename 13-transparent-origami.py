import numpy as np


def get_input():
    file = open('input/13.txt')
    lines = list(map(lambda line: line.rstrip(), file.readlines()))
    coordinates = [list(map(int, line.split(','))) for line in lines if len(line) > 0 and line[0].isdigit()]
    folds = [line.split(' ')[-1] for line in lines if 'fold' in line]
    return coordinates, folds


def print_paper(paper: np.ndarray):
    for line in paper:
        for is_dot in line:
            print('#' if is_dot else '.', end='')
        print()
    print()


def to_numpy_map(coordinates: list) -> np.ndarray:
    max_x = max([c[0] for c in coordinates])
    max_y = max([c[1] for c in coordinates])

    arr = np.zeros((max_y + 1, max_x + 1), dtype=bool)

    for coord in coordinates:
        arr[coord[1]][coord[0]] = True
    return arr


def make_horizontal_fold(paper: np.ndarray, coord: int):
    upper, lower = paper[:coord], paper[coord + 1:]
    lower = np.flip(lower, 0)

    return upper + lower


def make_vertical_fold(paper: np.ndarray, coord: int):
    left, right = paper[:, :coord], paper[:, coord + 1:]
    right = np.flip(right, 1)

    return left + right


def apply_folds(paper: np.ndarray, folds: list) -> np.ndarray:
    for fold in folds:
        text, coord = fold.split('=')
        is_horizontal_fold = text == 'y'

        if is_horizontal_fold:
            paper = make_horizontal_fold(paper, int(coord))
        else:
            paper = make_vertical_fold(paper, int(coord))
    return paper


def part1():
    coordinates, folds = get_input()
    paper = to_numpy_map(coordinates)
    paper = apply_folds(paper, [folds[0]])
    print(np.count_nonzero(paper))


def part2():
    coordinates, folds = get_input()
    paper = to_numpy_map(coordinates)

    paper = apply_folds(paper, folds)
    print_paper(paper)


if __name__ == '__main__':
    part1()
    part2()
