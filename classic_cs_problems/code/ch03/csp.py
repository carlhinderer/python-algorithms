from abc import abstractmethod


class Constraint:
    def __init__(self, variables):
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment):
        ...


class CSP:
    def __init__(self, variables, domains):
        self.variables = variables             # The variables to be constrained
        self.domains = domains                 # The domain of each variable
        self.constraints = {}

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable, assignment):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment={}):
        # Assignment is complete if every variable is assigned
        if len(assignment) == len(self.variables):
            return assignment

        # Get all variables in the CSP but not in the assignment
        unassigned = [v for v in self.variables if v not in assignment]

        # Get every possible domain value of the first unassigned variable
        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value

            # If we're still consistent, we recurse
            if self.consistent(first, local_assignment):
                result = self.backtracking_search(local_assignment)

                # If we didn't find the result, we will end up backtracking
                if result is not None:
                    return result

        return None
