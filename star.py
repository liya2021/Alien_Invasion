import pygame
from pygame.sprite import Sprite
from random import randint




class Star(Sprite):

    def __init__(self, ai_game):
        size = randint(0, 80)
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.transform.scale(pygame.image.load('images/star.bmp'), (size, size))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
