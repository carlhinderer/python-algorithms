from generic_search import bfs, node_to_path, Node


MAX_NUM = 3

CURRENT_STATE_MSG = """
On the west bank there are {} missionaries and {} cannibals.\n
On the east bank there are {} missionaries and {} cannibals.\n
The boat is on the {} bank."""

EAST_TO_WEST_MSG = "{} missionaries and {} cannibals moved from the east bank to the west bank.\n"
WEST_TO_EAST_MSG = "{} missionaries and {} cannibals moved from the west bank to the east bank.\n"


class MCState:
    def __init__(self, missionaries, cannibals, boat):
        self.wm = missionaries             # West bank missionaries
        self.wc = cannibals                # West bank cannibals
        self.em = MAX_NUM - self.wm        # East bank missionaries
        self.ec = MAX_NUM - self.wc        # East bank cannibals
        self.boat = boat                   # Which bank the boat is on

    def __str__(self):
        return CURRENT_STATE_MSG.format(self.wm, 
                                        self.wc, 
                                        self.em, 
                                        self.ec, 
                                        ("west" if self.boat else "east"))

    def goal_test(self):
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM

    @property
    def is_legal(self):
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.em > 0:
            return False
        return True

    def successors(self):
        sucs = []

        if self.boat:              # Boat on west bank
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc - 2, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wm, self.wc - 1, not self.boat))
            if (self.wc > 0) and (self.wm > 0):
                sucs.append(MCState(self.wm - 1, self.wc - 1, not self.boat))

        else:                      # Boat on east bank
            if self.em > 1:
                sucs.append(MCState(self.wm + 2, self.wc, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.wm + 1, self.wc, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.wm, self.wc + 2, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.wm, self.wc + 1, not self.boat))
            if (self.ec > 0) and (self.em > 0):
                sucs.append(MCState(self.wm + 1, self.wc + 1, not self.boat))

        return [x for x in sucs if x.is_legal]


def display_solution(path):
    if len(path) == 0: return

    old_state = path[0]
    print(old_state)

    for current_state in path[1:]:
        if current_state.boat:
            print(EAST_TO_WEST_MSG.format(old_state.em - current_state.em, 
                                          old_state.ec - current_state.ec))
        else:
            print(WEST_TO_EAST_MSG.format(old_state.wm - current_state.wm,
                                          old_state.wc - current_state.wc))
        print(current_state)
        old_state = current_state



if __name__ == '__main__':
    start = MCState(MAX_NUM, MAX_NUM, True)
    solution = bfs(start, MCState.goal_test, MCState.successors)

    if solution is None:
        print("No solution found.")
    else:
        path = node_to_path(solution)
        display_solution(path)
