import pygame
from ..configuration import *

class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.volume = INITIAL_SOUND_VOLUME
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.init()
            self.sounds = {
                "click": pygame.mixer.Sound(SOUND_CLICK_PATH),
                "game_over": pygame.mixer.Sound(SOUND_GAME_OVER_PATH),
                "meteorite": pygame.mixer.Sound(SOUND_METEORITE_PATH),
                "tir": pygame.mixer.Sound(SOUND_TIR_PATH),
            }
            self.set_volume(self.volume)
        except pygame.error as e:
            print(f"Audio ne s'est pas initialiser: {e}. Le son sera désactiver.")
            self.sounds = {}

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))
        for sound in self.sounds.values():
            sound.set_volume(self.volume)

    def play(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].play()