import pygame
from pygame import Rect
from pygame.transform import scale

from .game import Game
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
    def __init__(self, window, game, assets_dir):
        self.window = window
        self.board = game.board
        self.game = game
        self.scale_factor = (int(WIDTH * 50 / 400), int(HEIGHT * 50 / 400))
        pygame.font.init()
        self.font = pygame.font.SysFont("monospace", 100)

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

    def update(self, moves=None):
        if not moves:
            moves = []

        self.draw_squares()
        self.draw_effects()
        self.draw_pieces()
        self.draw_valid_moves(moves)
        if self.game.status == Game.CHECKMATE:
            self.draw_checkmate(self.game.checkmate)

        elif self.game.status == Game.DRAW:
            self.draw_draw()

        elif self.game.need_promotion:
            piece = self.board.get_piece(self.game.need_promotion)
            self.draw_promotion(piece.color)

        pygame.display.update()

    def draw_squares(self):
        self.window.fill(C_BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                self.draw_square((row, col), C_WHITE)

    def draw_square(self, pos, color):
        x = SQUARE_SIZE * pos[1]
        y = SQUARE_SIZE * pos[0]
        side = SQUARE_SIZE
        pygame.draw.rect(self.window, color, (x, y, side, side))

    def draw_effects(self):
        checks = self.game.under_check_moves
        for color, (king_pos, moves) in checks.items():
            if moves:
                self.draw_square(king_pos, (255, 0, 0))
                for move in moves:
                    self.draw_square(move, (180, 0, 0))

    def draw_pieces(self):
        for (row, col), piece in self.board.get_pieces(valid=True):
            self.draw_piece(piece.__class__, piece.color, col * SQUARE_SIZE, row * SQUARE_SIZE)

    def draw_piece(self, clss, color, x, y):
        image = None
        if color == WHITE:
            image = self.white_pieces[clss]
        elif color == BLACK:
            image = self.black_pieces[clss]

        return self.window.blit(image, (x, y))

    def draw_promotion(self, color):
        height = 100
        starty = (HEIGHT - height) / 2
        pygame.draw.rect(self.window, C_BLUE, Rect((0, starty), (WIDTH, height)))

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
            pygame.draw.circle(self.window, C_BLUE, position, 10)

    def draw_checkmate(self, winner):
        height = 200
        starty = (HEIGHT - height) / 2
        pygame.draw.rect(self.window, C_BLUE, Rect((0, starty), (WIDTH, height)))

        y_margin = (height - SQUARE_SIZE) / 2
        self.draw_piece(King, winner, WIDTH / 8, starty + y_margin)
        color = C_BLACK if winner == BLACK else C_WHITE

        label = self.font.render("VINCE", 2, color)  # 2 = antialiasing
        y_label = (height - label.get_size()[1]) / 2
        x_label = (WIDTH - label.get_size()[0] - 50) / 2 + SQUARE_SIZE
        self.window.blit(label, (x_label, starty + y_label))

    def draw_draw(self):
        height = 200
        starty = (HEIGHT - height) / 2
        pygame.draw.rect(self.window, C_BLUE, Rect((0, starty), (WIDTH, height)))
        label = self.font.render("PATTA", 2, C_WHITE)  # 2 = antialiasing
        y_label = (height - label.get_size()[1]) / 2
        x_label = (WIDTH - label.get_size()[0]) / 2
        self.window.blit(label, (x_label, starty + y_label))

    def choose_promotion(self, x, y):
        choosen = None
        # Dato che ho salvato i rettangoli delle immagini, posso controllare se questi rettangoli sono stati cliccati
        for clss, rect in self.prom_rects.items():  # Per ogni classe e rettangolo associato
            if rect.collidepoint(x, y):
                self.prom_rects.clear()
                choosen = clss
                break

        return choosen
