import pygame
from dinamics.constants import BLACK_QUEEN, WHITE_QUEEN, BLACK, WHITE

class Queen:
    def __init__(self):
        # self.color = color
        self.queen = None
        
    def pawn_color(self, color):
        if color == WHITE:
            self.queen = WHITE_QUEEN
        else:
            self.queen = BLACK_QUEEN
        return self.queen

    def movements(self):
        pass