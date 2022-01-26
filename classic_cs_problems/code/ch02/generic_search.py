
class Stack:
    def __init__(self):
        self._container = []

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        return self._container.append(item)

    def pop(self):
        return self._container.pop()   # LIFO

    def __repr__(self):
        return repr(self._container)


class Node:
    def __init__(self, state, parent, cost, heuristic):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


if __name__ == '__main__':
    s = Stack()
    s.push(123)
    s.push('abc')
    print(s.pop())
    print(s.pop())
    assert s.empty