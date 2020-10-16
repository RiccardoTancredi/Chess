import pygame
from .constants import *

class Board:
    def __init__(self):
        self.board = []
        self.create_board()

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                # here we have to add the initial configuration of the chess board
                # so we have to define first the piece class and all the pieces classes:
                # Pieces = King, Queen, Rook, Bishop, Knight, Pawn
                pass