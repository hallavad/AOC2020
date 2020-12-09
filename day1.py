from aocd import data, submit

day = 1
submit = True

def submit_a(res):
    submit(res, part="a", day=day, year=2020)

def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
data_list = list(map(int, data.split("\n")))






# Part a
# O(N^2)
def part_a(d):
    for i in range(len(d)):
        for j in range(i+1, len(d)):
            if d[i]+d[j] == 2020:
                print(d[i]*d[j])
                submit_a(d[i]*d[j])

def sum_2_numbers(numbers, sum):
    # sort the list
    numbers.sort()

    upper = len(numbers)-1
    lower = 0

    while upper > lower:
        # raise lower bound
        while numbers[lower]+numbers[upper] < sum:
            lower += 1

        if numbers[lower]+numbers[upper] == sum:
#            submit_a(numbers[lower]*numbers[upper])
            return True

        upper -= 1

    print("couldn't find a match")
    return False

# Part b
# O(N^3)
def three_sum_2020(d):
    for i in range(len(d)):
        for j in range(i+1, len(d)):
            for k in range(j+1, len(d)):
                if d[i]+d[j]+d[k] == 2020:
                    print(d[i]*d[j]*d[k])
                    submit_b(d[i]*d[j]*d[k])
