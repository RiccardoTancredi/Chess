import pygame
from dinamics.piece import Piece
from dinamics.board import Board
from dinamics.constants import *
from dinamics.draw import Draw

FPS = 60 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')


board = Board(WIN)


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    draw = Draw(WIN)
    while run:
        clock.tick(FPS)
        
        # if game.winner() != None:
        #     print(game.winner())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                print(row, col) # we have to add the method
                print(board.get_piece(row, col))
                # game.select(row, col)
        
        draw.update()
    pygame.quit()

main()
        

