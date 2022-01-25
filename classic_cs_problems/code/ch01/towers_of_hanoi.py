
class Stack:
    def __init__(self):
        self._container = []

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)


def hanoi(begin, end, temp, n):
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)


def print_towers(tower_a, tower_b, tower_c):
    print('Tower A: ', tower_a)
    print('Tower B: ', tower_b)
    print('Tower C: ', tower_c)


if __name__ == '__main__':
    num_discs = 3
    tower_a = Stack()
    tower_b = Stack()
    tower_c = Stack()

    for i in range(1, num_discs + 1):
        tower_a.push(i)

    print('Staring State:')
    print_towers(tower_a, tower_b, tower_c)

    hanoi(tower_a, tower_c, tower_b, num_discs)

    print('Ending State:')
    print_towers(tower_a, tower_b, tower_c)
