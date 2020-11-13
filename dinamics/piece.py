from dinamics.constants import BLACK


class Piece:

    def __init__(self, color):
        self.color = color
        self.moves_history = []

    # using x, y axes
    def get_movements(self):
        return []

    def on_move(self, start, end):
        self.moves_history.append(end)

    def edit_moves(self, board, position, moves):
        return moves

    # def delete_moves(self, board, position, moves):
    #     return moves
    #
    # def add_moves(self, board, position, moves):
    #     return moves

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

    def __repr__(self) -> str:
        color = "black" if self.color == BLACK else "white"
        return f"<{self.__class__.__name__} {color}>"


