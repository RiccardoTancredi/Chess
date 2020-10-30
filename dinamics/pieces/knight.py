# import pygame
# from dinamics.constants import BLACK_KNIGHT, WHITE_KNIGHT, BLACK, WHITE
#
# class Knight:
#     def __init__(self):
#         # self.color = color
#         self.knight = None
#
#     def knight_color(self, color):
#         if color == WHITE:
#             self.knight = WHITE_KNIGHT
#         else:
#             self.knight = BLACK_KNIGHT
#         return self.knight
#
#     def movements(self):
#         pass

from dinamics.piece import Piece


class Knight(Piece):
    def get_available_moves(self, position):
        return [(0, 0)]  # todo

    def get_movements_test(self):
        return [(1, 2), (2, 1), (-1, 2), (-2, 1),       # le 4 possibili L (se sono in (0,0))
                (-1, -2), (-2, -1), (1, -2), (2, -1)]

    def delete_moves(self, board, position, moves):
        pass

    def eat_piece(self, board, position, moves):
        pass
