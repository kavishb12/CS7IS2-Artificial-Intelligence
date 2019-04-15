import math
from copy import deepcopy

from domain.move import Move


class State:
    """
    Holds a list of moves done
    """

    def __init__(self, moves=None, next_index=0):
        """
        Constructs a new state
        :param moves: the list of moves of the state
        :param next_index: the index of the next unfinished move in the move list
        """

        self.next_index = next_index
        if moves is None:
            self.moves = []
        else:
            self.moves = moves

    def __add__(self, other):
        if isinstance(other, Move):
            self.moves.append(other)

    def __str__(self):
        s = ""
        for move in self.moves:
            s += str(move)
            s += ", "
        return s

    def is_final(self):
        """
        Checks if all the moves are finished
        """
        if self.next_index == len(self.moves):
            return True
        return False

    def next_states(self, grid):
        """
        Builds all possible values for the next unfinished move
        :param grid: the sudoku grid with current state's moves placed on
        :return: the possible values for the next unfinished move (by creating a new state for every possible move)
        """
        states = []
        current_move = self.moves[self.next_index]

        # Compute the move's square
        box_side_length = int(math.sqrt(len(grid)))
        box_start_x = current_move.x // box_side_length * box_side_length
        box_end_x = box_start_x + box_side_length
        box_start_y = current_move.y // box_side_length * box_side_length
        box_end_y = box_start_y + box_side_length

        for number in range(1, len(grid) + 1):
            valid = True
            # Check horizontal and vertical validity
            for i in range(0, len(grid)):
                if grid[i][current_move.y] == number:  #
                    valid = False
                if grid[current_move.x][i] == number:
                    valid = False

            # print("{0},{1},{2}, {3}".format(box_start_x,box_end_x,box_start_y,box_end_y))

            # Check square validity
            for x in range(box_start_x, box_end_x):
                for y in range(box_start_y, box_end_y):
                    if grid[x][y] == number:
                        valid = False
            if valid:
                new_moves = deepcopy(self.moves)
                new_moves[self.next_index].number = number
                states.append(State(new_moves, self.next_index + 1))
        return states
