from aocd import data, submit
from functools import reduce

#the current day
day = 16

# submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)

# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():
    def parse_rules(input):
        rules = []
        for val in input.split('\n'):
            type = 'rule'

            name, rule = val.split(': ')
            r1, r2 = rule.split(' or ')
            r1l, r1h = r1.split('-')
            r2l, r2h = r2.split('-')

            rules.append((name, int(r1l), int(r1h), int(r2l), int(r2h)))
        return rules
    def parse_mine(input):
        return [int(v) for v in input.split('\n')[1].split(',')]

    def parse_nearby(input):
        return [[int(v) for v in row.split(',')] for row in input.split('\n')[1:]]

    sections = data.split('\n\n')

    return {'rules': parse_rules(sections[0]), 'mine': parse_mine(sections[1]), 'nearby': parse_nearby(sections[2])}

def simplify_rule(rules):
       simple_rules = [rule]

       return simple_rules


def determine_invalid(rules, ticket):
    invalid_val = []
    for val in ticket:
        valid = False
        for rule in rules:
            if rule[1] <= val <= rule[2] or rule[3] <= val <= rule[4]:
                valid = True

        if not valid:
            invalid_val.append(val)

    return (True if len(invalid_val) == 0 else False, invalid_val)



def part_a():
    d = process_data()

    invalid_val = []
    for ticket in d['nearby']:
        invalid_val += determine_invalid(d['rules'], ticket)[1]

    res = sum(invalid_val)
    print(res)
    submit_a(res)


def part_b():
    d = process_data()

    valid_nearby = [nearby for nearby in d['nearby'] if determine_invalid(d['rules'], nearby)[0]]

    nearby_fields = d['rules']

    valid_field_nearby = []
    for ticket in valid_nearby:
        ticket_rule_validity = []
        for val in ticket:
            rule_validity = []
            for rule in d['rules']:
                rule_validity.append(rule[1] <= val <= rule[2] or rule[3] <= val <= rule[4])
            ticket_rule_validity.append(rule_validity)
        valid_field_nearby.append(ticket_rule_validity)

    valid_rules_per_field = reduce(lambda t1, t2: [[f1 and f2 for f1, f2 in zip(v1, v2) ] for v1, v2 in zip(t1, t2)], valid_field_nearby)

    rules_to_field = {}
    while len(rules_to_field) < 20:

        for rule_i, field_rule_validity in enumerate(valid_rules_per_field):

            if sum(field_rule_validity) == len(rules_to_field) + 1:
                for field_i, field in enumerate(field_rule_validity):
                    if field and field_i not in rules_to_field.values():
                        rules_to_field[rule_i] = field_i
                        break


    res = reduce(lambda a, b: a * b, [d['mine'][i] for i in range(20) if rules_to_field[i] < 6])

    print(res)
    #submit_b(res)


part_b()
