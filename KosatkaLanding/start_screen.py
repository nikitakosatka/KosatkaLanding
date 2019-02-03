import pygame
from .other import load_image


class StartGame:
    def __init__(self, screen):
        self.start = False
        self.screen = screen
        self.fps = 30
        self.background = load_image("background.jpg")

    def update(self):
        for event in pygame.event.get():
            if event.type in (pygame.MOUSEBUTTONUP, pygame.KEYUP):
                self.start = True
            elif event.type == pygame.QUIT:
                pygame.quit()

        if not self.start:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()