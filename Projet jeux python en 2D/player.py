import pygame

# créer la classe Player
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.image = pygame.image.load("Projet jeux python en 2D/assets/Mage.png")
        
        # Redimensionner l'image du joueur
        self.image = pygame.transform.scale(self.image, (300, 250))  # largeur=100, hauteur=150
        
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 430

    def move_right(self):
        self.rect.x += self.velocity  # Déplace le joueur vers la droite

    def move_left(self):
        self.rect.x -= self.velocity  # Déplace le joueur vers la gauche
