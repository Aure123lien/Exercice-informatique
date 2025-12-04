# Exercice sur les fonctions en Python

# Fonction qui calcule le carré d'un nombre
def carre(nombre):
    return nombre * nombre

# Fonction qui additionne deux nombres
def addition(a, b):
    return a + b

# Fonction qui affiche un message de bonjour
def saluer(nom):
    print(f"Bonjour, {nom}!")

# Permet a ce que la personne qu'il l'utilise puisse écrirel lui meme les valeurs
nombre = int(input("Entrez un nombre pour calculer son carré : "))
print(f"Le carré de {nombre} est :", carre(nombre))

a = int(input("Entrez le premier nombre pour l'addition : "))
b = int(input("Entrez le deuxième nombre pour l'addition : "))
print(f"{a} + {b} =", addition(a, b))

nom = input("Entrez votre nom : ")
saluer(nom)
