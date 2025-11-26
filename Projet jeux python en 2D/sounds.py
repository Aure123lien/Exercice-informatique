import pygame

if not pygame.mixer.get_init():
    pygame.mixer.pre_init(44100, -16, 2, 2, 512)
    pygame.mixer.init()

class SoundManager:
    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound("Projet jeux python en 2D/assets/sounds/click.ogg"),
            "game_over": pygame.mixer.Sound("Projet jeux python en 2D/assets/sounds/game_over.ogg"),
            "meteorite": pygame.mixer.Sound("Projet jeux python en 2D/assets/sounds/meteorite.ogg"),
            "tir": pygame.mixer.Sound("Projet jeux python en 2D/assets/sounds/tir.ogg"),
        }
        self.volume = 0.5  # volume global des effets
        self.set_volume(self.volume)

    def set_volume(self, volume):
        """Mettre à jour le volume de tous les sons."""
        self.volume = max(0.0, min(1.0, volume))
        for sound in self.sounds.values():
            sound.set_volume(self.volume)

    def play(self, sound_name):
        self.sounds[sound_name].play()



