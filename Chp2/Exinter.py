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
Code qui compte certains éléments apparaissant dans une liste. 
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

valeur = 0

for lettre in phrase:
    cle = lettre
    if cle not in my_dict:
        my_dict[cle] = valeur
        valeur = valeur + 1

print(my_dict)



#trouver le moyen d'afficher la phrase entière avec ses identifiants unique