import pygame


# créer la classe Monster
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.image = pygame.image.load("Projet jeux python en 2D/assets/ogre.png")
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 465
        self.velocity = 1
    # Redimensionner l'image du monstre
        self.image = pygame.transform.scale(self.image, (200, 150))

    def forward(self):
        # cette ligne rajoute que mon monstre pourra se déplacer jusqu'a ce qu'il est une colission avec le joueur
        if not self.game.check_collision(self, self.game.all_players):
           self.rect.x -= self.velocity