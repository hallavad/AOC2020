from aocd import data, submit
import pprint
import copy

#the current day
day = 11

# submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)

# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():
#    data = 'L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL'
    return [[seat for seat in row] for row in data.split('\n')]


def counted_seats(layout):
    counted_seats = {
                    '#': 0,
                    'L': 0,
                    '.': 0
                    }

    for row in layout:
        for spot in row:
            counted_seats[spot] += 1
    return counted_seats['#']


def adjacent_range(i, max):
    if i == 0:
        r = range(0,2)
    elif i+1 == max:
        r = range(-1,1)
    else:
        r = range(-1,2)
    return r


def run_layout(update_seat, check_adjacent):
    last_layout = process_data()

    state_changed = True

    next_layout = copy.deepcopy(last_layout)

    while state_changed:
        state_changed = False
        for y, row in enumerate(last_layout):
            for x, spot in enumerate(row):
                new_state = update_seat(spot, check_adjacent(y,x, last_layout))

                next_layout[y][x] = new_state[1]
                state_changed = state_changed or new_state[0]

        #swap last_layout with new layout and get prepared to overwrite the new next_layout with the new_layout
        temp_layout = last_layout
        last_layout = next_layout
        next_layout = temp_layout


    return counted_seats(last_layout)


def get_adjacent(y, x, layout):
    yoff_range = adjacent_range(y, len(layout))
    xoff_range = adjacent_range(x, len(layout[0]))

    adjacent = {
            '#': 0,
            'L': 0,
            '.': 0
            }

    for yoff in yoff_range:
        for xoff in xoff_range:
            if xoff == x and yoff == y:
                continue
            adjacent[layout[yoff+y][xoff+x]] += 1

    return adjacent


def part_a():
    def update_seat(state, adjacent):
        new_state = {
                '#': lambda: (True,'L') if adjacent['#'] >= 4 else (False,'#'),
                'L': lambda: (True,'#') if adjacent['#'] == 0 else (False,'L'),
                '.': lambda: (False,'.')
                }
        return new_state[state]()

    res = run_layout(update_seat, get_adjacent)
    print(res)
    #submit_a(res)

#part_a()


def get_adjacent_looking(y, x, layout):
    yoff_range = adjacent_range(y, len(layout))
    xoff_range = adjacent_range(x, len(layout[0]))

    adjacent = {
            '#': 0,
            'L': 0,
            '.': 0
            }

    for yoff in yoff_range:
        for xoff in xoff_range:
            if xoff == 0 and yoff == 0:
                continue
            offset = 1
            while layout[yoff*offset+y][xoff*offset+x] == '.':
                offset += 1
                if not len(layout) > yoff*offset+y >= 0 or not len(layout[0]) > xoff*offset+x >= 0:
                    offset -= 1
                    break

            adjacent[layout[yoff*offset+y][xoff*offset+x]] += 1
    return adjacent



def part_b():
    last_layout = process_data()

    def update_seat(state, adjacent):
        new_state = {
                '#': lambda: (True,'L') if adjacent['#'] >= 5 else (False,'#'),
                'L': lambda: (True,'#') if adjacent['#'] == 0 else (False,'L'),
                '.': lambda: (False,'.')
                }
        return new_state[state]()

    res = run_layout(update_seat, get_adjacent_looking)
    print(res)
    #submit_b(res)

part_b()
