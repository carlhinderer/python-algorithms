from collections import namedtuple
from enum import Enum
# from math import sqrt

import random


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

MazeLocation = namedtuple('MazeLocation', ['row', 'column'])


class Maze:
    def __init__(self, rows=10, columns=10, sparseness=0.2, start=(0, 0), goal=(9, 9)):
        # Initialize basic instance variables
        self._rows = rows
        self._columns = columns
        self.start = MazeLocation(*start)
        self.goal = MazeLocation(*goal)

        # Fill the grid with empty cells
        self._grid = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]

        # Populate the grid with blocked cells
        self._randomly_fill(rows, columns, sparseness)

        # Fill the start and goal locations in
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def _randomly_fill(self, rows, columns, sparseness):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def goal_test(self, m1):
        return m1 == self.goal

    def successors(self, m1):
        locations = []

        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))
            
        return locations

    def __str__(self):
        output = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output


if __name__ == '__main__':
    maze = Maze()
    print(maze)
