from aocd import data, submit
from functools import reduce

#the current day
day = 4

#submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)

# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():
    def val_func(x):
        cred_pairs = [pair.split(':') for pair in x.split()]
        return {cred[0]: cred[1] for cred in cred_pairs}

    return [val_func(d) for d in data.split('\n\n')]

def validate_cred_type(cred):
    req_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

    return all(map(lambda f: f in cred, req_fields))

def validate_cred_val(cred):
    val_f = {
            'byr': lambda v: 1920 <= int(v) <= 2002,
            'iyr': lambda v: 2010 <= int(v) <= 2020,
            'eyr': lambda v: 2020 <= int(v) <= 2030,
            'hgt': lambda v: (v[-2:] == 'in' and 59 <= int(v[:-2]) <= 76) or (v[-2:] == 'cm' and 150 <= int(v[:-2]) <= 193),
            'hcl': lambda v: v[0] == '#' and all([c in '0123456789abcdef' for c in v[1:]]),
            'ecl': lambda v: v in ['amb','blu','brn','gry','grn','hzl','oth'],
            'pid': lambda v: len(v) == 9 and all([c in '0123456789' for c in v]),
    }
    valid_fields = {'byr': False,'iyr': False,'eyr': False,'hgt': False,'hcl': False,'ecl': False,'pid': False}

    for k,v in cred.items():
        if k in val_f.keys():
            valid_fields[k] = val_f[k](v)

    return all(valid_fields.values())

def part_a():
    d = process_data()
    res = sum(map(validate_cred_type, d))
    print(res)
#    submit_a(res)

part_a()

def part_b():
    d = process_data()
    res = sum(map(validate_cred_val, d))

    print(res)
#    submit_b(res)

part_b()
