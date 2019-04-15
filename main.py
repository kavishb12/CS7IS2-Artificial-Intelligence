from controller.controller import Controller
from domain.problem import Problem
from ui.ui import UI


def main():
    problem = Problem((2, [[0, 0], [0, 0]]))
    controller = Controller(problem)
    ui = UI(controller)
    ui.run()


main()