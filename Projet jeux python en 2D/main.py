import pygame
from game import Game
pygame.init()


# on va générer la fenêtre du jeu
pygame.display.set_caption("Jeu de tir en 2D")
screen = pygame.display.set_mode((1080, 720))

# On va importer une image pour le mettre en arrière-plan du jeu
background = pygame.image.load("Projet jeux python en 2D/assets/Background.jpg")

# charger le jeu
game = Game()

running = True

# On va créer une boucle pour la condition juste au-dessus
while running:

    # appliquer l'arrière-plan
    screen.blit(background, (0, 0))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Deplacement de mon joueur veut aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()

    print(game.player.rect.x)
    
    # Mettre à jour l'écran
    pygame.display.flip()

    # On va vérifier si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # On va vérifier si l'événement est la fermeture de la fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu se ferme")
            # je vais detecter si un joueur fais une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed [event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed [event.key] = False
                

