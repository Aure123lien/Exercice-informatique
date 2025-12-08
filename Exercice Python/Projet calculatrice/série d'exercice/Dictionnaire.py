# 1 Exercice sur les Dictionnaires en Python

# Créez un dictionnaire nommé "invites" où les clés seront les noms des invités et les valeurs sont leurs âges

invites = {
    "Alice": 25,
    "Aurélien": 30,
    "Charlie": 22
}

# Affichez l'âge d'Alice en utilisant "invites"
print("Âge d'Alice :", invites["Alice"])

# Ajoutez un nouvel invité nommé qui sera "David" avec l'âge 28 ans
invites["David"] = 28

# Vérifiez si le nom Eve est dans le dictionnaire, Si c'est non, il faut l'ajouter avec l'âge sont age qui sera de 26 ans
if "Eve" not in invites:
    invites["Eve"] = 26

# Affichez tous les invités et leurs âges en utilisant une boucle
print("Liste des invités :")
for nom, age in invites.items():
    print(f"{nom} : {age} ans")

# Supprimez Aurélien de la liste car il ne peut pas venir
del invites["Aurélien"]

# Affichez le nombre total d'invités qui restera a la fin
print("Nombre d'invités restants :", len(invites))