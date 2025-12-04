# Exercice sur les fonctions en Python plus compliqué

# Fonction avec *args pour calculer la somme de plusieurs nombres
def somme(*args):
    return sum(args)

# Fonction avec **kwargs pour créer un profil
# Kwargs c'est une fonction qui permet de recevoir un nombre de variable d'arguments nommés sous forme d'un dictionnaire
def creer_profil(**kwargs):
    return kwargs

# c'est une fonction qui crée un compteur
def compteur():
    count = 0
    def incrementer():
        nonlocal count
        count += 1
        return count
    return incrementer

# Fonction pour la suite de Fibonacci
# Précision de ce que c'est Fibonacci est une suite mathématique où chaque nombre est la somme des deux précédents
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Fonction qui va traiter une liste de dictionnaires
def moyenne_notes(etudiants):
    moyennes = {}
    for etudiant in etudiants:
        notes = etudiant['notes']
        moyenne = sum(notes) / len(notes) if notes else 0
        moyennes[etudiant['nom']] = moyenne
    return moyennes

# Ce bloc permet a ce que l'utilisataire note lui meme s'est réponse
print("Somme de plusieurs nombres")
nombres_str = input("Entrez des nombres séparés par des espaces : ")
nombres = [float(x) for x in nombres_str.split()]
print(f"Somme : {somme(*nombres)}")

print("\nCréation de profil")
nom = input("Nom : ")
age = int(input("Âge : "))
ville = input("Ville : ")
profil = creer_profil(nom=nom, age=age, ville=ville)
print(f"Profil créé : {profil}")

print("\nCompteur")
mon_compteur = compteur()
for i in range(3):
    print(f"Compteur : {mon_compteur()}")

print("\nFibonacci")
n = int(input("Entrez un nombre pour Fibonacci : "))
print(f"Fibonacci de {n} : {fibonacci(n)}")