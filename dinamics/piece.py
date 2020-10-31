# import pygame


# from .pieces.Pawn import Pawn
# from .pieces.King import King
# from .pieces.Queen import Queen
# from .pieces.Bishop import Bishop
# from .pieces.Knight import Knight
# from .pieces.Rook import Rook


# class Piece:
#     def __init__(self, row, col, color, name, win):
#         self.row = row
#         self.col = col
#         self.color = color
#         # self.promotion = ["Queen", ""] this should work only for pawns
#         self.x = 0
#         self.y = 0
#         self.win = win
#         # self.calc_pos(self.win)
#         self.name = name
#
#     # def calc_pos(self):
#     #     self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
#     #     self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
#
#     def select_piece(self):
#         if self.name == "Pawn":
#             self.name = Pawn().pawn_color(self.color)
#             # self.name = Pawn(self.color)
#
#         if self.name == "King":
#             self.name = King().king_color(self.color)
#
#         elif self.name == "Queen":
#             self.name = Queen().queen_color(self.color)
#
#         elif self.name == "Rook":
#             self.name = Rook().rook_color(self.color)
#
#         elif self.name == "Bishop":
#             self.name = Bishop().bishop_color(self.color)
#
#         elif self.name == "Knight":
#             self.name = Knight().knight_color(self.color)
#
#         else:
#             pass
#         return self.name
#
#     # This method is only for drawing a smaller squares on which we have to put the image of the piece
#     # def draw(self, win):
#     #     dimension = SQUARE_SIZE//2 - 10
#     #     pygame.draw.rect(win, GREY, (row*SQUARE_SIZE + 2, col*SQUARE_SIZE + 2, dimension, dimension))
#
#     def move(self, row, col):
#         self.row = row
#         self.col = col
#         # self.calc_pos()
#
#     def __repr__(self):
#         return str(self.color)

class Piece:

    def __init__(self, color):
        self.color = color

    # position is a tuple: (row, column) with the current position
    # return a collection of tuples ex: [(1, 2), (1, 3)]
    def get_available_moves(self, position, color):
        # self. board = Board()
        # This is like the default implementation: if this function is not implemented
        # in the subclasses this function will be called (but we decided to throw an error)
        # So we are saying: if you subclass this class, you must implement this method!
        raise NotImplementedError

    # using x, y axes
    def get_movements_test(self):
        return []

    def on_move(self, start, end):
        pass

    def delete_moves(self, board, position, moves):

        raise NotImplementedError

    def eat_piece(self, board, position, moves):
        pass    

    def under_check(self):
        # here we have to check if the king is under attack. How?
        # A possible solution could be, every move, to see if the moves of each one of the opponent's pieces have the king position as a possible move
        # Computationally this is too expensive, IS think. So what?

        # ToDO

        pass

    def check(self):
        # in this method we see if a piece has made a check or maybe a checkmate. 
        # here we check if the king position is in the possible moves the piece can do. In that case we want the oppont to cancel the check, by moving the king or
        # by eating the piece which is doing check. This method could replace the method before (under_check) 

        # This method must be called after every move
 
        # Furthermore, in game.py, we want the oppont to do something (eating the piece, moving the king...) in order to not do an irregular move.
        
        pass
