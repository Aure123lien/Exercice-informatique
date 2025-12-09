@echo off
echo Compilation du jeu...
javac TicTacToe.java
if %errorlevel% neq 0 (
    echo Erreur de compilation. Assurez-vous que Java est installé.
    pause
    exit /b 1
)
echo Lancement du jeu...
java TicTacToe
pause