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
        # Titre doit etre au centre en haut
        self.screen.blit(self.title_text, self.title_rect)

        # HUD pour les compétences à gauche et au millieu
        skills_hud_width = 400
        skills_hud_height = 350
        skills_hud_x = SCREEN_WIDTH // 4 - skills_hud_width // 2
        skills_hud_y = 150
        skills_hud_rect = pygame.Rect(skills_hud_x, skills_hud_y, skills_hud_width, skills_hud_height)
        pygame.draw.rect(self.screen, DARK_GRAY, skills_hud_rect)
        pygame.draw.rect(self.screen, BLACK, skills_hud_rect, 3)  # Bordure de la fenetre

        # Titre de  l'HUD Compétences
        skills_title = title_font.render("Compétences", True, WHITE)
        skills_title_rect = skills_title.get_rect(centerx=skills_hud_rect.centerx, y=skills_hud_y + 10)
        self.screen.blit(skills_title, skills_title_rect)

        # Points de compétence
        skill_points_text = text_font.render(f"Points de compétence: {self.player.skill_points}", True, WHITE)
        skill_points_rect = skill_points_text.get_rect(centerx=skills_hud_rect.centerx, y=skills_title_rect.bottom + 10)
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
            skill_text = text_font.render(f"{skill_name}: {current_value}", True, WHITE)
            skill_rect = skill_text.get_rect(centerx=skills_hud_rect.centerx, y=y_offset_skills)
            self.screen.blit(skill_text, skill_rect)

            # Bouton + crée si des points de compétence sont disponibles
            if self.player.skill_points > 0:
                plus_button = pygame.Rect(skill_rect.right + 10, y_offset_skills - 10, 30, 30)
                pygame.draw.rect(self.screen, GREEN, plus_button)
                plus_text = text_font.render("+", True, BLACK)
                plus_text_rect = plus_text.get_rect(center=plus_button.center)
                self.screen.blit(plus_text, plus_text_rect)
                self.skill_buttons.append((plus_button, skill_name))
            else:
                self.skill_buttons.append((None, skill_name))

            y_offset_skills += 40

        # l'HUD statistiques à droite
        stats_hud_width = 400
        stats_hud_height = 350
        stats_hud_x = 3 * SCREEN_WIDTH // 4 - stats_hud_width // 2
        stats_hud_y = 150
        stats_hud_rect = pygame.Rect(stats_hud_x, stats_hud_y, stats_hud_width, stats_hud_height)
        pygame.draw.rect(self.screen, DARK_GRAY, stats_hud_rect)
        pygame.draw.rect(self.screen, BLACK, stats_hud_rect, 3) 

        # Titre de HUD statistiques
        stats_title = title_font.render("Statistiques", True, WHITE)
        stats_title_rect = stats_title.get_rect(centerx=stats_hud_rect.centerx, y=stats_hud_y + 10)
        self.screen.blit(stats_title, stats_title_rect)

        # Barre de santé toujours pleine pour représenter le maximum de pv du personne en plus des point rajouter dedans
        bar_width = 300
        bar_height = 20
        bar_x = stats_hud_rect.centerx - bar_width // 2
        bar_y = stats_title_rect.bottom + 20
        pygame.draw.rect(self.screen, GRAY, [bar_x, bar_y, bar_width, bar_height])
        pygame.draw.rect(self.screen, RED, [bar_x, bar_y, bar_width, bar_height])  # Toujours pleine
        health_text = text_font.render(f"Vie maximale: {int(self.player.max_health)}", True, WHITE)
        health_text_rect = health_text.get_rect(centerx=stats_hud_rect.centerx, y=bar_y - 25)
        self.screen.blit(health_text, health_text_rect)

        # Statistiques en dessous
        stats_y = bar_y + bar_height + 20
        # Afficher niveau et XP 
        level_text = text_font.render(f"Niveau: {self.player.level}/{PLAYER_MAX_LEVEL}", True, WHITE)
        level_rect = level_text.get_rect(centerx=stats_hud_rect.centerx, y=stats_y)
        self.screen.blit(level_text, level_rect)
        stats_y += 30
        xp_text = text_font.render(f"XP: {self.player.xp}/{self.player.xp_to_next}", True, WHITE)
        xp_rect = xp_text.get_rect(centerx=stats_hud_rect.centerx, y=stats_y)
        self.screen.blit(xp_text, xp_rect)
        stats_y += 30

        # Statistique améliorables avec le boutons +
        upgradeable_stats = [
            ("Vie maximale", self.player.max_health),
            ("Attaque", self.player.attack),
            ("Vitesse", self.player.velocity)
        ]
        self.upgrade_buttons = []
        for stat_name, current_value in upgradeable_stats:
            stat_text = text_font.render(f"{stat_name}: {current_value}", True, WHITE)
            stat_rect = stat_text.get_rect(centerx=stats_hud_rect.centerx, y=stats_y)
            self.screen.blit(stat_text, stat_rect)

            # Bouton + si points disponibles
            if self.player.skill_points > 0:
                plus_button = pygame.Rect(stat_rect.right + 10, stats_y - 10, 30, 30)
                pygame.draw.rect(self.screen, GREEN, plus_button)
                plus_text = text_font.render("+", True, BLACK)
                plus_text_rect = plus_text.get_rect(center=plus_button.center)
                self.screen.blit(plus_text, plus_text_rect)
                self.upgrade_buttons.append((plus_button, stat_name))
            else:
                self.upgrade_buttons.append((None, stat_name))

            stats_y += 40

        # Bouton retour en bas
        if self.back_button_rect.collidepoint(mouse_pos):
            self.screen.blit(self.back_button_hover, self.back_button_hover_rect)
        else:
            self.screen.blit(self.back_button, self.back_button_rect)

    def handle_click(self, pos):
        if self.back_button_rect.collidepoint(pos):
            return "back"
        # Boutons dans le HUD gauche (compétences)
        for button, skill_name in self.skill_buttons:
            if button and button.collidepoint(pos) and self.player.skill_points > 0:
                if skill_name == "Vie maximale":
                    self.player.max_health += 10
                    self.player.health = self.player.max_health 
                elif skill_name == "Attaque":
                    self.player.attack += 2
                elif skill_name == "Vitesse":
                    self.player.velocity += 0.1
                self.player.skill_points -= 1
                self.player.save_stats()
                break
        # Boutons dans le HUD droit (améliorations)
        for button, stat_name in self.upgrade_buttons:
            if button and button.collidepoint(pos) and self.player.skill_points > 0:
                if stat_name == "Vie maximale":
                    self.player.max_health += 10
                    self.player.health = self.player.max_health 
                elif stat_name == "Attaque":
                    self.player.attack += 2
                elif stat_name == "Vitesse":
                    self.player.velocity += 0.1
                self.player.skill_points -= 1
                self.player.save_stats()
                break
        return None