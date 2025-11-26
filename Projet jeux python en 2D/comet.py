import pygame
import random

# création de ma classe comet
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("Projet jeux python en 2D/assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 1800)  # adapté à 1920
        self.rect.y = - random.randint(0, 1080)  # adapté à 1080
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play("meteorite")

        # verifier si les comète sont = 0
        if len(self.comet_event.all_comets) == 0:
            print("La pluie de comète est fini")
            self.comet_event.reset_percent()
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity
        
        if self.rect.y >= self.comet_event.game.screen.get_height() * 0.46:  # zone adaptée à 1080
            self.remove()

            # si plus de comète sur le jeu
            if len(self.comet_event.all_comets) == 0:
                print("La pluie de comète est fini")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            print("la comète a toucher")
            self.remove()
            # dégat sur le joueur
            self.comet_event.game.player.damage(20)
