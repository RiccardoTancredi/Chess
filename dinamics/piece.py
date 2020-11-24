from dinamics.constants import BLACK


class Piece:

    def __init__(self, color):
        self.color = color
        self.moves_history = []

    # using x, y axes
    def get_movements(self):
        return []

    def after_move(self, start, end):
        self.moves_history.append(end)

    def edit_moves(self, board, position, moves):
        return moves

    def side_effects(self, board, start, end):
        # se una mossa ha altri effetti oltre a catturare le pedina (se si muove su una casella occupata)
        # qui è il metodo per "fare" gli effetti. Tipo arrocco ed en passant
        pass

    def __repr__(self) -> str:
        color = "black" if self.color == BLACK else "white"
        return f"<{self.__class__.__name__} {color}>"
