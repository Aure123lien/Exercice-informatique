# Exercice un peu plus avancée sur les fonctions en Python

# Fonction qui permet de calculer la factorielle
def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n - 1)

# Fonction qui permet de calculer une puissance
def puissance(base, exposant=2):
    resultat = 1
    for _ in range(exposant):
        resultat *= base
    return resultat

# Fonction qui filtre les nombres pairs d'une liste
def filtrer_pairs(liste):
    return [x for x in liste if x % 2 == 0]

# Fonction qui applique une opération à chaque élément d'une liste
def appliquer_operation(liste, operation):
    return [operation(x) for x in liste]

# Cela permet que la personne intéragisse avec le programme
n = int(input("Entrez un nombre entier positif pour calculer sa factorielle : "))
print(f"Factorielle de {n} :", factorielle(n))

base = float(input("Entrez la base pour la puissance : "))
exposant = int(input("Entrez l'exposant (ou appuyez Entrée pour 2) : ") or 2)
print(f"{base} à la puissance {exposant} :", puissance(base, exposant))

liste_str = input("Entrez une liste de nombres séparés par des espaces pour filtrer les pairs : ")
liste = [int(x) for x in liste_str.split()]
print(f"Nombres pairs dans {liste} :", filtrer_pairs(liste))

# Utilisation de appliquer_operation avec une fonction lambda
carres = appliquer_operation([1, 2, 3, 4], lambda x: x**2)
print("Carrés de [1,2,3,4] :", carres)

