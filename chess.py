import pygame
from dinamics.piece import Piece
from dinamics.board import Board
from dinamics.constants import *
from dinamics.draw import Draw

FPS = 60 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

def main():
    run = True
    clock = pygame.time.Clock()
    # game = Game(WIN)
    draw_chess_board = Draw()
    draw_chess_board.draw(WIN)
    while run:
        clock.tick(FPS)
        
        # if game.winner() != None:
        #     print(game.winner())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        #         pos = pygame.mouse.get_pos()
        #         row, col = get_row_col_from_mouse(pos)
        #         game.select(row, col)
        
        # game.update()
    pygame.quit()

main()
        

