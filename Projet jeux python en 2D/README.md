# Jeu 2D réalisé avec Pygame

Ce projet est un jeu de shooter en 2D développé en Python avec Pygame.  
Le joueur doit survivre face à des vagues de monstres et à des événements spéciaux comme la chute de comètes, tout en marquant le meilleur score possible.  
Ce projet met en avant l'orientation objet, les collisions, la gestion des sons et la création d’événements personnalisés, la création de classe, vous découvrivrez plus ci dessous les détails de mon projet et l'installation

Ce projet permet de vous montrer ma capacité à concevoir un programme structuré et organiser, à résoudre des problèmes, et surtout a montrer ma motivation à progresser dans le domaine de l’informatique

# Fonctionnalités principales de mon jeux

- Un menu principal + écran de fin de partie (sur le bouton de fin de partie possibilité de refaire une partie ou de revenir au menu principal)
- Un déplacement fluide du joueur
- Un Système de tir et de projectiles + des comètes
- Le Score visible en temps réel avec un timer tous au long de la partie en cours
- Apparition de plusieurs types de monstres différents
- Événement spécial : chute de comètes qui arrive au bout d'un certain temps
- Sons variés (tir, dégâts subis, chute des comètes)
- Musique au menu principale, pendant le jeux et au menu quand le joueur a perdu
- Gestion des collisions (entre les différents entitée joueur avec monstre et comètes par exemple)
- Barre de vie du joueur et des monstres visible
- J'ai essayer d'optimiser au mieux la boucle du jeu (120 FPS) 

## 🧠 Structure du projet

Voici la structure des fichiers principaux du jeu :
- main.py C'est le Point d'entrée du jeu boucle principale et ou toutes les fonctionnalité (musique, etc)
- game.py  C'est le fichier de la gestion du jeu global du jeux affichage, collisions et bien d'autre
- player.py C'est le fichier qui sert a creer et gerer la classe joueur et la personnalisé (Les PV du joueur, l'attaque du joueur, la vitesse des joueurs)
- projectile.py C'est le fichier qui permet l'envoie des projectiles du joueur et gère ses fonctionnalité
- monster.py  C'est la Classe des monstres et permet de les modifier et d'en rajouter
- comet_event.py Il gère l'évenenement rajouter au jeux (j'ai choisis la chute de comète)
- comet.py  Ce qui représentant une comète seule et les intéractions qu'elle va pouvoir réaliser
- sounds.py  Gestion et chargement des effets sonores
- assets/  Ce dossier sert a gerer toutes les Images, sprites, sons, polices, etc qui seront rajouter dans le jeux

Chaque fichier représente un élément bien séparé du jeux et qui permet donc une clareter, une logique et avec une facilité de gerer les différents élement du jeux

# Installation de mon jeux

1. Installer Pygame :
   
   Lancer votre terminal faites :
   - pip install pygame

2. télécharger mon projet :

 Sur la page de mon guithub un petit logo vert sera visible "code" cliquez dessus et faites "download ZIP" le fichier se téléchargera avec tous mon projet se téléchargera

 ou cloner mon projet 

# Les Contrôles

- Pour les déplacements de gauche a droite : appuyer sur les touches fleches gauche et droite 
- Pour effectuer un tir avec votre joueur : appuyer sur la touche espace
- En jeux pour avoir accès au menu pause : appuyer sur la touche Esc

# Compétences acquises

Grâce à ce projet, j’ai développé :

# Compétences techniques
- Python (structures, classes, modules)
- Pygame (affichage, images, sons, collisions)
- Gestion de plusieurs fichier qui gèrent différentes fonctionnalité du jeux
- Gestion de ressources (sprites, sons)
- Gerer une superposition d'éléments complet qui doivent se gerer ensemble

# Compétences générales
- Autonomie dans l’apprentissage
- Résolution de problèmes
- Planification et organisation d’un projet
- Persévérance et capacité à débuguer un programme complet

# Améliorations envisagées






# Credits

Projet développé par Wins Aurélien, candidat sur Parcoursup pour des formations en informatique / développement  
Ce jeu illustre ma passion pour la programmation et mon envie d’apprendre et de créer







