from domain.problem import Problem
from time import time


class UI:

    def __init__(self, controller):
        self.controller = controller

    def print_menu(self):
        s = ""
        s += "0. Exit \n"
        s += "1. Read a grid :)\n"
        s += "2. Solve with BFS\n"
        s += "3. Solve with GBFS\n"
        print(s)

    def read_grid(self):
        f = open("grid1.txt", "r")
        lines = f.readlines()
        size = int(lines[0])
        grid = [[int(val) for val in line.split()] for line in lines[1:]]
        self.controller.problem = Problem((size, grid))

    def find_solution_bfs(self):
        start_time = time()
        solution = self.controller.bfs()
        solution_grid = self.controller.problem.build_grid_from_state(solution)
        for x in range(0, len(solution_grid)):
            for y in range (0, len(solution_grid)):
                print(solution_grid[x][y], end=" ")
            print()
        print('execution time = ', time() - start_time, " seconds")

    def find_solution_gbfs(self):
        start_time = time()
        solution = self.controller.bfs()
        solution_grid = self.controller.problem.build_grid_from_state(solution)
        for x in range(0, len(solution_grid)):
            for y in range(0, len(solution_grid)):
                print(solution_grid[x][y], end=" ")
            print()
        print('execution time = ', time() - start_time, " seconds")

    def run(self):
        self.print_menu()
        running = True
        while running:
            try:
                command = int(input(">> "))
                if command == 0:
                    running = False
                if command == 1:
                    self.read_grid()
                if command == 2:
                    self.find_solution_bfs()
                if command == 3:
                    self.find_solution_gbfs()
            except Exception as e:
                print(str(e))
