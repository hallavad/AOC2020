from aocd import data, submit
from functools import reduce

# the current day
day = 10


# submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)


# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():
    return [int(v) for v in data.split('\n')]


def part_a():
    d = sorted(process_data())

    one_step = 0
    three_step = 1
    curr_jolts = 0

    for adapter in d:
        diff = adapter - curr_jolts

        if diff == 1:
            one_step += 1
        elif diff == 2:
            print("two steps") # My input doesn't have any required 2 steps in it since this is not printed
        elif diff == 3:
            three_step += 1
        elif diff > 3:
            break

        curr_jolts = adapter

    res = one_step * three_step
    print(res)
    #submit_a(res)


part_a()


def part_b():
    d = sorted(process_data())

    x = [[0]]
    x_i = 0
    curr_jolts = 0
    for adapter in d:
        diff = adapter - curr_jolts

        if diff == 1:
            x[x_i].append(adapter)
        elif diff == 3:
            x.append([adapter])
            x_i += 1
        elif diff > 3:
            break

        curr_jolts = adapter

    # How many choices you have with contigual list of number of size N
    choices = {
            1: 1,
            2: 1,
            3: 2,
            4: 4,
            5: 7,
    }
    res = reduce(lambda x, y: x * y, map(lambda x: choices[len(x)], x))

    print(res)
    #submit_b(res)


part_b()
