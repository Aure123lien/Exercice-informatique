import pygame
from player import Player
from monster import Monster

# créer une seconde classe
class Game:

    def __init__(self):
        # générer un joueur
        self.player = Player()
        # groupe des monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)