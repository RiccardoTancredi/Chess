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
    selected = None
    moves = []
    while run:
        clock.tick(FPS)
        turn = game.turn

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                raw_pos = pygame.mouse.get_pos()
                pos = get_row_col_from_mouse(raw_pos)
                # print(pos)
                if selected and pos in moves:
                    if piece and piece.color == turn:
                        game.move_piece(selected, pos, check=False)
                        selected = None
                        moves = []
                    else:
                        print("This is not yout turn. Wait until the opponent has moved")

                else:
                    selected = pos
                    moves = game.get_possible_moves(selected)
                    piece = game.board.get_piece(selected)
                    if piece and piece.color == turn:
                        if piece:
                            print(f"Selected {piece.__class__.__name__} in {pos}")
                        if moves:
                            draw.draw_valid_moves(moves)
                    else:
                        break

        draw.draw()
        draw.update(moves)    
         
    pygame.quit()

     
main()

print(game.notation)