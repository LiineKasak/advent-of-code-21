import numpy as np

board_len = 5


def get_input():
    file = open('04-input.txt')
    lines = file.readlines()
    bingo_numbers = list(map(int, lines[0].split(',')))
    bingo_boards = []

    for i_line in range(2, len(lines), board_len + 1):
        board = [list(map(int, line.split())) for line in lines[i_line: i_line + board_len]]
        bingo_boards.append(board)
    return bingo_numbers, bingo_boards


def is_win(board_of_hit: np.array) -> bool:
    global board_len
    for i in range(board_len):
        if np.all(board_of_hit[:, i]) or np.all(board_of_hit[i, :]):
            return True
    return False


def get_win_index(board: list, win_numbers: list) -> tuple:
    board = np.array(board)
    board_of_hit = np.repeat(False, board_len ** 2).reshape(board_len, board_len)

    for move_i, bingo_nr in enumerate(win_numbers):
        board_of_hit[board == bingo_nr] = True
        if is_win(board_of_hit):
            return move_i, np.sum((board_of_hit == False) * board)
    return -1, board_len ** 2


def part1():
    numbers, boards = get_input()

    best_move_nr = len(numbers)
    winning_score = 0

    for board in boards:
        nr_moves, unmarked_sum = get_win_index(board, numbers)
        print(nr_moves, unmarked_sum)
        print(numbers[nr_moves])
        if nr_moves < best_move_nr:
            winning_score = unmarked_sum * numbers[nr_moves]
            best_move_nr = nr_moves
    print(winning_score)


def part2():
    pass


if __name__ == '__main__':
    part1()
    part2()
