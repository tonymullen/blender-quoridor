from bge import logic as GL
from Rasterizer import showMouse

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Board:
    """The Quoridor board"""
    cells = [[Cell(x, y ) for x in range(9)] for y in range(9)]
    

if not hasattr(GL, "init"):
    showMouse(1)
    GL.board = Board()
    GL.init = None