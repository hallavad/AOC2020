from aocd import data, submit
import copy

#the current day
day = 8


# submit part a
def submit_a(res):
    submit(res, part="a", day=day, year=2020)


# submit part b
def submit_b(res):
    submit(res, part="b", day=day, year=2020)


class state:
    def __init__(self, instrs):
        self.terminate = False
        self.accu = 0
        self.instrs = instrs
        self.instr_id = 0

    def run(self):
        while not self.terminate:
            if self.instr_id >= len(self.instrs):
                return True

            if self.instrs[self.instr_id].execute(self):
                self.instr_id += 1

        return False


class instr:
    def __init__(self, instr, arg):
        self.instr = instr
        self.arg = arg
        self.run = False

    def execute(self, state):
        if self.run:
            print('A', state.accu)
#            submit_a(state.accu)
            state.terminate = True
            return False

        instr_ls = {
                'nop': self.nop,
                'acc': self.acc,
                'jmp': self.jmp
                }
        self.run = True
        return instr_ls[self.instr](state)

    def nop(self, state):
        return True

    def acc(self, state):
        state.accu += int(self.arg)

        return True

    def jmp(self, state):
        state.instr_id += int(self.arg) - 1

        return True


# Process the input data into a list
def process_data():
    def val_func(x):
        instr_name, arg = x.split(' ')

        return instr(instr_name, arg)

    return [val_func(d) for d in data.split('\n')]


def part_a():
    d = process_data()

    state(d).run()


part_a()


def change_instr(start, instrs):
    i = start

    while i < len(instrs):
        if instrs[i].instr == 'nop':
            instrs[i].instr = 'jmp'
            return (i, instrs)
        if instrs[i].instr == 'jmp':
            instrs[i].instr = 'nop'
            return (i, instrs)
        i += 1

    return (i, instrs)


def part_b():
    d = process_data()
    ch_instr = 0

    while ch_instr < len(d):
        ch_instr, instrs = change_instr(ch_instr, copy.deepcopy(d))
        st = state(instrs)
        if st.run():
            print('B', st.accu)
#            submit_b(st.accu)
            break

        ch_instr += 1


part_b()
