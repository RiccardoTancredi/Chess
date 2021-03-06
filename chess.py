import pygame

from dinamics.game import Game
from dinamics.piece import Piece
from dinamics.board import Board, TestBoard, DrawBoard
from dinamics.constants import *
from dinamics.draw import Draw
from latex import *

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')



def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


# game = Game(board=DrawBoard())
game = Game()
draw = Draw(WIN, game, "./assets")

latex_file_name = game.latex_file_name

def main():
    run = True
    clock = pygame.time.Clock()
    selected = None
    moves = []

    while run:
        clock.tick(FPS)
        turn = game.turn

        draw.update(moves)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if game.status != Game.PLAYING:
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                raw_pos = pygame.mouse.get_pos()

                if game.need_promotion:
                    # ritorna la classe di quello che il pedone diventerà (se il click è invalido non fa nulla)
                    clss = draw.choose_promotion(raw_pos[0], raw_pos[1])
                    if clss:
                        game.promote(clss)

                else:
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

    pygame.quit()


main()

print(game.notation)
doc = game.doc
# end_doc = latex_end(latex_file_name)
# PDF = convert_to_PDF(doc, "Chess_Game")