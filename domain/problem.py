from copy import deepcopy

from domain.state import State
from domain.move import Move


class Problem:

    def __init__(self, initial):
        """
        Initializes the problem with an initial state and grid size
        :param initial: (size, grid) tuple
        """
        self.size = initial[0]
        self.grid = initial[1]
        self.initial_state = State()
        for i in range(0, self.size):
            for j in range (0, self.size):
                if self.grid[i][j] == 0:
                    self.initial_state + Move(i, j)

    def expand(self, state):
        """
        Expands the current state to the next possible states
        :param state: the current state
        :return: the next states
        """
        return state.next_states(self.build_grid_from_state(state))

    def build_grid_from_state(self, state):
        """
        Builds the current state grid by placing the state's moves on the initial grid
        :param state: the current state
        :return: the built grid
        """
        new_grid = deepcopy(self.grid)
        for move in state.moves:
            new_grid[move.x][move.y] = move.number
        return new_grid

    def heuristics(self, state):
        """
        Counts how many times the last move's number happens on the grid
        :param state: the current state
        :return: the number of times the move happens on the grid
        """
        count = -1
        new_grid = self.build_grid_from_state(state)
        for x in range(0, len(new_grid)):
            for y in range (0, len(new_grid)):
                if state.moves[state.next_index-1].number == new_grid[x][y]:
                    count += 1
        return count




