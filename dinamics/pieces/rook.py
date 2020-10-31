# import pygame
# from dinamics.constants import BLACK_ROOK, WHITE_ROOK, BLACK, WHITE
#
# class Rook:
#     def __init__(self):
#         # self.color = color
#         self.rook = None
#
#     def rook_color(self, color):
#         if color == WHITE:
#             self.rook = WHITE_ROOK
#         else:
#             self.rook = BLACK_ROOK
#         return self.rook
#
#     def movements(self):
#         pass

from dinamics.piece import Piece
from dinamics.constants import ROWS, COLS

class Rook(Piece):
    def get_available_moves(self, position):
        pass

    def get_movements_test(self):
        basic_moves = []
        for j in range(-COLS+1, COLS):
            basic_moves.append((0, j))
        for i in range(-ROWS+1, ROWS):
                basic_moves.append((i, 0))
        return basic_moves

    def delete_moves(self, board, position, moves):

        #Partially Working

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         piece = board.get_piece((i, j))
        #         if piece and (i, j) in moves: 
        #             if self.color == "BLACK":
        #                 if piece.color == self.color:
        #                     if i == position[0]:
        #                         for l in range(j, COLS):
        #                             if (i, l) in moves:
        #                                 moves.remove((i, l))
        #                     elif j == position[1]:
        #                         for k in range(i, ROWS):
        #                             if (k, j) in moves:
        #                                 moves.remove((k, j))
                                
        #                 elif piece.color != self.color:
        #                     if i == position[0]:
        #                         for l in range(j+1, COLS):
        #                             if (i, l) in moves:
        #                                 moves.remove((i, l))
        #                     elif j == position[1]:
        #                         for k in range(i+1, ROWS):
        #                             if (k, j) in moves:
        #                                 moves.remove((k, j))

        #             if self.color == "WHITE":
        #                 if piece.color == self.color:
        #                     if i == position[0]:
        #                         for l in range(j, -1, -1):
        #                             if (i, l) in moves:
        #                                 moves.remove((i, l))
        #                     elif j == position[1]:
        #                         for k in range(i, -1, -1):
        #                             if (k, j) in moves:
        #                                 moves.remove((k, j))
                                
        #                 elif piece.color != self.color:
        #                     if i == position[0]:
        #                         for l in range(j-1, -1):
        #                             if (i, l) in moves:
        #                                 moves.remove((i, l))
        #                     elif j == position[1]:
        #                         for k in range(i-1, -1):
        #                             if (k, j) in moves:
        #                                 moves.remove((k, j))

        return moves

    def eat_piece(self, board, position, moves):
        return moves

