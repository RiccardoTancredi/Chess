import pygame
from dinamics.constants import BLACK_PAWN, WHITE_PAWN, BLACK, WHITE
class Pawn:
    def __init__(self):
        # self.color = color
        self.pawn = None
        
    def pawn_color(self, color):
        if color == WHITE:
            self.pawn = WHITE_PAWN
        else:
            self.pawn = BLACK_PAWN
        return self.pawn

    def movements(self):
        pass

    # def make_king(self):
    #     self.king = True