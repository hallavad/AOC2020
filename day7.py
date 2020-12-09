from aocd import data, submit

# the current day
day = 7


# submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)


# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# hashmap with the outer bags as keys
def process_data_outer():
    def val_func(out_bag):
        out_color, other = out_bag.split(' bags contain ')

        in_bag = []
        if not other.startswith('no '):
            for bag in other.split(', '):
                word = bag.split(' ')
                in_bag.append((int(word[0]), word[1] + ' ' + word[2]))

        return (out_color, in_bag)

    return {val[0]: val[1] for val in [val_func(out_bag) for out_bag in data.split('\n')]}


# hashmap with inner bags as keys
def process_data_inner():
    rules = data.split('\n')

    parsed_rules = {}
    for rule in rules:
        out_color, other = rule.split(' bags contain ')

        if not other.startswith('no '):
            for bag in other.split(', '):
                word = bag.split(' ')
                color = word[1] + ' ' + word[2]
                if color in parsed_rules:
                    parsed_rules[color].append((int(word[0]), out_color))
                else:
                    parsed_rules[color] = [(int(word[0]), out_color)]

    return parsed_rules


def part_a():
    d = process_data_inner()

    def inside_of(color):
        if color in d:
            outer_bags = [color]
            for outer_bag in d[color]:
                outer_bags += inside_of(outer_bag[1])
            return outer_bags
        else:
            return [color]

    res = len(set(inside_of('shiny gold'))) - 1

    print(res)
#    submit_a(res)


part_a()


def part_b():
    d = process_data_outer()

    def count_bags(color):
        if color in d:
            num_bags = 0
            for inner_bag in d[color]:
                num_bags += inner_bag[0] + inner_bag[0] * count_bags(inner_bag[1])
            return num_bags
        else:
            return 0

    res = count_bags('shiny gold')

    print(res)
#    submit_b(res)

part_b()
