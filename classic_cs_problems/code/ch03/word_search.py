from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint


GridLocation = namedtuple('GridLocation', ['row', 'column'])


def generate_grid(rows, columns):
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]


def display_grid(grid)
    for row in grid:
        print("".join(row))


def generate_domain(word, grid):
    domain = []
    height = len(grid)
    width = len(grid[0])
    length = len(word)

    for row in range(height):
        for col in range(width):
            columns = range(col, col + length + 1)
            rows = range(row, row + length + 1)
            