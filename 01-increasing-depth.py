# https://adventofcode.com/2021/day/1

def get_input():
    file = open('01-input.txt')
    return list(map(int, file.readlines()))


def part1():
    """
    Find the number of times the depth has increased.

    The input array is in chronological order.
    We need to compare single values - current compared to the next one.
    """
    depths = get_input()
    times_increased = sum([1 for i, depth in enumerate(depths[1:]) if depth > depths[i]])
    print(times_increased)


def part2():
    """
    Find the number of times the depth has increased between triplets.

    The input array is in chronological order.
    We need to compare triple values. First triple: i:i+3. Second triplet: i+1:i+4.
    Counts as increase in depth if the sum of first triplet is smaller than the sum of the second triplet.
    """
    depths = get_input()
    times_triplet_increased = sum(
        [1 for i in range(len(depths) - 3) if sum(depths[i:i + 3]) < sum(depths[i + 1:i + 4])])
    print(times_triplet_increased)


if __name__ == '__main__':
    part1()
    part2()
