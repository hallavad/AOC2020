from aocd import data, submit

day = 1

def submit_a(res):
    submit(res, part="a", day, year=2020)

def submit_b(res):
    submit(res, part="b", day, year=2020)


# Process the input data into a list
data_list = list(map(int, data.split("\n")))
