import pygame

from dinamics.game import Game
from dinamics.piece import Piece
from dinamics.board import Board
from dinamics.constants import *
from dinamics.draw import Draw

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')


# board = Board(WIN)


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


game = Game()
draw = Draw(WIN, game, "./assets")


def main():
    run = True
    clock = pygame.time.Clock()
    moves = []
    # draw = Draw(WIN)
    while run:
        clock.tick(FPS)

        # if game.winner() != None:
        #     print(game.winner())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and moves:
                new_pos = get_row_col_from_mouse(pygame.mouse.get_pos())
                if new_pos in moves:
                    game.move_piece(chess_pos, moves[0], piece.color)
                    print("Here we go. I'm moving it")
                    print(chess_pos)
                    moves = []
                else:
                    moves = []

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                chess_pos = get_row_col_from_mouse(pos)
                print(chess_pos)
                piece = game.board.get_piece(chess_pos)
                if piece:
                    moves = piece.get_available_moves(chess_pos, piece.color)
                    draw.draw_valid_moves(moves)
                    # print(moves)
                # if event.type == pygame.MOUSEBUTTONDOWN:
                    # new_pos = get_row_col_from_mouse(pygame.mouse.get_pos())
                    # print(new_pos)
                    # if new_pos in moves:
                # game.move_piece(chess_pos, moves[0], piece.color)
                # print("Here we go. I'm moving it")
                # print(chess_pos)

        draw.draw()
        draw.update(moves)
    pygame.quit()


main()
