from aocd import data, submit
import day1
from functools import reduce


#the current day
day = 9

#submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)

# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():
    return [int(v) for v in data.split('\n')]



def part_a():
    d = process_data()

    for i in range(25,len(d)):
        if not day1.sum_2_numbers(d[i-25:i], d[i]):
            print(d[i])
            #submit_a(d[i])
            return d[i]


part_a()


def part_b():
    d = process_data()

    sums = []
    inv_num = part_a()
    i = 25

    sum = 0
    start_i = i
    lower = d[i]
    upper = d[i]

    while i < len(d):
        if sum == inv_num:
            sums.append((lower, upper, i-start_i, start_i, i))
            i += 1
            start_i = i
            sum = d[i]
            lower = d[i]
            upper = d[i]

        elif sum < inv_num:
            sum += d[i]

            upper = d[i] if d[i] > upper else upper
            lower = d[i] if d[i] < lower else lower

        elif sum > inv_num:
            i = start_i+1
            sum = d[i]
            start_i = i
            lower = d[i]
            upper = d[i]

        i += 1

    longest_sum = reduce(lambda x, y: x if x[2] > y[2] else y, sums)

    res = longest_sum[0] + longest_sum[1]
    print(res)
    #submit_b(res)


part_b()
