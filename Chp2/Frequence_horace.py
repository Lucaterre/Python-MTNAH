"""
on va vous demander de calculer la distribution totale des mots dans l'intégralité d'Horace de Corneille. Puis calculer la fréquence
relative des mots dans le texte. La fréquence relative consiste en le nombre de fois qu'un mot apparait divisé par le nombre total de mots.

"""

def ecrire_colonne(distribution, fichier):
    """ Ecrit dans un fichier chaque mot en clef de distribution avec la fréquence associée
    dans un fichier donné.

    :param distibution: Dictionnaire où la clef est un mot et la valeur le nombre d'occurrence
    :type distribution: dict
    :param fichier: Fichier ouvert pour l'écriture
    :type fichier: TextIOWrapper
    """
    fichier.write("Mot;Distribution\n")
    for mot, frequence in distribution.items():
        fichier.write(mot + ";" + str(frequence) + '\n')


# Ouvrir le fichier et stocker son contenu

with open(
        "data/horace.txt") as fichier_text:  # ouverture du texte est assignation a une variable, le with évite d'oublier le .close()
    texte = fichier_text.read()

# Nettoyer le texte

texte = texte.lower()  # transformer les maj en min .lower()
ponctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`'
for marqueur in ponctuation:
    texte = texte.replace(marqueur, " ")

# Calculer la distribution

mots = texte.split()
distribution = {}

for mot in set(
        mots):  # je caste la liste mot en set (supprime les doublons, itérable, non ordonné) au lieu de le stocker dans une variable intermédiaire
    distribution[mot] = mots.count(mot)  # clé = mot / valeur = fréquence

frequence = list(distribution.items())

# Ouvrir le fichier `frequence_horace.txt` pour écrire

# with open("frequence_horace.txt", mode='w', encoding='utf-8') as fichier_final:
# Utiliser la fonction ecrire_colonne pour écrire dans ce fichier
#    ecrire_colonne(distribution, fichier_final)


# calculer la frequence relative dans le fichier frequence_horace.txt
distribution_relative = {}
total_mot = sum(list(distribution.values()))
total_mot = len(mots)

for mot, freq in distribution.items():
    distribution_relative[mot] = freq / total_mot
# On commence par calculer la frequence moyenne d'apparition des mots dans le texte
print(len(distribution))

with open("frequence_horace.txt", mode='w', encoding='utf-8') as fichier_final:
    # Utiliser la fonction ecrire_colonne pour écrire dans ce fichier
    ecrire_colonne(distribution_relative, fichier_final)