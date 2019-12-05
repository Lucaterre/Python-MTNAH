"""
Exercice final du chap.1 :

Le but de l'exercice est de faire un programme qui calcule et retourne le
nombre de 'a' présent dans le texte en prenant en compte la fréquence d'apparition des
mots dans ce dernier.

@ENC MTNAH

"""


distribution = {'1821': 1, '2006': 1, 'Depuis': 1, 'Enseignement': 1, 'Fondée': 1,
                'L': 1, 'Recherche': 1, 'Technologies': 1, 'a': 1, 'appliquées': 1,
                'aux': 1, 'chartes': 2, 'd': 1, 'dans': 1, 'de': 3, 'des': 2, 'du': 1,
                'en': 1, 'est': 2, 'et': 2, 'fondamentales': 1, 'formant': 1, 'formation': 1,
                'française': 1, 'grand': 1, 'grande': 1, 'histoire': 2, 'intitulé': 1, 'l': 6,
                'la': 3, 'le': 1, 'master': 1, 'ministère': 1, 'nationale': 2, 'numériques': 1,
                'ouvert': 1, 'par': 1, 'placée': 1, 'possède': 1, 'promotion': 1, 'sciences': 1,
                'sous': 1, 'spécialisée': 1, 'statut': 1, 'supérieur': 1, 'tutelle': 1, 'un': 1,
                'une': 2, 'vingtaine': 1, '«': 1, '»': 1, 'École': 3, 'Éducation': 1, 'à': 1, 'école': 1,
                'établissement': 1, 'étudiants': 1}

nombre_de_a = 0

liste_a = []

for c, v in distribution.items():
    if "a" in c:
        for i in range(v):
            liste_a.append(c)

for i in liste_a:
    nombre_de_a += i.count("a")

print("Le nombre de 'a' dans la distribution est de : ",nombre_de_a)

# Ce code vérifie
if nombre_de_a == 30:
    print('Bien joué!')
else:
    print('La réponse est incorrecte, essaye encore!')