def get_input():
    file = open('input/10.txt')
    return list(map(lambda line: line.replace('\n', ''), file.readlines()))


error_scores_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
complete_scores_dict = {')': 1, ']': 2, '}': 3, '>': 4}
closing_to_opening = {')': '(', ']': '[', '}': '{', '>': '<'}
opening_to_closing = {'(': ')', '[': ']', '{': '}', '<': '>'}


def get_error_score(line: str) -> int:
    """
    Find the first closing parenthesis that causes a syntax error (no matching parentheses in stack);
    and return the score of it.
    If there is no syntax error, return 0.

    :param line: chunk of parentheses code to evaluate. Allowed chars in '()[]{}<>'.
    :return: int score of error or 0.
    """
    global error_scores_dict, closing_to_opening
    stack = []
    for c in line:
        if c in closing_to_opening.values():
            stack.append(c)
        elif c in closing_to_opening.keys():
            if len(stack) == 0 or stack.pop() != closing_to_opening[c]:
                return error_scores_dict[c]
    return 0


def complete_line(line: str) -> str:
    """
    Complete the line of parentheses code such that every opening parenthesis has a matching closing parenthesis.

    :param line: chunk of (uncompleted) parentheses code. Allowed chars in '()[]{}<>'.
    :return: string which completes line such that it is syntactically valid.
    """
    global opening_to_closing
    stack = []
    for c in line:
        if c in closing_to_opening.values():
            stack.append(c)
        elif stack[-1] == closing_to_opening[c]:
            stack.pop()

    autocomplete = ''.join(list(map(lambda c: opening_to_closing[c], stack[::-1])))
    return autocomplete


def score_autocomplete(line: str) -> int:
    """
    Calculate the score of the autocompleted string.
    Scoring rules: for each char, multiply total score with 5, then add the cost of the current autocompleted char.

    :param line: autocompleted parentheses code. Allowed chars in '()[]{}<>'.
    :return: score of the autocompleted string.
    """
    global complete_scores_dict
    total_score = 0

    for c in line:
        total_score *= 5
        total_score += complete_scores_dict[c]
    return total_score


def part1():
    """Find the total error score of the lines of parentheses syntax."""
    lines = get_input()

    total_score = sum(list(map(lambda line: get_error_score(line), lines)))
    print(total_score)


def part2():
    """
    Calculate the autocomplete score for each parentheses syntax code line completion;
    sort the array and return the middle score.
    """
    lines = list(filter(lambda line: get_error_score(line) == 0, get_input()))

    scores = list(map(lambda line: score_autocomplete(complete_line(line)), lines))
    print(sorted(scores)[len(scores) // 2])


if __name__ == '__main__':
    part1()
    part2()
