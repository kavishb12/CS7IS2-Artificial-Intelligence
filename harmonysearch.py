#coding: utf-8

import random as _r_
from sudoku_classes import Solution, Grid

def harmony_search(prob, iterations=5000, HMS=100, HCR=.6, PAR=.2):
    hm = HarmonyMemory(prob, HMS, HCR, PAR)
    for x in range(iterations):
        if hm.memory[0][1] == 0: break
        hm.improvise()
    return (x+1, hm, hm.memory[0])

class HarmonyMemory(object):
    
    def __init__(self, problem, memory_size=50, HCR=.7, PAR=.1):
        self.problem = problem
        self.memory_size = memory_size
        self.HCR = HCR
        self.PAR = PAR
        
        self.memory = [self.rand_solu(problem) for x in range(memory_size)]
        self.memory = [(s, s.evaluate()) for s in self.memory]
        self.update()
    
    def __repr__(self):
        return str(self.memory + [sum([x[1] for x in self.memory])])
        
    def update(self):
        self.memory.sort(key=lambda x: x[1])
        self.memory = self.memory[:self.memory_size]

    def rand_solu(self, problem):
        return Solution([_r_.choice(x) for x in self.problem])
        
    def memory_consideration(self, square):
        return _r_.choice([h[0].numbers[square] for h in self.memory])
        
    def insert_to_memory(self, new_harmony):
        score = new_harmony.evaluate()
        if score < self.memory[-1][1]:
            self.memory.append((new_harmony, score))

    def new_harmony(self):
        square_list = []
        for square in range(81):
            b = self.get_boundaries(square)
            if len(b) == 1: s = b[0]
            elif _r_.random() > self.HCR: s = self.random_selection(b)
            elif _r_.random() > self.PAR: s = self.memory_consideration(square)
            else: s = self.pitch_adjustment(self.memory_consideration(square), b)
            square_list.append(s)
        return Solution(square_list)

    def random_selection(self, boundaries):
        return _r_.choice(boundaries)
    
    def get_boundaries(self, square):
        return self.problem[square] 

    def pitch_adjustment(self, value, boundaries):
        direction = _r_.choice([1, -1])
        index = boundaries.index(value)
        try: adjusted = boundaries[index+direction]
        except IndexError: adjusted = boundaries[0]
        return adjusted
        
    def improvise(self, times=1):
        for x in range(times):
            self.insert_to_memory(self.new_harmony())
            self.update()


def load_problem(problem_name="veryeasy1", heuristic=True):
    '''Loads a puzzle from the Problem folder.'''

    result = []
    with open("Problems/" + problem_name) as f:
        for line in f:
            result += [int(n) for n in line.rstrip().split("\t")]
    
    return result

