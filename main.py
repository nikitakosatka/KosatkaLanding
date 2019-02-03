import pygame
from KosatkaLanding.start_screen import StartGame

pygame.init()
size = width, height = 300, 450
screen = pygame.display.set_mode(size)
pygame.display.set_caption("KosatkaLanding")
running = True
clock = pygame.time.Clock()
start = StartGame(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    start.update()
