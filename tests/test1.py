import unittest

from dinamics.board import Board
from dinamics.constants import BLACK, WHITE, ROWS, COLS
from dinamics.game import Game
from dinamics.pieces import *


class TestCastlingBasic(unittest.TestCase):
    # Esegue questo codice prima di ogni test, quindi mi prepara la board e il game
    def setUp(self):
        self.board = Board()
        self.game = Game(board=self.board)

    def test_castling_black_long(self):
        board, game = self.board, self.game  # variabili più corte
        board.put((0, 0), clss=Rook, color=BLACK)  # metto la torre in 1, 1
        board.put((0, 4), clss=King, color=BLACK)  # metto il re in 1, 5
        game.initialize()
        moves = game.get_possible_moves((0, 4))  # prendo le mosse possibili del re
        # controllo che l'arrocco sia fra le mosse, se non lo è da errore
        self.assertIn((0, 2), moves)

        game.change_turn()  # sto testando i neri, quindi devo passare il turno
        game.move_piece((0, 4), (0, 2), check=False)
        # controllo che la torre si sia spostata
        self.assertEqual(board.get_piece((0, 3)).__class__, Rook)

    # gli altri tre casi
    def test_castling_black_short(self):
        board, game = self.board, self.game
        board.put((0, 7), clss=Rook, color=BLACK)
        board.put((0, 4), clss=King, color=BLACK)
        game.initialize()
        moves = game.get_possible_moves((0, 4))
        self.assertIn((0, 6), moves)

        game.change_turn()
        game.move_piece((0, 4), (0, 6), check=False)
        self.assertEqual(board.get_piece((0, 5)).__class__, Rook)

    def test_castling_white_long(self):
        board, game = self.board, self.game
        board.put((7, 0), clss=Rook, color=WHITE)
        board.put((7, 4), clss=King, color=WHITE)
        game.initialize()
        moves = game.get_possible_moves((7, 4))
        self.assertIn((7, 2), moves)

        game.move_piece((7, 4), (7, 2), check=False)
        self.assertEqual(board.get_piece((7, 3)).__class__, Rook)

    def test_castling_white_short(self):
        board, game = self.board, self.game
        board.put((7, 7), clss=Rook, color=BLACK)
        board.put((7, 4), clss=King, color=BLACK)
        game.initialize()
        moves = game.get_possible_moves((7, 4))
        self.assertIn((7, 6), moves)

        game.change_turn()
        game.move_piece((7, 4), (0, 6), check=False)
        self.assertEqual(board.get_piece((7, 5)).__class__, Rook)


class TestCastlingAdvanced(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game = Game(board=self.board)

    def test_cannot_castling_path_blocked(self):
        board, game = self.board, self.game
        board.put((0, 7), clss=Rook, color=BLACK)
        board.put((0, 4), clss=King, color=BLACK)
        board.put((4, 6), clss=Rook, color=WHITE)
        game.initialize()
        moves = game.get_possible_moves((0, 4))
        self.assertNotIn((0, 6), moves)

    def test_cannot_castling_rook_blocked(self):
        board, game = self.board, self.game
        board.put((0, 7), clss=Rook, color=BLACK)
        board.put((0, 4), clss=King, color=BLACK)
        board.put((4, 7), clss=Rook, color=WHITE)
        game.initialize()
        moves = game.get_possible_moves((0, 4))
        self.assertNotIn((0, 6), moves)


class TestRookMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game = Game(board=self.board)

    def test_rook_path_blocked_allies(self):
        board, game = self.board, self.game
        board.put((3, 3), clss=Rook, color=WHITE)
        board.put((3, 4), clss=Pawn, color=WHITE)
        board.put((3, 2), clss=Pawn, color=WHITE)
        board.put((2, 3), clss=Pawn, color=WHITE)
        board.put((4, 3), clss=Pawn, color=WHITE)
        moves = game.get_possible_moves((3, 3))
        self.assertEqual(len(moves), 0)

    def test_rook_path_blocked_enemies(self):
        board, game = self.board, self.game
        board.put((3, 3), clss=Rook, color=WHITE)
        board.put((3, 4), clss=Pawn, color=BLACK)
        board.put((3, 2), clss=Pawn, color=BLACK)
        board.put((2, 3), clss=Pawn, color=BLACK)
        board.put((4, 3), clss=Pawn, color=BLACK)
        moves = game.get_possible_moves((3, 3))
        self.assertIn((3, 4), moves)
        self.assertIn((3, 2), moves)
        self.assertIn((2, 3), moves)
        self.assertIn((4, 3), moves)
        self.assertEqual(len(moves), 4)

    def test_rook_path(self):
        board, game = self.board, self.game
        board.put((3, 3), clss=Rook, color=WHITE)
        moves = game.get_possible_moves((3, 3))
        for i in range(ROWS):
            if i == 3:
                continue
            self.assertIn((i, 3), moves)
        for i in range(COLS):
            if i == 3:
                continue
            self.assertIn((3, i), moves)


class TestEnPassant(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game = Game(board=self.board)

    def test_en_passant_white(self):
        board, game = self.board, self.game
        board.put((1, 0), clss=Pawn, color=BLACK)
        board.put((4, 1), clss=Pawn, color=WHITE)
        game.move_piece((4, 1), (3, 1))
        game.move_piece((1, 0), (3, 0))
        moves = game.get_possible_moves((3, 1))
        self.assertIn((2, 0), moves)
        game.move_piece((3, 1), (2, 0))
        self.assertIsNone(self.board.get_piece((3, 0)))

    def test_en_passant_black(self):
        board, game = self.board, self.game
        board.put((3, 2), clss=Pawn, color=BLACK)
        board.put((6, 1), clss=Pawn, color=WHITE)
        game.change_turn()
        game.move_piece((3, 2), (4, 2))
        game.move_piece((6, 1), (4, 1))
        moves = game.get_possible_moves((4, 2))
        self.assertIn((5, 1), moves)
        game.move_piece((4, 2), (5, 1))
        self.assertIsNone(self.board.get_piece((4, 1)))


def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCastlingBasic("Test Basic Castling"))
    suite.addTest(TestCastlingAdvanced("Test Advanced Castling"))
    suite.addTest(TestRookMoves("Test Rook Moves"))
    suite.addTest(TestEnPassant("Test En Passant"))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_suite())
