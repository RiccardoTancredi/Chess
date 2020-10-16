import pygame
from dinamics.constants import BLACK_BISHOP, WHITE_BISHOP, BLACK, WHITE

class Bishop:
    def __init__(self):
        # self.color = color
        self.bishop = None
        
    def pawn_color(self, color):
        if color == WHITE:
            self.bishop = WHITE_BISHOP
        else:
            self.bishop = BLACK_BISHOP
        return self.bishop

    def movements(self):
        pass