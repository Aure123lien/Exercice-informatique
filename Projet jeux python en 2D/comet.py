import pygame

# création de ma classe comet
class Comet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Projet jeux python en 2D/assets/comet.png")
        self.rect = self.image.get_rect()
        