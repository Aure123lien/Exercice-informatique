import pygame
from player import Player
from monster import Dragon, Monster, Ogre
from comet_event import CometFallEvent
from sounds import SoundManager

# créer une seconde classe
class Game:

    def __init__(self):
        # Définir si le jeu a commencé
        self.is_playing = False
        self.is_game_over = False

        # groupe joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        # génération de l'événement
        self.comet_event = CometFallEvent(self)

        # groupe de monstres
        self.all_monsters = pygame.sprite.Group()

        # gérer le son
        self.sound_manager = SoundManager()

        # mettre le score à 0
        self.font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 25)
        self.score = 0
        self.pressed = {}

        self.game_over_image = pygame.image.load("Projet jeux python en 2D/assets/Game_over.png").convert()

        self.go_title_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 60)
        self.go_sub_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 35)

        self.go_restart_button = pygame.Rect(390, 300, 300, 60)
        self.go_menu_button = pygame.Rect(390, 380, 300, 60)

    def start(self):
        self.is_playing = True
        # remettre le joueur plus haut sur le sol
        self.player.rect.x = 350
        self.player.rect.y = 760
        # générer 2 Ogres et 1 Dragon
        for _ in range(2):
            self.spawn_monster(Ogre)
        self.spawn_monster(Dragon)

    def add_score(self, points):
        self.score += points

    def game_over(self):
        # remettre le jeu à zéro
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        # remettre le joueur plus haut sur le sol
        self.player.rect.x = 350
        self.player.rect.y = 760
        self.comet_event.reset_percent()
        self.is_playing = False
        self.is_game_over = True
        self.score = 0
        # jouer le son
        self.sound_manager.play("game_over")

    def display_game_over(self, screen):
        # image
        screen.blit(self.game_over_image, (0, 0))

        # titre
        title = self.go_title_font.render("Vous avez péri", True, (255, 0, 0))
        screen.blit(title, title.get_rect(center=(screen.get_width() // 2, 90)))

        # bouton recommencer
        pygame.draw.rect(screen, (200, 200, 200), self.go_restart_button)
        restart_text = self.go_sub_font.render("Recommencer", True, (0, 0, 0))
        screen.blit(restart_text, restart_text.get_rect(center=self.go_restart_button.center))

        # bouton retour menu
        pygame.draw.rect(screen, (200, 200, 200), self.go_menu_button)
        menu_text = self.go_sub_font.render("Retour au menu", True, (0, 0, 0))
        screen.blit(menu_text, menu_text.get_rect(center=self.go_menu_button.center))

    def update(self, screen):
        # afficher le score sur l'écran
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # afficher le joueur
        screen.blit(self.player.image, self.player.rect)

        # afficher la barre de vie du joueur
        self.player.update_health_bar(screen)

        # afficher la barre de la comète
        self.comet_event.update_bar(screen)

        # déplacer et afficher les projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()
        self.player.all_projectiles.draw(screen)

        # déplacer et afficher les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        self.all_monsters.draw(screen)

        # comètes
        for comet in self.comet_event.all_comets:
            comet.fall()
        self.comet_event.all_comets.draw(screen)

        # déplacements joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.right < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.left > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name=Ogre):
        self.all_monsters.add(monster_class_name(self))











