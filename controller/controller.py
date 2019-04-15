class Controller:

    def __init__(self, problem):
        self.problem = problem

    def bfs(self):
        """
        Solves the sudoku using breadth-first-search
        :return: the winning state - if solvable
            None - otherwise
        """
        queue = [self.problem.initial_state]
        while len(queue) > 0:
            current_state = queue.pop(0)
            # print(current_state)
            if current_state.is_final():
                return current_state
            queue = queue + self.problem.expand(current_state)
        return None

    def gbfs(self):
        """
        Solves the sudoku using greedy best-first-search
        :return: the winning state -if solvable
            None - otherwse
        """
        visited = []
        to_visit = [self.problem.initial_state]
        while len(to_visit) > 0:
            state = to_visit.pop(0)
            visited.append(state)
            if state.is_final():
                return state
            aux = []
            for next_state in self.problem.expand(state):
                if next_state not in visited:
                    aux.append(next_state)
            aux = [[next_state, self.problem.heuristics(next_state)] for next_state in aux]
            aux.sort(key=lambda next_state_pair: next_state_pair[1])
            aux = [next_state[0] for next_state in aux]
            to_visit = aux[:] + to_visit
        return None
