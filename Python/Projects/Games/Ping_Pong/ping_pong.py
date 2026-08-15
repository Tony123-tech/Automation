import pygame

pygame.init()

WIDTH, HEIGHT = 700, 800

class Ping_Pong_Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ping Pong Game")
        self.clock = pygame.time.Clock()
        self.font_small = pygame.font.Font(None, 24)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_large = pygame.font.Font(None, 48)
        self.font_xl = pygame.font.Font(None, 64)
        self.font_clock = pygame.font.Font(None, 52)

    def run():
        pass


def main():
    game = Ping_Pong_Game()