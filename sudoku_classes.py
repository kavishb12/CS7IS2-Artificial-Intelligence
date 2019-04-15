#coding: utf-8

from math import sqrt

class Grid(object):

    def __init__(self, numbers):
        self.numbers = numbers
        self.locked = [n for n in range(len(self.numbers)) if self.numbers[n] in [1,2,3,4,5,6,7,8,9]]
        
    def __repr__(self):
        return "\n".join(str(self.get_line(x)) for x in range(9))
        
    def get_line(self, index):
        if index > 8: return None
        return self.numbers[index*9:index*9+9]
        
    def get_box(self, index):
        if index > 8: return None
        if index < 3:
            box = self.numbers[index*3:index*3+3]
            box += self.numbers[index*3+9:index*3+12]
            box += self.numbers[index*3+18:index*3+21]
        elif index < 6:
            box = self.numbers[index*3+18:index*3+3+18]
            box += self.numbers[index*3+9+18:index*3+12+18]
            box += self.numbers[index*3+18+18:index*3+21+18]
        else:
            box = self.numbers[index*3+36:index*3+3+36]
            box += self.numbers[index*3+9+36:index*3+12+36]
            box += self.numbers[index*3+18+36:index*3+21+36]
        return box
        
    def get_column(self, index):
        if index > 8: return None
        column = [self.numbers[n] for n in range(index, 81, 9)]
        return column
        
    def get_lines(self):
        return [self.get_line(x) for x in range(9)]
        
    def get_boxes(self):
        return [self.get_box(x) for x in range(9)]
        
    def get_columns(self):
        return [self.get_column(x) for x in range(9)]
        
    def get_all_subgrids(self):
        return self.get_lines() + self.get_boxes() + self.get_columns()
        
    def sub_eval(self, subgrid):
        # res = sqrt((sum(subgrid) - 45)**2)
        res = sum([subgrid.count(n) for n in subgrid if subgrid.count(n) > 1])
        # res = sum([1 for n in subgrid if subgrid.count(n) > 1])
        return res
        
    def evaluate(self):
        return sum([self.sub_eval(x) for x in self.get_all_subgrids()])
        
    def possibilities(self, square):
        if type(square) == tuple: square = 9*square[0]+square[1]
        if square in self.locked and type(self.numbers[square]) == int: return [self.numbers[square]]
        if type(self.numbers[square]) == list:
            if len(self.numbers[square]) == 1: return self.numbers[square]
            return [n for n in self.numbers[square] if n not in self.sqs_subs(square)]
        
        return [n for n in range(10) if n not in self.sqs_subs(square)]
        
    def in_which_line(self, square):
        return int(square / 9)
        
    def in_which_column(self, square):
        return square % 9
        
    def in_which_box(self, square):
        arrow = [[0]*3+[1]*3+[2]*3]*3+[[3]*3+[4]*3+[5]*3]*3
        arrow += [[6]*3+[7]*3+[8]*3]*3
        return arrow[self.in_which_line(square)][self.in_which_column(square)]
        
    def sqs_subs(self, square):
        if type(self.numbers[0]) != list: 
            all_three = self.get_box(self.in_which_box(square))
            all_three += self.get_line(self.in_which_line(square))
            all_three += self.get_column(self.in_which_column(square))
        else:
            all_three = [y[0] for y in self.get_box(self.in_which_box(square)) if len(y) == 1]
            all_three += [y[0] for y in self.get_line(self.in_which_line(square)) if len(y) == 1]
            all_three += [y[0] for y in self.get_column(self.in_which_column(square)) if len(y) == 1]
            
        return all_three
        
    def get_problem(self):
        return [self.possibilities(n) for n in range(81)]
        
    def constraint_propagation(self):
        while True:
            before = self.numbers.copy()
            self.numbers = self.get_problem()
            if len([x for y in self.numbers for x in y]) == 81: break
            if before == self.numbers: break
        return self.numbers
            
    
class Solution(Grid):

    def __init__(self, solution):
        Grid.__init__(self, solution)
        
        