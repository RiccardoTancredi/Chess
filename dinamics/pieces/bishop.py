# import pygame
# from dinamics.constants import BLACK_BISHOP, WHITE_BISHOP, BLACK, WHITE
#
# class Bishop:
#     def __init__(self):
#         # self.color = color
#         self.bishop = None
#
#     def bishop_color(self, color):
#         if color == WHITE:
#             self.bishop = WHITE_BISHOP
#         else:
#             self.bishop = BLACK_BISHOP
#         return self.bishop
#
#     def movements(self):
#         pass

from dinamics.piece import Piece
from dinamics.constants import ROWS, COLS

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def get_available_moves(self, position, color):
        self.color = color
        pass

    def get_movements_test(self):
        return [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
                (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
                (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7)]

    def delete_moves(self, board, position, moves):
        for i in range(ROWS):
            for j in range(COLS):
                piece = board.get_piece((i, j))
                if self.color == "WHITE":
                    if piece and  piece.color == "WHITE" and (i, j) in moves:
                        # for col in range(position[0]-column, -1, -1):
                        #     if (col, position[1]) in moves:
                        
                        for l in range(i, ROWS):
                            for k in range(j, COLS):
                                # if (position[0] - l, position[1] - k) in moves:
                                #     moves.remove((position[0] - l, position[1] - k))
                                # if (position[0] - l, position[1] + k) in moves:
                                #     moves.remove((position[0] - l, position[1] + k)) 
                                if (l, k) in moves:  
                                    moves.remove((l, k))   
                else:
                    if self.color == "BLACK":
                            # for col in range(position[0]+column, ROWS):
                            #     if (col, position[1]) in moves:
                        if piece and (i, j) in moves: #and piece.color == "BLACK"
                            if j < position[1] and i > position[0]:
                                for l in range(i, ROWS):
                                    for k in range(j):
                                        if (l, k) in moves:  
                                            moves.remove((l, k))  
                            elif j > position[1] and i < position[0]:
                                for l in range(i):
                                    for k in range(j, COLS):
                                        if (l, k) in moves:  
                                            moves.remove((l, k)) 
                            elif  j < position[1] and i < position[0]:
                                for l in range(i):
                                    for k in range(j):
                                        if (l, k) in moves:  
                                            moves.remove((l, k)) 
                            elif j > position[1] and i > position[0]:
                                for l in range(i, ROWS):
                                    for k in range(j, ROWS):
                                        if (l, k) in moves:  
                                            moves.remove((l, k)) 


                                            #To be continue
                                
        return moves

    def eat_piece(self, board, position, moves):
        return moves
