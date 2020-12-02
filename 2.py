from aocd import data, submit

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
