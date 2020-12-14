from aocd import data, submit

#the current day
day = 12

# submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)

# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


# Process the input data into a list
def process_data():
    return [(v[0], int(v[1:])) for v in data.split('\n')]

class Ship:
    def __init__(self):
        self.face = 0
        self.east = 0
        self.north = 0

        self.w_east = 10
        self.w_north = 1




    def move(self, instr, dist):

        if instr == 'N':
            self.north += dist
        elif instr == 'S':
            self.north -= dist
        elif instr == 'E':
            self.east += dist
        elif instr == 'W':
            self.east -= dist
        elif instr == 'L':
            self.face = (self.face - dist/90) % 4
        elif instr == 'R':
            self.face = (self.face + dist/90) % 4
        elif instr == 'F':
            face = {
                    0: 'E',
                    1: 'S',
                    2: 'W',
                    3: 'N'
                    }

            self.move(face[self.face], dist)

    def move2(self, instr, dist):

        if instr == 'N':
            self.w_north += dist
        elif instr == 'S':
            self.w_north -= dist
        elif instr == 'E':
            self.w_east += dist
        elif instr == 'W':
            self.w_east -= dist
        elif instr == 'L':
            facing = (dist/90) % 4
            while facing > 0:
                self.w_north, self.w_east = (self.w_east, -self.w_north)
                facing -= 1

        elif instr == 'R':
            facing = (dist/90) % 4
            while facing > 0:
                self.w_north, self.w_east = (-self.w_east, self.w_north)
                facing -= 1

        elif instr == 'F':
            self.north += self.w_north * dist
            self.east += self.w_east * dist



def part_a():

    ship = Ship()
    for instr in process_data():
        ship.move(*instr)

    res = abs(ship.east) + abs(ship.north)
    print(res)
    submit_a(res)

def part_b():
    ship = Ship()

    for instr in process_data():
        ship.move2(*instr)

    res = abs(ship.east) + abs(ship.north)
    print(res)
    submit_b(res)

part_b()
