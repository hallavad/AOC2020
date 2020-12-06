from aocd import data, submit

#the current day
day = 6

#submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)

# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():

    return [group for group in data.split("\n\n")]


def part_a():
    res = sum(map(lambda x: len(set(x.replace('\n',''))), process_data()))

    print(res)
#    submit_a(res)


part_a()

def part_b():
    res = sum([len(set.intersection(*[set(person) for person in group.split('\n')])) for group in process_data()])

    print(res)
#    submit_b(res)

part_b()
