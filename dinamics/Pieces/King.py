import pygame
from dinamics.constants import BLACK_KING, WHITE_KING, BLACK, WHITE

class King:
    def __init__(self):
        # self.color = color
        self.king = None
        
    def king_color(self, color):
        if color == WHITE:
            self.king = WHITE_KING
        else:
            self.king = BLACK_KING
        return self.king

    def movements(self):
        pass