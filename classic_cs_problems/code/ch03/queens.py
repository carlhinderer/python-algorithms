from csp import Constraint, CSP


class QueensConstraint(Constraint):
    def __init__(self, columns):
        super().__init__(columns)
        self.columns = columns

    def satisfied(self, assignment):
        # q1c = queen 1 column, q1r = queen 1 row
        for q1c, q1r in assignment.items():
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r = assignment[q2c]
                    if q1r == q2r:       # Same row?
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):     # Same diagonal?
                        return False
        return True 



if __name__ == "__main__":
    # Set up chess board
    columns = list(range(1, 9))
    rows = {}

    for column in columns:
        rows[column] = list(range(1, 9))

    # Set up CSP
    csp = CSP(columns, rows)
    csp.add_constraint(QueensConstraint(columns))

    # Solve
    solution = csp.backtracking_search()
    if solution is None:
        print('No solution found!')
    else:
        print(solution)