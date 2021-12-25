def get_input():
    file = open('input/06.txt')
    return list(map(int, file.readlines()[0].split(',')))


def simulate(timers: list, nr_days) -> list:
    print(f'day 0: {timers}')
    for i in range(nr_days):
        nr_creates_new = timers[0]
        timers = timers[1:] + [nr_creates_new]
        timers[6] += nr_creates_new
    return timers


def get_nr_alive_fish(nr_days: int) -> int:
    timers = get_input()
    timer_list = [0 for _ in range(9)]

    for timer in timers:
        timer_list[timer] += 1

    new_timer_list = simulate(timer_list, nr_days)
    return sum(new_timer_list)


def part1():
    print(get_nr_alive_fish(80))


def part2():
    print(get_nr_alive_fish(256))


if __name__ == '__main__':
    part1()
    part2()
