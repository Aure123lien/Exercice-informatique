import pygame
pygame.init()

#creer la première classe du jeux
class player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load("Projet jeux python en 2D/assets/Mage.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300


# on va generer la fenetre du jeux
pygame.display.set_caption("jeux de tir en 2D")
screen = pygame.display.set_mode((1080, 720))

# On va importer une image pour le mettre en arrire plan du jeu
background = pygame.image.load("Projet jeux python en 2D/assets/Background.jpg")

# Mettre le personnage sur le jeux
player = player()

running = True

# On va creer une boucle pour la condition juste au dessus
while running:

    # appliquer l'arrière plan
    screen.blit(background, (0, 0))

    # appliquer l'image du joueur
    screen.blit(player.image, player.rect)
    
    # Mettre a jour l'ecran
    pygame.display.flip()

    # On va vérifier si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # On va vérifier l'évenement est fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False

# Quand on sort de la boucle
pygame.quit()
print("Le jeux se ferme")

