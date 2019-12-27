#Exercice 1 : combien de fois se trouve la lettre "e" dans un texte

nombre_de_e = 0
# Votre code ici

for lettre in texte:
    if "e" == lettre:
        nombre_de_e += 1
print(nombre_de_e)

# Ce code vérifiera ce que vous avez écrit
assert nombre_de_e == 182, "On devrait trouver 180 'e'"

fichier_ouvert.close()

#Exercice 2

"""
Programme qui compte certains éléments apparaissant dans une liste. 
Écrivez un bloc de code qui définit la variable nombre_de_resultats 
et compte combien de fois le mot à (assigné à a_compter) 
apparaît dans la liste de mots appelée mots.
"""
    
mots = texte.split()
a_compter = "à"
ex_a = "Là,"


for i in mots:
    nombre_de_resultats = mots.count(a_compter)
    if ex_a in mots:
        nombre_de_resultats = nombre_de_resultats -1
print(nombre_de_resultats)


# Ce test ne devrait pas lancer d'erreur si tout va bien
assert nombre_de_resultats == 6, "Il devrait y avoir 6 résultats"

#Exercice spécial du chat qui court...

phrase = "Le petit chat court dans la prairie"

my_dict = {}
list(phrase)
valeur = 0

index = 0

for lettre in phrase:
    cle = lettre
    if cle not in my_dict:
        my_dict[cle] = valeur
        valeur += 1

resultat =[]

for lettre in phrase:
    resultat.append(my_dict[lettre])
print(resultat)
print(my_dict)


"""
Alternative pour chat qui court... :

phrase = "Le petit chat court dans la prairie"

gaffiot = []

for char in phrase:
    if char not in gaffiot:
      gaffiot[char] = len(gaffiot)

for char in phrase:
    resultat.append(gaffiot[char])
print(resultat)

si phrase.split() => on coupe la phrase par mot et non par char

"""

#SERIE D'EXERCICES INTERMEDIAIRES SUR LES FONCTIONS

"""
Exercice 1 : Créer une fonction qui conjuge un verbe
du premier groupe au présent de l'indicatif
à la personne demandée

"""

def conjugue(verbe, clé):
    """
    Conjugue un verbe par extraction du radical et ajout de la terminaison
    stocké dans un dictionnaire
    :param verbe: verbe a conjuguer
    :type verbe : CHAR
    :param clé: clé du dictionnaire de terminaisons
    :type clé : INT
    :returns : verbe(VAR verbe) conjuguer à la personne demandé(INT clé)
    :rtype : CHAR
    :
    """
    terminaisons = {2: "es", 5: "ez", 3: "ons"}
    radical = verbe[:-2]
    verbe_conj = radical + terminaisons[clé]
    return  verbe_conj


print(conjugue("manger", 2))
print(conjugue("balayer", 5))
print(conjugue("travailler", 3))

# Vérification
assert conjugue("manger", 2) == "manges"
assert conjugue("balayer", 5) == "balayez"
assert conjugue("travailler", 3) == "travaillons"

