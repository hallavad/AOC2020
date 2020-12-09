from aocd import data, submit
from functools import reduce

day = 2

def submit_a(res):
    submit(res, part="a", day=day, year=2020)

def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():
    def val_func(x):

        rule, pas = x.split(": ")
        bounds, key = rule.split(" ")
        lo, hi = bounds.split("-")

        return (pas, key, int(lo), int(hi))


    return list(map(val_func, data.split("\n")))

def part_a():
    d = process_data()

    valid = 0

    for pas, key, lo, hi in d:
        count = pas.count(key)
        if count >= lo and count <= hi:
            valid += 1
    print(valid)
#    submit_a(valid)

part_a()

def part_b():
    d = process_data()

    valid = 0

    for pas, key, lo, hi in d:
        if (pas[lo-1] == key) != (pas[hi-1] == key):
            valid += 1
    print(valid)
#    submit_b(valid)

part_b()


# Alternate solutions to both parts that only goes through the puzzel input once
def alternate_solution():
    def sol_a(pas, key, lo, hi):
        return int(lo <= pas.count(key) <= hi)

    def sol_b(pas, key, lo, hi):
        return int((pas[lo-1] == key) != (pas[hi-1] == key))

    def sol_combined(x):
        return (sol_a(*x), sol_b(*x))

    def reduce_combined(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def val_processing(x):

        rule, pas = x.split(": ")
        bounds, key = rule.split(" ")
        lo, hi = bounds.split("-")

        return (pas, key, int(lo), int(hi))


    processed_data = map(val_processing, data.split("\n"))
    valid_a,valid_b = reduce(reduce_combined, map(sol_combined, processed_data))

    print(valid_a)
#    submit_a(valid_a)

    print(valid_b)
#    submit(valid_b)

alternate_solution()
