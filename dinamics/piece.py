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
