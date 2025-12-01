import pygame
from ..configuration import *

# Les différentes polices d'écriture utilisées dans le menu
title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
text_font = pygame.font.Font(FONT_PATH, TEXT_FONT_SIZE)

class StatsMenu:
    def __init__(self, screen, player, best_score, level_scores):
        self.screen = screen
        self.player = player
        self.best_score = best_score
        self.level_scores = level_scores

        # Charger les images du menu
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        self.background = pygame.transform.smoothscale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Titre
        self.title_text = title_font.render("Statistiques du Personnage", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.centerx = SCREEN_WIDTH // 2
        self.title_rect.y = 50

        # Bouton retour
        self.back_button = pygame.image.load(RETOUR_IMG_PATH).convert_alpha()
        self.back_button = pygame.transform.scale(self.back_button, (200, 100))
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.centerx = SCREEN_WIDTH // 2
        self.back_button_rect.y = SCREEN_HEIGHT - 150
        self.back_button_hover = pygame.transform.scale(self.back_button, (int(200 * 1.05), int(100 * 1.05)))
        self.back_button_hover_rect = self.back_button_hover.get_rect(center=self.back_button_rect.center)

        self.skill_buttons = []

    def draw(self, mouse_pos):
        self.screen.blit(self.background, (0, 0))
        # Centrer le titre au milieu de l'écran
        self.screen.blit(self.title_text, self.title_rect)

        # Compétences à gauche
        skills_title = title_font.render("Compétences", True, BLACK)
        skills_title_rect = skills_title.get_rect()
        skills_title_rect.centerx = SCREEN_WIDTH // 3
        skills_title_rect.y = 150
        self.screen.blit(skills_title, skills_title_rect)

        # Points de compétence
        skill_points_text = text_font.render(f"Points de compétence: {self.player.skill_points}", True, BLACK)
        skill_points_rect = skill_points_text.get_rect()
        skill_points_rect.centerx = SCREEN_WIDTH // 3
        skill_points_rect.y = skills_title_rect.bottom + 10
        self.screen.blit(skill_points_text, skill_points_rect)

        # Liste des compétences
        y_offset_skills = skill_points_rect.bottom + 20
        skills = [
            ("Vie maximale", self.player.max_health),
            ("Attaque", self.player.attack),
            ("Vitesse", self.player.velocity)
        ]
        self.skill_buttons = []
        for skill_name, current_value in skills:
            skill_text = text_font.render(f"{skill_name}: {current_value}", True, BLACK)
            skill_rect = skill_text.get_rect(centerx=SCREEN_WIDTH // 3, y=y_offset_skills)
            self.screen.blit(skill_text, skill_rect)

            # Bouton + si points disponibles
            if self.player.skill_points > 0:
                plus_button = pygame.Rect(SCREEN_WIDTH // 3 + 100, y_offset_skills - 10, 30, 30)
                pygame.draw.rect(self.screen, (0, 255, 0), plus_button)
                plus_text = text_font.render("+", True, BLACK)
                plus_text_rect = plus_text.get_rect(center=plus_button.center)
                self.screen.blit(plus_text, plus_text_rect)
                self.skill_buttons.append((plus_button, skill_name))
            else:
                self.skill_buttons.append((None, skill_name))

            y_offset_skills += 40

        # Statistiques à droite
        stats_title = title_font.render("Statistiques", True, BLACK)
        stats_title_rect = stats_title.get_rect()
        stats_title_rect.centerx = 2 * SCREEN_WIDTH // 3
        stats_title_rect.y = 150
        self.screen.blit(stats_title, stats_title_rect)

        y_offset_stats = stats_title_rect.bottom + 20
        stats = [
            f"Niveau: {self.player.level}/{PLAYER_MAX_LEVEL}",
            f"XP: {self.player.xp}/{self.player.xp_to_next}",
            f"Vie maximale: {self.player.max_health}",
            f"Attaque: {self.player.attack}",
            f"Vitesse: {self.player.velocity}"
        ]

        for stat in stats:
            text = text_font.render(stat, True, BLACK)
            rect = text.get_rect(centerx=2 * SCREEN_WIDTH // 3, y=y_offset_stats)
            self.screen.blit(text, rect)
            y_offset_stats += 30

        # Bouton retour en bas
        if self.back_button_rect.collidepoint(mouse_pos):
            self.screen.blit(self.back_button_hover, self.back_button_hover_rect)
        else:
            self.screen.blit(self.back_button, self.back_button_rect)

    def handle_click(self, pos):
        if self.back_button_rect.collidepoint(pos):
            return "back"
        for button, skill_name in self.skill_buttons:
            if button and button.collidepoint(pos) and self.player.skill_points > 0:
                if skill_name == "Vie maximale":
                    self.player.max_health += 10
                    self.player.health = self.player.max_health  # Heal to full
                elif skill_name == "Attaque":
                    self.player.attack += 5
                elif skill_name == "Vitesse":
                    self.player.velocity += 1
                self.player.skill_points -= 1
                self.player.save_stats()
                break
        return None