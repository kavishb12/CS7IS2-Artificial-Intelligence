#coding: utf-8

from gui import show_board
from harmonysearch import *
import random as _r_

def main(problem, methods=("constraint propagation", "harmony search"),
         gui=True, iterations=10000, HMS=40, HCR=.95, PAR=.5):
    prob = load_problem(problem)
    grid = Grid(prob)
    solution = grid.get_problem()
    locked = grid.locked.copy()
    
    if "constraint propagation" in methods:
        solution = grid.constraint_propagation()
        score = Grid(prob).evaluate()
        
    if "harmony search" in methods:
        hs_out = harmony_search(solution, iterations=iterations, HMS=HMS, HCR=HCR, PAR=PAR)
        solution = hs_out[2][0].numbers
        score = hs_out[2][1]
    
    if gui:
        show_board(solution, locked, score)
        
    return (solution, score)

res = []

def main_loop(res=res):
    for execution in range(100):
        iterations = 5000
        HMS = _r_.choice(list(range(10,51)))
        HCR = float("{0:.2f}".format(_r_.random()*_r_.random()+0.4))
        PAR = float("{0:.2f}".format(_r_.random()*_r_.random()))
        main_out = main("veryhard1", iterations=iterations,
                        HMS=HMS, HCR=HCR, PAR=PAR)
        res.append((main_out[1], HMS, HCR, PAR))
        res.sort(key=lambda x: x[0], reverse=True)