class Move:
    """
    Class responsible for storing a move on the grid
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.number = 0  # number = 0 => move hasn't been done yet

    def __str__(self):
        return str("[{0}, {1}, {2}]".format(self.x, self.y, self.number))



