from aocd import data, submit


# the current day
day = 5


# submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)


# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():
    def line_func(line):
        return int(''.join(list(map(lambda c: str(int(c in 'BR')), line))), 2)

    return {line_func(d) for d in data.split('\n')}


def part_a():
    d = process_data()

    res = max(d)

    print(res)
#    submit_a(res)


part_a()


def part_b():
    passports = process_data()
    passports = d
    for seat in passports:
        if seat+1 not in passports and seat+2 in passports:
            print(seat+1)
#            submit_b(seat+1)


part_b()
