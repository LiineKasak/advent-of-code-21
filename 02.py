from typing import Callable


def get_input():
    file = open('02-input.txt')
    return file.readlines()


def move(params: tuple, command: str) -> tuple:
    """
    Simple move function:
        - 'forward' increases position
        - 'down' increases depth
        - 'up' decreases depth

    :param params: consists of integers values for depth, position and aim
    :param command: string command consisting of a direction (str) and step (int)
    :return: new params for placement after moving
    """
    depth, position, _ = params
    dir, step = command.split()
    step = int(step)

    if dir == 'forward':
        position += step
    elif dir == 'down':
        depth += step
    elif dir == 'up':
        depth -= step

    return depth, position, _


def move_with_aim(params: tuple, command: str) -> tuple:
    """
    Move function using aim:
        - 'forward' increases *position* by step and *depth* by step*aim.
        - 'down' increases *aim*
        - 'up' decreases *aim*

    :param params: consists of integers values for depth, position and aim
    :param command: string command consisting of a direction (str) and step (int)
    :return: new params for placement after moving
    """
    depth, position, aim = params
    dir, step = command.split()
    step = int(step)

    if dir == 'forward':
        position += step
        depth += step * aim
    elif dir == 'down':
        aim += step
    elif dir == 'up':
        aim -= step

    return depth, position, aim


def apply_moves(move_fn: Callable) -> int:
    """
    Apply move commands from the input file, given a move function that interprets commands.

    :param move_fn: given move function that accepts
    1) a tuple of parameters (depth, position, aim) and
    2) a command (direction and step).
    :return: int product of final depth and position
    """
    params = 0, 0, 0
    for command in get_input():
        params = move_fn(params, command)
    depth, position, _ = params
    return depth * position


def part1():
    """Calculate product of final position and final depth."""
    print(apply_moves(move_fn=move))


def part2():
    """Calculate product of final position and final depth using commands with aim."""
    print(apply_moves(move_fn=move_with_aim))


if __name__ == '__main__':
    part1()
    part2()
