import pygame
import sys
import math
pygame.init()

# Musique du menu
pygame.mixer.music.load("Projet jeux python en 2D/assets/sounds/musique_ecran_d'acceuil.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, fade_ms=50)

from game import Game

# Clock
clock = pygame.time.Clock()
FPS = 120

# Musique du jeu
game_music_path = "Projet jeux python en 2D/assets/sounds/musique_dans_le_jeux.ogg"

# Menu pause
is_paused = False

# Fenêtre
pygame.display.set_caption("Jeu de tir en 2D")
screen = pygame.display.set_mode((1920, 1080))

# Arrière-plan
background = pygame.image.load("Projet jeux python en 2D/assets/Background.jpg").convert()
background = pygame.transform.scale(background, (1920, 1080))

# Bannière
banner = pygame.image.load("Projet jeux python en 2D/assets/banner.png").convert_alpha()
banner = pygame.transform.scale(banner, (int(screen.get_width()*0.42), int(screen.get_height()*0.7)))
banner_rect = banner.get_rect()
banner_rect.centerx = screen.get_width() // 2
banner_rect.y = int(screen.get_height() * 0.05)

# Boutons jouer,crédits,quitter
play_button = pygame.image.load("Projet jeux python en 2D/assets/button.png").convert_alpha()
play_button = pygame.transform.scale(play_button, (int(screen.get_width()*0.25), int(screen.get_height()*0.14)))
play_button_rect = play_button.get_rect()
play_button_rect.centerx = screen.get_width() // 2
play_button_rect.y = int(screen.get_height() / 1.6)
play_button_hover = pygame.transform.scale(play_button, (int(screen.get_width()*0.27), int(screen.get_height()*0.15)))
play_button_hover_rect = play_button_hover.get_rect(center=play_button_rect.center)

credits_img_original = pygame.image.load("Projet jeux python en 2D/assets/credits.png").convert_alpha()
credits_img = pygame.transform.scale(credits_img_original, (int(screen.get_width()*0.12), int(screen.get_height()*0.07)))
credits_rect = credits_img.get_rect(topright=(screen.get_width()-20, 20))
credits_img_hover = pygame.transform.scale(credits_img_original, (int(screen.get_width()*0.135), int(screen.get_height()*0.08)))
credits_hover_rect = credits_img_hover.get_rect(center=credits_rect.center)

quit_img_original = pygame.image.load("Projet jeux python en 2D/assets/quit.png").convert_alpha()
quit_img = pygame.transform.scale(quit_img_original, (int(screen.get_width()*0.25), int(screen.get_height()*0.14)))
quit_rect = quit_img.get_rect()
quit_rect.centerx = screen.get_width() // 2
quit_rect.y = play_button_rect.y + play_button_rect.height + 20
quit_img_hover = pygame.transform.scale(quit_img, (int(screen.get_width()*0.27), int(screen.get_height()*0.15)))
quit_hover_rect = quit_img_hover.get_rect(center=quit_rect.center)

# Icône réglages menu principal
settings_img_original = pygame.image.load("Projet jeux python en 2D/assets/settings.png").convert_alpha()
settings_img = pygame.transform.scale(settings_img_original, (int(screen.get_width()*0.12), int(screen.get_height()*0.07)))
settings_rect = settings_img.get_rect(bottomright=(screen.get_width() - 20, screen.get_height() - 20))
settings_img_hover = pygame.transform.scale(settings_img_original, (int(screen.get_width()*0.135), int(screen.get_height()*0.08)))
settings_hover_rect = settings_img_hover.get_rect(center=settings_rect.center)

# Popup crédits
show_popup = False
popup_width = int(screen.get_width() * 0.3)
popup_height = int(screen.get_height() * 0.28)
popup_rect = pygame.Rect((screen.get_width() - popup_width)//2,
                         (screen.get_height() - popup_height)//2,
                         popup_width,
                         popup_height)
close_btn_radius = 18
close_btn_center = (popup_rect.right - 30, popup_rect.top + 30)

# Fonts
title_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 60)
text_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 35)
credit_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 30)
pause_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 50)
font_small = pygame.font.Font(None, 36)

# Zones fin de partie
restart_rect = pygame.Rect(int(screen.get_width()*0.21), int(screen.get_height()*0.25), int(screen.get_width()*0.18), int(screen.get_height()*0.055))
menu_rect = pygame.Rect(int(screen.get_width()*0.21), int(screen.get_height()*0.32), int(screen.get_width()*0.18), int(screen.get_height()*0.055))

# Charger le jeu
game = Game()
manche_start_time = 0

# Volume
music_volume = 0.5
sound_volume = 0.5
pygame.mixer.music.set_volume(music_volume)
game.sound_manager.set_volume(sound_volume)

# Barre de volume
music_bar_rect = pygame.Rect(0,0,200,10)
music_slider_rect = pygame.Rect(0,0,20,20)
sound_bar_rect = pygame.Rect(0,0,200,10)
sound_slider_rect = pygame.Rect(0,0,20,20)
dragging_music = False
dragging_sound = False

# Variable pour menu réglages
show_settings = False

# Menu réglage son et musique
def draw_settings_menu(screen, music_volume, sound_volume):
    overlay = pygame.Surface((1920,1080), pygame.SRCALPHA)
    overlay.fill((0,0,0,150))
    screen.blit(overlay,(0,0))

    settings_window_width = 400
    settings_window_height = 300
    settings_window = pygame.Rect(
        (screen.get_width() - settings_window_width)//2,
        (screen.get_height() - settings_window_height)//2,
        settings_window_width,
        settings_window_height
    )
    pygame.draw.rect(screen,(50,50,50),settings_window,border_radius=12)
    pygame.draw.rect(screen,(255,255,255),settings_window,3,border_radius=12)

    margin_x = 50
    music_bar_y = settings_window.top + 90
    sound_bar_y = settings_window.top + 160

    # Musiques
    music_bar_rect.topleft = (settings_window.left + margin_x, music_bar_y)
    music_bar_rect.width = settings_window.width - 2*margin_x
    music_slider_rect.y = music_bar_rect.y - 5
    music_slider_rect.x = music_bar_rect.x + music_volume*music_bar_rect.width - 10
    pygame.draw.rect(screen,(180,180,180),music_bar_rect)
    pygame.draw.rect(screen,(255,255,0),music_slider_rect)
    screen.blit(font_small.render("Musique", True, (255,255,255)), (music_bar_rect.x, music_bar_rect.y-30))

    # Sons
    sound_bar_rect.topleft = (settings_window.left + margin_x, sound_bar_y)
    sound_bar_rect.width = settings_window.width - 2*margin_x
    sound_slider_rect.y = sound_bar_rect.y - 5
    sound_slider_rect.x = sound_bar_rect.x + sound_volume*sound_bar_rect.width - 10
    pygame.draw.rect(screen,(180,180,180),sound_bar_rect)
    pygame.draw.rect(screen,(255,255,0),sound_slider_rect)
    screen.blit(font_small.render("Sons", True, (255,255,255)), (sound_bar_rect.x, sound_bar_rect.y-30))

    # Bouton fermer avec X rouge
    close_btn = pygame.Rect(settings_window.right-40, settings_window.top+10, 30, 30)
    pygame.draw.rect(screen,(200,0,0),close_btn)
    pygame.draw.line(screen,(255,255,255),(close_btn.left+5,close_btn.top+5),(close_btn.right-5,close_btn.bottom-5),3)
    pygame.draw.line(screen,(255,255,255),(close_btn.right-5,close_btn.top+5),(close_btn.left+5,close_btn.bottom-5),3)

    return close_btn

# Début de la boucle principale du jeux
running = True
while running:
    screen.blit(background, (0, 0))
    mouse_pos = pygame.mouse.get_pos()

    # Quand la partie est en cours
    if game.is_playing:
        if not is_paused:
            game.update(screen)
            score_text = text_font.render(f"Score : {game.player.score}", True, (255, 255, 255))
            screen.blit(score_text, score_text.get_rect(center=(screen.get_width()//2, 50)))
            elapsed_time = (pygame.time.get_ticks() - manche_start_time)//1000
            timer_text = text_font.render(f"Temps : {elapsed_time}s", True, (255,255,255))
            screen.blit(timer_text, timer_text.get_rect(topleft=(20,20)))
        else:
            overlay = pygame.Surface((1920, 1080), pygame.SRCALPHA)
            overlay.fill((0,0,0,150))
            screen.blit(overlay,(0,0))
            pause_rect = pygame.Rect(screen.get_width()//2-250, screen.get_height()//2-150,500,300)
            pygame.draw.rect(screen,(50,50,50),pause_rect,border_radius=12)
            pygame.draw.rect(screen,(255,255,255),pause_rect,3,border_radius=12)

            # Boutons menu pause
            continue_rect = pygame.Rect(pause_rect.x+50,pause_rect.y+30,400,50)
            continue_color = (255,255,0) if continue_rect.collidepoint(mouse_pos) else (255,255,255)
            continue_text = pause_font.render("Continuer", True, continue_color)
            screen.blit(continue_text, continue_text.get_rect(center=(pause_rect.centerx, pause_rect.y+55)))

            settings_rect_area = pygame.Rect(pause_rect.x+50,pause_rect.y+100,400,50)
            settings_color = (255,255,0) if settings_rect_area.collidepoint(mouse_pos) else (255,255,255)
            settings_text = pause_font.render("Réglages", True, settings_color)
            screen.blit(settings_text, settings_text.get_rect(center=(pause_rect.centerx, pause_rect.y+125)))

            quit_rect_area = pygame.Rect(pause_rect.x+50,pause_rect.y+170,400,50)
            quit_color = (255,255,0) if quit_rect_area.collidepoint(mouse_pos) else (255,255,255)
            quit_text_pause = pause_font.render("Quitter", True, quit_color)
            screen.blit(quit_text_pause, quit_text_pause.get_rect(center=(pause_rect.centerx, pause_rect.y+195)))

            # Afficher menu réglages si ouvert
            if show_settings:
                close_btn = draw_settings_menu(screen, music_volume, sound_volume)

    # Menu principal et de fin
    else:
        if not game.is_game_over:
            screen.blit(banner,banner_rect)
            screen.blit(play_button_hover if play_button_rect.collidepoint(mouse_pos) else play_button, play_button_rect)
            screen.blit(credits_img_hover if credits_rect.collidepoint(mouse_pos) else credits_img, credits_rect)
            screen.blit(quit_img_hover if quit_rect.collidepoint(mouse_pos) else quit_img, quit_rect)

            # Icône réglages menu principal
            if settings_rect.collidepoint(mouse_pos):
                screen.blit(settings_img_hover, settings_hover_rect)
            else:
                screen.blit(settings_img, settings_rect)

            if show_settings:
                close_btn = draw_settings_menu(screen, music_volume, sound_volume)
        else:
            # Fin de la partie
            game_over_img = pygame.image.load("Projet jeux python en 2D/assets/Game_over.png").convert_alpha()
            game_over_img = pygame.transform.scale(game_over_img,(1920,1080))
            screen.blit(game_over_img,(0,0))
            title = title_font.render("Vous avez péri", True,(255,0,0))
            screen.blit(title,title.get_rect(center=(screen.get_width()//2,int(screen.get_height()*0.11))))
            if restart_rect.collidepoint(mouse_pos):
                text = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf",40).render("Recommencer une nouvelle partie",True,(255,255,0))
            else:
                text = text_font.render("Recommencer une nouvelle partie",True,(255,255,255))
            screen.blit(text,text.get_rect(center=restart_rect.center))
            if menu_rect.collidepoint(mouse_pos):
                text = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf",40).render("Retour au menu principale",True,(255,255,0))
            else:
                text = text_font.render("Retour au menu principale",True,(255,255,255))
            screen.blit(text,text.get_rect(center=menu_rect.center))

    # La popup crédit
    if show_popup:
        overlay = pygame.Surface((1920,1080),pygame.SRCALPHA)
        overlay.fill((0,0,0,150))
        screen.blit(overlay,(0,0))
        popup_rect = pygame.Rect((screen.get_width()-popup_width)//2,(screen.get_height()-popup_height)//2,popup_width,popup_height)
        close_btn_center = (popup_rect.right-30,popup_rect.top+30)
        pygame.draw.rect(screen,(240,240,240),popup_rect,border_radius=12)
        pygame.draw.rect(screen,(0,0,0),popup_rect,3,border_radius=12)
        text1 = credit_font.render("Jeu créé et développé par",True,(0,0,0))
        text2 = credit_font.render("Aurélien Wins",True,(0,0,0))
        text1_rect = text1.get_rect(center=(popup_rect.centerx,popup_rect.top+popup_rect.height*0.35))
        text2_rect = text2.get_rect(center=(popup_rect.centerx,popup_rect.top+popup_rect.height*0.55))
        screen.blit(text1,text1_rect)
        screen.blit(text2,text2_rect)
        pygame.draw.circle(screen,(200,0,0),close_btn_center,close_btn_radius)
        pygame.draw.line(screen,(255,255,255),(close_btn_center[0]-8,close_btn_center[1]-8),(close_btn_center[0]+8,close_btn_center[1]+8),3)
        pygame.draw.line(screen,(255,255,255),(close_btn_center[0]+8,close_btn_center[1]-8),(close_btn_center[0]-8,close_btn_center[1]+8),3)

    pygame.display.flip()

    # Les différent évenements
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            print("Le jeu se ferme")
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and game.is_playing and not is_paused:
                game.player.launch_projectile()
            elif event.key==pygame.K_ESCAPE and game.is_playing:
                is_paused=not is_paused
            game.pressed[event.key]=True
        elif event.type==pygame.KEYUP:
            game.pressed[event.key]=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mx,my=event.pos
            if music_slider_rect.collidepoint(event.pos):
                dragging_music=True
            if sound_slider_rect.collidepoint(event.pos):
                dragging_sound=True
            # Fermer la fenêtre réglages
            if show_settings and close_btn.collidepoint(event.pos):
                show_settings = False
            # Menu pause
            if is_paused:
                if continue_rect.collidepoint((mx,my)):
                    is_paused=False
                elif settings_rect_area.collidepoint((mx,my)):
                    show_settings=True
                elif quit_rect_area.collidepoint((mx,my)):
                    is_paused=False
                    game.is_playing=False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("Projet jeux python en 2D/assets/sounds/musique_ecran_d'acceuil.ogg")
                    pygame.mixer.music.play(-1,fade_ms=50)
            # Ouvrir menu réglages depuis menu principal
            if not game.is_playing and not game.is_game_over:
                if settings_rect.collidepoint(event.pos):
                    show_settings = True
            # Fermer popup crédits
            if show_popup and math.hypot(mx-close_btn_center[0],my-close_btn_center[1])<=close_btn_radius:
                show_popup=False
            # Menu principal
            if not game.is_playing and not game.is_game_over and not show_settings:
                if play_button_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(game_music_path)
                    pygame.mixer.music.play(-1,fade_ms=50)
                    game.start()
                    game.sound_manager.play("click")
                    manche_start_time=pygame.time.get_ticks()
                elif credits_rect.collidepoint(event.pos):
                    show_popup=True
                    game.sound_manager.play("click")
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            # Fin partie
            if game.is_game_over:
                if restart_rect.collidepoint(event.pos):
                    game.is_game_over=False
                    game.start()
                    manche_start_time=pygame.time.get_ticks()
                    game.sound_manager.play("click")
                elif menu_rect.collidepoint(event.pos):
                    game.is_game_over=False
                    game.is_playing=False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("Projet jeux python en 2D/assets/sounds/musique_ecran_d'acceuil.ogg")
                    pygame.mixer.music.play(-1,fade_ms=50)
                    game.sound_manager.play("click")
        elif event.type==pygame.MOUSEBUTTONUP:
            dragging_music=False
            dragging_sound=False
        elif event.type==pygame.MOUSEMOTION:
            if dragging_music:
                rel_x = max(0, min(event.pos[0] - music_bar_rect.x, music_bar_rect.width))
                music_volume = rel_x / music_bar_rect.width
                pygame.mixer.music.set_volume(music_volume)
                music_slider_rect.x = music_bar_rect.x + rel_x - 10
            if dragging_sound:
                rel_x = max(0, min(event.pos[0] - sound_bar_rect.x, sound_bar_rect.width))
                sound_volume = rel_x / sound_bar_rect.width
                game.sound_manager.set_volume(sound_volume)
                game.sound_manager.play("click")
                sound_slider_rect.x = sound_bar_rect.x + rel_x - 10

    clock.tick(FPS)


















  

























