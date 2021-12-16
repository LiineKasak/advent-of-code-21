import numpy as np


def get_input() -> np.ndarray:
    """Get bits as numpy array."""
    file = open('input/03.txt')
    return np.array([[int(bit) for bit in line.replace('\n', '')] for line in file.readlines()])


def get_most_common(array: np.ndarray) -> np.ndarray:
    """
    Calculate the most common column value for each column in a 2D array consisting of bit values.

    :param array: 2D numpy array consisting of zeros and ones
    :return: 1D numpy array where int at pos i represents the most common column value
    """
    nr_ones = np.count_nonzero(array, 0)
    nr_zeros = np.repeat(array.shape[0], array.shape[1]) - nr_ones

    is_one_most_common = nr_ones > nr_zeros
    return is_one_most_common.astype(int)


def bin_int_arr_to_str(array: np.ndarray) -> int:
    """
    Convert a numpy array representing a number in bit system to a decimal.

    :param array: 1D numpy array consisting of 0s and 1s representing a binary number.
    :return: Decimal value of given binary number.
    """
    return int(''.join([str(x) for x in array]), 2)


def part1():
    """
    Calculate the gamma and epsilon value and return their product.

    Gamma value: the decimal value of the string made up from the MOST common
    column values in a 2D array of binary values.
    Epsilon value: the decimal value of the string made up from the LEAST common
    column values in a 2D array of binary values.
    """
    data = get_input()
    gamma_array = get_most_common(data)
    gamma_nr = bin_int_arr_to_str(gamma_array)

    # switch ones and zeros as we want least common
    epsilon_array = gamma_array ^ (gamma_array & 1 == gamma_array)
    epsilon_nr = bin_int_arr_to_str(epsilon_array)

    print(gamma_nr * epsilon_nr)


def find_rating(data: np.ndarray, most_common: bool = True) -> int:
    """
    Find the rating from either most or least common values of a 2D binary array.

    Iterate over the columns, and for each column i keep the rows which
    have the most common (or least common) value of that column in position i.
    Return the decimal value of bits if only one row remains.

    :param data: 2D numpy array of binary values
    :param most_common: if we want to keep the most common value in each column (not least)
    :return: decimal value of remaining row
    """
    for i in range(data.shape[1]):

        col_nr_ones = np.count_nonzero(data[:, i])
        col_nr_zeros = data.shape[0] - col_nr_ones

        keep_nr = 1 if col_nr_ones >= col_nr_zeros else 0
        if not most_common:
            keep_nr = 0 if keep_nr == 1 else 1
        data = data[data[:, i] == keep_nr]

        if data.shape[0] == 1:
            break
    return bin_int_arr_to_str(data[0])


def part2():
    """
    Calculate the oxygen and CO2 rating and return their product (life support rating).

    Oxygen rating: the result of find_rating for MOST common values per column.
    CO2 rating: the result of find_rating for LEAST common values per column.
    """
    data = get_input()

    oxygen_rating = find_rating(data, most_common=True)
    co2_rating = find_rating(data, most_common=False)

    life_support_rating = oxygen_rating * co2_rating
    print(oxygen_rating, co2_rating)
    print(life_support_rating)


if __name__ == '__main__':
    part1()
    part2()
