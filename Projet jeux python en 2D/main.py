import pygame
pygame.init()

# Musique du menu
pygame.mixer.music.load("Projet jeux python en 2D/assets/sounds/musique_ecran_d'acceuil.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, fade_ms=50)

import math
from game import Game

# Réaliser une clock
clock = pygame.time.Clock()
FPS = 120

# on va générer la fenêtre du jeu
pygame.display.set_caption("Jeu de tir en 2D")
screen = pygame.display.set_mode((1920, 1080))

# On va importer une image pour le mettre en arrière-plan du jeu
background = pygame.image.load("Projet jeux python en 2D/assets/Background.jpg").convert()
background = pygame.transform.scale(background, (1920, 1080))

# charger la bannière
banner = pygame.image.load("Projet jeux python en 2D/assets/banner.png").convert_alpha()
banner = pygame.transform.scale(banner, (int(screen.get_width()*0.42), int(screen.get_height()*0.7)))
banner_rect = banner.get_rect()
banner_rect.centerx = screen.get_width() // 2  # centrage horizontal
banner_rect.y = int(screen.get_height() * 0.05)  # marge en haut

# charger le bouton jouer
play_button = pygame.image.load("Projet jeux python en 2D/assets/button.png").convert_alpha()
play_button = pygame.transform.scale(play_button, (int(screen.get_width()*0.25), int(screen.get_height()*0.14)))
play_button_rect = play_button.get_rect()
play_button_rect.centerx = screen.get_width() // 2  # centrage horizontal
play_button_rect.y = int(screen.get_height() / 1.6)

# version agrandie du bouton jouer pour le survol
play_button_hover = pygame.transform.scale(play_button, (int(screen.get_width()*0.27), int(screen.get_height()*0.15)))
play_button_hover_rect = play_button_hover.get_rect(center=play_button_rect.center)

# Affichage de l'image du bouton crédits 
credits_img_original = pygame.image.load("Projet jeux python en 2D/assets/credits.png").convert_alpha()
credits_img = pygame.transform.scale(credits_img_original, (int(screen.get_width()*0.12), int(screen.get_height()*0.07)))
credits_rect = credits_img.get_rect(topright=(screen.get_width()-20, 20))

# survol du bouton credits lorsque la souris passe dessus
credits_img_hover = pygame.transform.scale(credits_img_original, (int(screen.get_width()*0.135), int(screen.get_height()*0.08)))
credits_hover_rect = credits_img_hover.get_rect(center=credits_rect.center)

# Popup crédits
show_popup = False
popup_rect = pygame.Rect(int(screen.get_width()*0.15), int(screen.get_height()*0.18), int(screen.get_width()*0.3), int(screen.get_height()*0.28))

# bouton rond fermer
close_btn_center = (popup_rect.x + popup_rect.width - 30, popup_rect.y + 30)  # en haut à droite du popup
close_btn_radius = 18

# Fonts
title_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 60)
text_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 35)
credit_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 30)

# Zones cliquables fin de partie
restart_rect = pygame.Rect(int(screen.get_width()*0.21), int(screen.get_height()*0.25), int(screen.get_width()*0.18), int(screen.get_height()*0.055))
menu_rect = pygame.Rect(int(screen.get_width()*0.21), int(screen.get_height()*0.32), int(screen.get_width()*0.18), int(screen.get_height()*0.055))

# charger le jeu
game = Game(screen)

running = True

while running:

    # appliquer l'arrière-plan
    screen.blit(background, (0, 0))

    # vérifier si le jeu a commencé
    if game.is_playing:
        game.update(screen)

    else:
        # écran d'accueil
        if not game.is_game_over:
            screen.blit(banner, banner_rect)
            # survol dynamique du bouton jouer
            mouse_pos = pygame.mouse.get_pos()
            if play_button_rect.collidepoint(mouse_pos):
                screen.blit(play_button_hover, play_button_hover_rect)
            else:
                screen.blit(play_button, play_button_rect)

            # affichage du bouton crédits + survol
            if credits_rect.collidepoint(mouse_pos):
                screen.blit(credits_img_hover, credits_hover_rect)
            else:
                screen.blit(credits_img, credits_rect)

        # écran de fin de partie
        else:
            game_over_img = pygame.image.load("Projet jeux python en 2D/assets/Game_over.png").convert_alpha()
            game_over_img = pygame.transform.scale(game_over_img, (1920, 1080))
            screen.blit(game_over_img, (0, 0))

            title = title_font.render("Vous avez péri", True, (255, 0, 0))
            screen.blit(title, title.get_rect(center=(screen.get_width() // 2, int(screen.get_height()*0.11))))

            mouse_pos = pygame.mouse.get_pos()

            # bouton recommencer la partie
            if restart_rect.collidepoint(mouse_pos):
                color = (255, 255, 0)
                hover_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 40)
                text = hover_font.render("Recommencer une nouvelle partie", True, color)
            else:
                text = text_font.render("Recommencer une nouvelle partie", True, (255, 255, 255))
            screen.blit(text, text.get_rect(center=restart_rect.center))

            # retour au menu principale
            if menu_rect.collidepoint(mouse_pos):
                hover_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 40)
                text = hover_font.render("Retour au menu principale", True, (255, 255, 0))
            else:
                text = text_font.render("Retour au menu principale", True, (255, 255, 255))
            screen.blit(text, text.get_rect(center=menu_rect.center))

    # Affichage de la popup
    if show_popup:

        # Le fond de la popupp
        overlay = pygame.Surface((1920, 1080), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))

        # fenêtre popup
        pygame.draw.rect(screen, (240, 240, 240), popup_rect, border_radius=12)
        pygame.draw.rect(screen, (0, 0, 0), popup_rect, width=3, border_radius=12)

        # texte crédits
        text1 = credit_font.render("Jeu créé et développé par", True, (0, 0, 0))
        text2 = credit_font.render("Aurélien Wins", True, (0, 0, 0))

        screen.blit(text1, text1.get_rect(center=(screen.get_width()//2, popup_rect.y + 90)))
        screen.blit(text2, text2.get_rect(center=(screen.get_width()//2, popup_rect.y + 140)))

        # bouton rond rouge
        pygame.draw.circle(screen, (200, 0, 0), close_btn_center, close_btn_radius)

        # dessin du X
        pygame.draw.line(screen, (255, 255, 255),
                         (close_btn_center[0] - 8, close_btn_center[1] - 8),
                         (close_btn_center[0] + 8, close_btn_center[1] + 8), 3)

        pygame.draw.line(screen, (255, 255, 255),
                         (close_btn_center[0] + 8, close_btn_center[1] - 8),
                         (close_btn_center[0] - 8, close_btn_center[1] + 8), 3)

    # mise à jour dynamique
    pygame.display.flip()

    # gestions des évenements
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu se ferme")

        # tirer avec espace
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.is_playing:
                game.player.launch_projectile()

            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # fermer popup
            if show_popup:
                mx, my = event.pos
                if math.hypot(mx - close_btn_center[0], my - close_btn_center[1]) <= close_btn_radius:
                    show_popup = False
                continue

            # bouton jouer
            if not game.is_playing and not game.is_game_over:
                if play_button_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop() 
                    game.start()
                    game.sound_manager.play("click")

                # bouton crédits
                if credits_rect.collidepoint(event.pos):
                    show_popup = True
                    game.sound_manager.play("click")

            # fin de partie
            if game.is_game_over:

                if restart_rect.collidepoint(event.pos):
                    game.is_game_over = False
                    game.start()
                    game.sound_manager.play("click")

                elif menu_rect.collidepoint(event.pos):
                    game.is_game_over = False
                    game.is_playing = False
                    pygame.mixer.music.play(-1) 
                    game.sound_manager.play("click")

    clock.tick(FPS)
















