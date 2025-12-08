# 2ème Exercice sur les Dictionnaires en Python

# Créez un dictionnaire nommé 'etudiants' où chaque clé est le nom d'un étudiant, et la valeur est un dictionnaire de matières avec leurs notes

etudiants = {
    "Alice": {"Math": 15, "Français": 12, "Histoire": 14},
    "Aurélien": {"Math": 10, "Français": 16, "Histoire": 13},
    "Charlie": {"Math": 18, "Français": 11, "Histoire": 17}
}

# Calculez et affichez la moyenne générale de chaque étudiant
print("Moyennes générales :")
for nom, notes in etudiants.items():
    moyenne = sum(notes.values()) / len(notes)
    print(f"{nom} : {moyenne:.2f}")

# Trouvez et affichez l'étudiant avec la meilleure moyenne en Mathématiques
meilleur_math = max(etudiants, key=lambda x: etudiants[x]["Math"])
print(f"Meilleur en Math : {meilleur_math} avec {etudiants[meilleur_math]['Math']}")

# Ajoutez une nouvelle matière "Sciences" avec des notes pour tous les étudiants
# Pour simplifier, ajoutons des notes fixes.
for nom in etudiants:
    etudiants[nom]["Sciences"] = 14  # ceci est une note fixe pour un exemple

# Créez une liste des étudiants triés par moyenne générale décroissante
def moyenne_etudiant(notes):
    return sum(notes.values()) / len(notes)

etudiants_tries = sorted(etudiants.items(), key=lambda x: moyenne_etudiant(x[1]), reverse=True)
print("Étudiants triés par moyenne décroissante :")
for nom, notes in etudiants_tries:
    moy = moyenne_etudiant(notes)
    print(f"{nom} : {moy:.2f}")

# Pour chaque matière il faut trouver l'étudiant avec la meilleure note
matieres = ["Math", "Français", "Histoire", "Sciences"]
for matiere in matieres:
    meilleur = max(etudiants, key=lambda x: etudiants[x].get(matiere, 0))
    print(f"Meilleur en {matiere} : {meilleur} avec {etudiants[meilleur][matiere]}")

# Calculez la moyenne de la classe pour chaques matières
print("Moyennes de classe par matière :")
for matiere in matieres:
    notes_matiere = [etudiants[nom][matiere] for nom in etudiants if matiere in etudiants[nom]]
    moyenne_classe = sum(notes_matiere) / len(notes_matiere)
    print(f"{matiere} : {moyenne_classe:.2f}")

# Utilisez un dictionnaire supplémentaire pour ajouter des informations comme l'âge de chaque étudiant
for nom in etudiants:
    etudiants[nom]["Âge"] = 20 

# Affichez toutes les informations
print("Informations complètes des étudiants :")
for nom, info in etudiants.items():
    print(f"{nom} : {info}")