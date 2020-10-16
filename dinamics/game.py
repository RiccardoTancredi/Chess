import pygame
from .constants import BLACK, WHITE
from .board import Board
from .piece import Piece
from .draw import Draw

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        # self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Draw()
        self.turn = WHITE
        self.valid_moves = {}
    
    def reset(self):
        self._init()