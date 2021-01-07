import time

import pygame

from dinamics.constants import WIDTH, HEIGHT, WHITE
from dinamics.draw import Draw
from dinamics.game import Game
from pgn.pgn_parser import ParsedGame, Move

map_column = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
map_row = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}


class Replay:
    def __init__(self, parsed_game: ParsedGame):
        self.parsed = parsed_game
        self.game = None
        self.WIN = None
        self.draw = None

        self.pause = False
        self.stop = False
        self._need_move = False

        self._move_ms = 750

    def play(self):

        pygame.init()
        game = self.game = Game()

        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        draw = self.draw = Draw(self.WIN, self.game, "../assets")

        clock = pygame.time.Clock()
        count = 0
        finished = False

        self._set_move_timer()
        while True:
            clock.tick(60)

            self._handle_event()

            if self.stop:
                break

            if not self.pause and self._need_move:
                print("Moving....")

                self._set_move_timer()

                move = self.parsed.moves[count]
                start, prom = self._get_move_info(move)
                game.move_piece(start, move.end)

                if prom:
                    game.promote(prom)

                draw.update([])

                self._need_move = False
                count += 1
                if count == len(self.parsed.moves):
                    finished = True
                    break

        if finished:
            pygame.time.wait(3000)

        pygame.quit()

    def _set_move_timer(self):
        pygame.time.set_timer(pygame.USEREVENT, self._move_ms, True)

    def _handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closing the game....")
                self.stop = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pause = not self.pause
                    if not self.pause:
                        print("Game Resumed")
                    else:
                        print("Game Paused")

                elif event.key == pygame.K_1:
                    print("Decreasing speed...")
                    self._move_ms = round(self._move_ms * 2)

                elif event.key == pygame.K_2:
                    print("Increasing speed...")
                    self._move_ms = round(self._move_ms / 2)

            elif event.type == pygame.USEREVENT:
                self._need_move = True

    def _get_move_info(self, move):
        game = self.game

        prom = None
        column = None
        row = None
        if move.type == Move.PROMOTION:
            prom = move.info

        elif move.type == Move.CAPTURE:
            if move.info:
                if move.info in map_column:
                    column = map_column[move.info]
                elif move.info in map_row:
                    row = map_row[move.info]
                else:
                    print(f"Unknown move: {move.text}")

        elif move.type == Move.CASTLING:
            end_row = 7 if game.turn == WHITE else 0
            end_col = map_column[move.info]
            move.end = (end_row, end_col)

        elif move.type == Move.NORMAL:
            if move.info:
                if move.info in map_column:
                    column = map_column[move.info]
                elif move.info in map_row:
                    row = map_row[move.info]
                else:
                    print(f"Unknown move: {move.text}")

        else:
            print(f"Unknown move type: {move.type} for move: {move}")

        # piece_found = None
        start = None
        for (j, k), piece in game.board.get_pieces(valid=True):
            if piece.color != game.turn or piece.__class__ != move.piece:
                continue

            if column and k != column:
                continue

            if row and j != row:
                continue

            moves = game.get_possible_moves((j, k))

            if move.end in moves:
                # piece_found = piece
                start = (j, k)
                break

        if not start:
            print(f"Impossibile trovare il pezzo: {move.piece.__name__}, move: {move} "
                  f"color: {game.turn}, board: {game.board}")
            exit()

        return start, prom
