import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS 

#rgb
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

scale_factor = (int(WIDTH*50/400), int(HEIGHT*50/400))

#Black Pieces
BLACK_KING = pygame.transform.scale(pygame.image.load('assets/black_king.png'), scale_factor)
BLACK_QUEEN = pygame.transform.scale(pygame.image.load('assets/black_queen.png'), scale_factor)
BLACK_ROOK = pygame.transform.scale(pygame.image.load('assets/black_rook.png'), scale_factor)
BLACK_BISHOP = pygame.transform.scale(pygame.image.load('assets/black_bishop.png'), scale_factor)
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load('assets/black_knight.png'), scale_factor)
BLACK_PAWN = pygame.transform.scale(pygame.image.load('assets/black_pawn.png'), scale_factor)

BLACK_PIECES = [BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING, BLACK_BISHOP, BLACK_KNIGHT, BLACK_ROOK, BLACK_PAWN]

#White Pieces
WHITE_KING = pygame.transform.scale(pygame.image.load('assets/white_king.png'), scale_factor)
WHITE_QUEEN = pygame.transform.scale(pygame.image.load('assets/white_queen.png'), scale_factor)
WHITE_ROOK = pygame.transform.scale(pygame.image.load('assets/white_rook.png'), scale_factor)
WHITE_BISHOP = pygame.transform.scale(pygame.image.load('assets/white_bishop.png'), scale_factor)
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load('assets/white_knight.png'), scale_factor)
WHITE_PAWN = pygame.transform.scale(pygame.image.load('assets/white_pawn.png'), scale_factor)


WHITE_PIECES = [WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING, WHITE_BISHOP, WHITE_KNIGHT, WHITE_ROOK, WHITE_PAWN]