import pygame
from .constants import BLACK, WHITE, SQUARE_SIZE, ROWS, COLS
from .board import Board
from .piece import Piece

class Draw:
    def __init__(self, win):
        self.board = Board()
        self.win = win
        
    def squares(self):
        self.win.fill(BLACK)
        self.board.create_board()
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(self.win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def update(self):
        self.draw()
        pygame.display.update()

    def draw(self):
        self.squares()

    def draw_pieces(self):
        # here we have to call a method from the pieces class
        pass