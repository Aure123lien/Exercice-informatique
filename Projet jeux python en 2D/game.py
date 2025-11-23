import pygame
from player import Player

# créer une seconde classe
class Game:

    def __init__(self):
        # générer un joueur
        self.player = Player()
        self.pressed = {}