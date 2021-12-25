from typing import Iterable

length_to_digit = {2: 1, 3: 7, 4: 4, 7: 8}


def get_input():
    # return ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    #         'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
    #         'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
    #         'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
    #         'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
    #         'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
    #         'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
    #         'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
    #         'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
    #         'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce']
    file = open('input/08.txt')
    return [line.replace('\n', '') for line in file.readlines()]


def flatten(t):
    return [item for sublist in t for item in sublist]


def get_digits():
    lines = get_input()
    split_lines = [[part.split(' ') for part in line.split(' | ')] for line in lines]
    return split_lines


def part1():
    global length_to_digit

    digits = get_digits()
    output_digits = flatten([line[1] for line in digits])

    nr_1478 = len([digit for digit in output_digits if len(digit) in length_to_digit.keys()])
    print(nr_1478)


def find_unique_match(iterable: Iterable, condition):
    results = list(filter(condition, iterable))
    assert len(results) == 1
    return results[0]


def contains_str(test: str, should_contain: str) -> bool:
    return len(list(filter(lambda char: char not in test, should_contain))) == 0


def get_digit_to_pattern(unique_patterns):
    global length_to_digit

    digit = {length_to_digit[len(p)]: p for p in unique_patterns if len(p) in length_to_digit.keys()}

    length_6 = list(filter(lambda p: len(p) == 6, unique_patterns))
    length_5 = list(filter(lambda p: len(p) == 5, unique_patterns))

    # find 9 from length 6, containing 4
    digit[9] = find_unique_match(length_6, lambda p: contains_str(p, digit[4]))

    # find 0 from length 6, containing 1, is not 9
    digit[0] = find_unique_match(length_6, lambda p: contains_str(p, digit[1]) and p is not digit[9])

    # find 6 from length 6, is not 0, is not 9
    digit[6] = find_unique_match(length_6, lambda p: p not in [digit[0], digit[9]])

    # find 5 from length 5, contained by 6
    digit[5] = find_unique_match(length_5, lambda p: contains_str(digit[6], p))

    # find 3 from length 5, contains 7
    digit[3] = find_unique_match(length_5, lambda p: contains_str(p, digit[7]))

    # find 2 from length 5, is not 3, is not 5
    digit[2] = find_unique_match(length_5, lambda p: p not in [digit[3], digit[5]])
    return digit


def get_output(unique_patterns: list, output_digits: list) -> int:
    digit_to_pattern = get_digit_to_pattern(unique_patterns)

    output = ''
    for pattern in output_digits:
        for d, p in digit_to_pattern.items():
            if contains_str(p, pattern) and contains_str(pattern, p):
                output += str(d)
                break

    return int(output)


def part2():
    digits = get_digits()

    total_sum = sum(list(map(lambda d: get_output(*d), digits)))
    print(total_sum)


if __name__ == '__main__':
    part1()
    part2()
