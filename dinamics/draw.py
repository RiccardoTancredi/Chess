import pygame
from pygame import Rect
from pygame.transform import scale

from .pieces.bishop import Bishop
from .pieces.king import King
from .pieces.knight import Knight
from .pieces.pawn import Pawn
from .constants import BLACK, WHITE, SQUARE_SIZE, ROWS, COLS, HEIGHT, WIDTH
from .pieces.queen import Queen
from .pieces.rook import Rook

C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_BLUE = (0, 0, 255)


class Draw:
    def __init__(self, win, game, assets_dir):
        self.win = win
        self.board = game.board
        self.scale_factor = (int(WIDTH * 50 / 400), int(HEIGHT * 50 / 400))

        self.white_pieces = {
            Pawn: scale(pygame.image.load(f'{assets_dir}/white_pawn.png'), self.scale_factor),
            Knight: scale(pygame.image.load(f'{assets_dir}/white_knight.png'), self.scale_factor),
            King: scale(pygame.image.load(f'{assets_dir}/white_king.png'), self.scale_factor),
            Queen: scale(pygame.image.load(f'{assets_dir}/white_queen.png'), self.scale_factor),
            Rook: scale(pygame.image.load(f'{assets_dir}/white_rook.png'), self.scale_factor),
            Bishop: scale(pygame.image.load(f'{assets_dir}/white_bishop.png'), self.scale_factor)
        }
        self.black_pieces = {
            Pawn: scale(pygame.image.load(f'{assets_dir}/black_pawn.png'), self.scale_factor),
            Knight: scale(pygame.image.load(f'{assets_dir}/black_knight.png'), self.scale_factor),
            King: scale(pygame.image.load(f'{assets_dir}/black_king.png'), self.scale_factor),
            Queen: scale(pygame.image.load(f'{assets_dir}/black_queen.png'), self.scale_factor),
            Rook: scale(pygame.image.load(f'{assets_dir}/black_rook.png'), self.scale_factor),
            Bishop: scale(pygame.image.load(f'{assets_dir}/black_bishop.png'), self.scale_factor)
        }

        self.prom_rects = {}

    def update(self, moves=None, promotion=False):
        if not moves:
            moves = []

        self.draw_squares()
        self.draw_pieces()
        self.draw_valid_moves(moves)
        if promotion:
            piece = self.board.get_piece(promotion)
            self.draw_promotion(piece.color)
        pygame.display.update()

    def draw_squares(self):
        self.win.fill(C_BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(self.win, C_WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self):
        for (row, col), piece in self.board.get_pieces(valid=True):
            self.draw_piece(piece.__class__, piece.color, col * SQUARE_SIZE, row * SQUARE_SIZE)

    def draw_piece(self, clss, color, x, y):
        image = None
        if color == WHITE:
            image = self.white_pieces[clss]
        elif color == BLACK:
            image = self.black_pieces[clss]

        return self.win.blit(image, (x, y))

    def draw_promotion(self, color):
        height = 100
        starty = (HEIGHT - height) / 2
        pygame.draw.rect(self.win, C_BLUE, Rect((0, starty), (WIDTH, height)))

        y_margin = (height - SQUARE_SIZE) / 2
        spacing = 30
        x_margin = (WIDTH - SQUARE_SIZE * 4 - spacing * 3) / 2
        for count, clss in enumerate([Queen, Rook, Bishop, Knight]):
            x = x_margin + count * (SQUARE_SIZE + spacing)
            image_rect = self.draw_piece(clss, color, x, starty + y_margin)
            self.prom_rects[clss] = image_rect

    def draw_valid_moves(self, moves):
        for (row, col) in moves:
            position = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            pygame.draw.circle(self.win, C_BLUE, position, 10)

    def choose_promotion(self, x, y):
        choosen = None
        # Dato che ho salvato i rettangoli delle immagini, posso controllare se questi rettangoli sono stati cliccati
        for clss, rect in self.prom_rects.items():  # Per ogni classe e rettangolo associato
            if rect.collidepoint(x, y):
                self.prom_rects.clear()
                choosen = clss
                break

        return choosen
