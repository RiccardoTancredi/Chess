import pygame
from .constants import SQUARE_SIZE, WHITE, BLACK, ROWS, COLS, GREY
from .Pieces.Pawn import Pawn
from .Pieces.King import King
from .Pieces.Queen import Queen 
from .Pieces.Bishop import Bishop
from .Pieces.Knight import Knight
from .Pieces.Rook import Rook 

class Piece:
    def __init__(self, row, col, color, name, win):
        self.row = row
        self.col = col
        self.color = color 
        # self.promotion = ["Queen", ""] this should work only for pawns
        self.x = 0
        self.y = 0
        self.win = win
        # self.calc_pos(self.win)
        self.name = name

    # def calc_pos(self):
    #     self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
    #     self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def select_piece(self):
        if self.name == "Pawn":
            self.name = Pawn().pawn_color(self.color)
    
        elif self.name == "King":
            self.name = King().king_color(self.color)

        elif self.name == "Queen":
            self.name = Queen().queen_color(self.color)
        
        elif self.name == "Rook":
            self.name = Rook().rook_color(self.color)
        
        elif self.name == "Bishop":
            self.name = Bishop().bishop_color(self.color)

        elif self.name == "Knight":
            self.name = Knight().knight_color(self.color)

        else:
            pass
        return self.name


    #This method is only for drawing a smaller squares on which we have to put the image of the piece
    # def draw(self, win):
    #     dimension = SQUARE_SIZE//2 - 10
    #     pygame.draw.rect(win, GREY, (row*SQUARE_SIZE + 2, col*SQUARE_SIZE + 2, dimension, dimension))

    def move(self, row, col):
        self.row = row
        self.col = col
        # self.calc_pos()

    def __repr__(self):
        return str(self.color)