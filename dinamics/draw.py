import pygame
from .constants import BLACK, WHITE, SQUARE_SIZE, ROWS, COLS
from .board import Board
from .piece import Piece

class Draw:
    def __init__(self):
        self.board = Board()
    
    def chess_board(self, win):
        win.fill(BLACK)
        self.board.create_board()
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def update(self):
        pygame.display.update()

    def draw(self, win):
        self.chess_board(win)
