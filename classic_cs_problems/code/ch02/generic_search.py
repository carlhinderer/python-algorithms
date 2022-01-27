from collections import deque


class Stack:
    def __init__(self):
        self._container = []

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()   # LIFO

    def __repr__(self):
        return repr(self._container)


class Queue:
    def __init__(self):
        self._container = deque()

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.popleft()      # FIFO

    def __repr__(self):
        return repr(self._container)


class Node:
    def __init__(self, state, parent, cost=0.0, heuristic=0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def dfs(initial, goal_test, successors):
    # Frontier is where we have yet to go
    frontier = Stack()
    frontier.push(Node(initial, None))

    # Explored is where we've been
    explored = {initial}

    # Keep going while there is more to explore
    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state

        # If we found the goal, we're done
        if goal_test(current_state):
            return current_node

        # Check where we can go next and haven't explored
        for child in successors(current_state):
            if child in explored:
                continue              # Skip children we already explored
            explored.add(child)
            frontier.push(Node(child, current_node))

    return None


def bfs(initial, goal_test, successors):
    frontier = Queue()
    frontier.push(Node(initial, None))

    explored = {initial}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state

        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))

    return None


# Gives us the path of a given node, which we can use to reconstruct the path we took
def node_to_path(node):
    path = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path



if __name__ == '__main__':
    s = Stack()
    s.push(123)
    s.push('abc')
    print(s.pop())
    print(s.pop())
    assert s.empty
