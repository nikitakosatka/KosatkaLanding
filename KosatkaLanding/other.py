import pygame
import os

def load_image(name):
    fullname = os.path.join('', name)
    try:
        image = pygame.image.load(fullname)
        return image
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)