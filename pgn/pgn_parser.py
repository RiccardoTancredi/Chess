from dinamics.board import Board
from dinamics.pieces import *


class Move:
    NORMAL = "NORMAL"
    CASTLING = "CASTLING"
    CAPTURE = "CAPTURE"
    EN_PASSANT = "EN_PASSANT"
    PROMOTION = "PROMOTION"

    def __init__(self):
        self.type = Move.NORMAL
        self.end = None
        self.info = None
        self.piece = None
        self.check = False
        self.text = None

    def __repr__(self):
        typ = f"{self.type}, " if self.type != Move.NORMAL else ""
        return f"<Move {typ}{self.piece.__name__}, {self.end}>"


class ParsedGame:
    def __init__(self, info, moves, score):
        self.info = info
        self.moves = moves
        self.score = score

    def __repr__(self):
        return f"<ParsedGame {self.info}>"


class PGNParser:
    def __init__(self):
        self.map_piece = {"K": King, "Q": Queen, "R": Rook, "N": Knight, "B": Bishop, "P": Pawn}
        self.initials = list(self.map_piece.keys())

    def parse_file(self, path, index=None):

        with open(path) as f:
            text = f.read()

        blocks = text.split("\n\n")
        matches = []
        for count in range(0, len(blocks), 2):
            matches.append((blocks[count], blocks[count + 1]))

        parsed_games = []
        for info, moves_text in matches:
            moves_text = moves_text.replace("\n", " ")
            parsed_games.append(self._parse_match(info, moves_text))

        return parsed_games

    def _parse_match(self, info, moves_text):
        moves, score = self._parse_moves(moves_text)
        return ParsedGame(info, moves, score)

    def _parse_moves(self, moves_text: str):

        moves = []
        text = moves_text
        count = 1
        white = True
        while True:
            if white:
                foo = len(str(count)) + 1
                text = text[foo:]
                count += 1

            try:
                text = text.strip()
                move_text, text = text.split(" ", maxsplit=1)

            except ValueError as e:
                score = text.strip()
                break

            moves.append(self._parse_move(move_text))
            white = not white

        return moves, score

    def _parse_move(self, move_text):

        move = Move()
        move.text = move_text

        if "+" in move_text:
            move.check = True
            move_text = move_text[:-1]

        if "O" in move_text:
            move.type = Move.CASTLING
            move.piece = King
            move.info = "g" if move_text.count("-") == 1 else "c"  # colonna
            return move

        elif "x" in move_text:
            move.type = Move.CAPTURE
            first, second = move_text.split("x")

            move.end = _coord_to_move(second)
            if len(first) == 1:
                if first[0] in self.map_piece:
                    move.piece = self.map_piece[first[0]]
                else:
                    move.piece = Pawn
                    move.info = first[0]
            elif len(first) == 2:
                move.piece = self.map_piece[first[0]]
                move.info = first[1]

            else:
                print(f"Unknown capture: {move_text}")

        elif "=" in move_text:
            move.type = Move.PROMOTION
            move.piece = Pawn

            end, piece = move_text.split("=")
            move.end = _coord_to_move(end)
            move.info = self.map_piece[piece]

        elif len(move_text) == 2:
            move.piece = Pawn
            move.end = _coord_to_move(move_text)

        elif len(move_text) == 3:
            if move_text[0] in self.map_piece:
                move.piece = self.map_piece[move_text[0]]
            else:
                move.piece = Pawn
                move.info = move_text[0]
            move.end = _coord_to_move(move_text[1:])

        elif len(move_text) == 4:
            move.end = _coord_to_move(move_text[2:])
            move.info = move_text[1]
            move.piece = self.map_piece[move_text[0]]

        else:
            print(f"Unknown move: {move_text}")

        return move


map_column = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}


def _coord_to_move(coord: str):
    return 8 - int(coord[1]), map_column[coord[0]]


def search_for_piece(piece_cl, column, color, board: Board):
    column = map_column[column]
    for (j, k), piece in board.get_pieces(valid=True):
        if piece.color != color or piece.__class__ != piece_cl:
            continue

        if k == column:
            return (j, k), piece

