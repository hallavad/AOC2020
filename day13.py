from aocd import data, submit
from functools import reduce

#the current day
day = 13


#submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)


# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():
    d_time, bus_IDs = data.split('\n')

    return (int(d_time), [int(bus_ID) for bus_ID in bus_IDs.split(',') if bus_ID != 'x'])


def part_a():
    d_time, bus_IDs = data.split('\n')

    bus_IDs = [int(bus_ID) for bus_ID in bus_IDs.split(',') if bus_ID != 'x']
    d_time = int(d_time)

    first_bus = reduce(lambda b1, b2: b1 if b1[1] < b2[1] else b2, map(lambda b: (b, b - (d_time % b)), bus_IDs))

    res = first_bus[0] * first_bus[1]
    print(res)
    #submit_a(res)


part_a()

def extended_gcd(a, b):
    old_r, r = (a, b)
    old_s, s = (1, 0)
    old_t, t = (0, 1)

    while r != 0:
        quotient = old_r // r
        old_r, r = (r, old_r - quotient * r)
        old_s, s = (s, old_s - quotient * s)
        old_t, t = (t, old_t - quotient * t)

    return (old_s)

def chinese_remainder_theorem(busses):
    _, N = reduce(lambda b1, b2: (0, b1[1]*b2[1]), busses)

    sum = 0
    for a, n in busses:
        y = N // n
        sum += a * extended_gcd(y, n) * y

    return sum % N


def part_b():
    _, bus_IDs = data.split('\n')

    bus_IDs = [(int(bus_ID)-i, int(bus_ID)) for i, bus_ID in enumerate(bus_IDs.split(',')) if bus_ID != 'x']
    print(bus_IDs)

    res = chinese_remainder_theorem(bus_IDs)

    print(int(res))
    #submit_b(int(res))

part_b()
