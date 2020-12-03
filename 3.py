from aocd import data, submit

#the current day
day = 3

#submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)

# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():

    # changed to using list comprehension instead of map for better readability
    return [[x == '#' for x in d ] for d in data.split("\n")]

def check_slope(d, xdiff,ydiff):
    width = len(d[0])

    trees = 0
    x = 0
    y = 0
    while y < len(d):
        if d[y][x]:
            trees += 1

        x = (xdiff + x) % width
        y += ydiff

    return trees

def part_a():
    res = check_slope(process_data(), 3, 1)
    print(res)
    #submit_a(res)

def part_b():
    d = process_data()

    res = check_slope(d, 1, 1) * check_slope(d, 3, 1) * check_slope(d, 5, 1) * check_slope(d, 7, 1) * check_slope(d, 1, 2)

    print(res)
    #submit_b(res)

part_a()
part_b()
