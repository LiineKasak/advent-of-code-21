import sys
from math import log2
from functools import reduce


def get_input():
    file = open('input/16.txt')
    return file.readlines()[0]


def get_package_data(bin_data: str) -> tuple:
    version = int(bin_data[:3], 2)
    type_id = int(bin_data[3:6], 2)
    content = bin_data[6:]
    return version, type_id, content


def get_literal_value(package_content: str) -> tuple:
    groups = []
    for i in range(0, len(package_content) - 4, 5):
        groups.append(package_content[i + 1:i + 5])
        is_last = package_content[i] == '0'
        if is_last:
            next_content = package_content[i + 5:]
            return int(''.join(groups), 2), next_content


def get_operator(package_content: str) -> tuple:
    length_type_id = package_content[0]
    total_length, nr_sub_packets = sys.maxsize, sys.maxsize

    if length_type_id == '0':
        total_length = int(package_content[1:16], 2)
        sub_packets = package_content[16:]
    else:
        nr_sub_packets = int(package_content[1:12], 2)
        sub_packets = package_content[12:]
    return total_length, nr_sub_packets, sub_packets


def sum_versions(bin_data: str) -> int:
    if bin_data.replace('0', '') == '':
        return 0
    version_sum = 0
    version, type_id, content = get_package_data(bin_data)
    version_sum += version

    if type_id == 4:
        literal_value, next_content = get_literal_value(content)
        version_sum += sum_versions(next_content)
    else:
        _, _, sub_packets = get_operator(content)
        version_sum += sum_versions(sub_packets)
    return version_sum


def part1():
    hex_data = get_input()
    nr_bits = int(len(hex_data) * log2(16))
    bin_data = bin(int(hex_data, 16))[2:].zfill(nr_bits)
    print(sum_versions(bin_data))


def get_sub_packets(content: str) -> tuple:
    total_length, nr_sub_packets, next_content = get_operator(content)

    sub_values = []

    current_length = 0
    while nr_sub_packets != 0 and total_length > current_length and next_content is not None:
        current_length += len(next_content)
        value, next_content = parse_expression(next_content)
        current_length -= len(next_content)

        nr_sub_packets -= 1
        sub_values.append(value)
    return sub_values, next_content


def parse_expression(bin_data: str) -> tuple:
    version, type_id, content = get_package_data(bin_data)

    if type_id == 4:
        literal_value, next_content = get_literal_value(content)
        return literal_value, next_content

    sub_values, next_content = get_sub_packets(content)
    if type_id == 0:
        return sum(sub_values), next_content
    elif type_id == 1:
        return reduce(lambda x, y: x * y, sub_values), next_content
    elif type_id == 2:
        return min(sub_values), next_content
    elif type_id == 3:
        return max(sub_values), next_content
    elif type_id == 5:
        assert len(sub_values) == 2
        is_greater = 1 if sub_values[0] > sub_values[1] else 0
        return is_greater, next_content
    elif type_id == 6:
        assert len(sub_values) == 2
        is_less = 1 if sub_values[0] < sub_values[1] else 0
        return is_less, next_content
    elif type_id == 7:
        assert len(sub_values) == 2
        is_equal = 1 if sub_values[0] == sub_values[1] else 0
        return is_equal, next_content
    print('not allowed!!!')


def part2():
    hex_data = get_input()
    nr_bits = int(len(hex_data) * log2(16))
    bin_data = bin(int(hex_data, 16))[2:].zfill(nr_bits)
    print(parse_expression(bin_data)[0])


if __name__ == '__main__':
    part1()
    part2()
