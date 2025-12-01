@echo off
echo Lancement du jeu Python en 2D...
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installé ou n'est pas dans le PATH.
    echo Veuillez installer Python depuis https://www.python.org/
    echo Puis réessayez.
    pause
    exit /b 1
)

REM Aller dans le répertoire du jeu
cd /d "%~dp0"

REM Configurer le pilote audio pour éviter les erreurs WASAPI
set SDL_AUDIODRIVER=directsound

REM Lancer le jeu
python launch_game.py

REM Si le jeu se ferme, afficher un message
if errorlevel 1 (
    echo.
    echo Le jeu s'est fermé. Si vous avez des problèmes, essayez:
    echo python -m main.main
)

pause