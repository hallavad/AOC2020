from aocd import data, submit

#the current day
day = 15

# submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)

# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():
    d = data.split(',')

    print(d)
    print(data)
    return ({int(v): i for i,v in enumerate(d[:-1],1)}, int(d[-1]))


def count_to(n):
    numbers, number = process_data()

    i = len(numbers.keys())+1

    while i < n:
        if number in numbers.keys():
            next_number = i - numbers[number]
            numbers[number] = i
        else:
            next_number = 0
            numbers[number] = i

        number = next_number
        i += 1

    print(number)

count_to(2020)

count_to(30000000)
