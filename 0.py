from aocd import data, submit

#the current day
day =

# submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)

# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():
    def val_func(val):
        return val

    return [val_func(x) for x in data.split('\n')]
