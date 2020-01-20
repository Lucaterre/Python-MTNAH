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
    stockée dans un dictionnaire
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

"""

Alternative Exercice 1 : 

def conjugue(infinitif, personne):
    radical = infinitif[:-2]
    suffixe = ["e","es","e","ons","ez","ent"]
    return radical + suffixe[personne-1]

"""


print(conjugue("manger", 2))
print(conjugue("balayer", 5))
print(conjugue("travailler", 3))

# Vérification
assert conjugue("manger", 2) == "manges"
assert conjugue("balayer", 5) == "balayez"
assert conjugue("travailler", 3) == "travaillons"

"""
Exercice 2 : Créer une fonction qui conjuge un verbe du premier groupe au temps de l'indicatif demandé 
(entre présent et imparfait) à la personne demandée

"""

def conjugue(verbe, clé, temps):
    """
    Conjugue un verbe par extraction du radical et ajout de la terminaison
    stockée dans un dictionnaire selon une propriété temps de conjugaison (présent ou imparfait)
    :param verbe: verbe a conjuguer
    :type verbe : CHAR
    :param clé: clé du dictionnaire de terminaisons
    :type clé : INT
    :returns : verbe(VAR verbe) conjuguer à la personne demandé(INT clé)
    :rtype : CHAR
    :
    """
    terminaisons_present = {1: "e", 2: "es", 3: "e", 4: "ons", 5: "ez", 6: "ent"}
    terminaisons_imparfait = {1: "ais", 2: "ais", 3: "ait", 4: "ions", 5: "iez", 6: "aient"}
    radical = verbe[:-2]
    if temps == "présent":
        verbe_conj = radical + terminaisons_present[clé]
    if temps == "imparfait":
        verbe_conj = radical + terminaisons_imparfait[clé]
    return  verbe_conj


print(conjugue("manger", 2, "présent"))
print(conjugue("balayer", 5, "présent"))
print(conjugue("travailler", 4, "imparfait"))

# Vérification
assert conjugue("manger", 2, "présent") == "manges"
assert conjugue("balayer", 5, "présent") == "balayez"
assert conjugue("travailler", 4, "imparfait") == "travaillions"


"""
Alternative Exercice 2 : 

def conjugue(infinitif, personne, temps):
    radical = infinitif[:-2]
    suffixes = {
        "présent": ["e","es","e","ons","ez","ent"],
        "imparfait": ["ais","ais","ait","ions","iez","aient"]
    }
    mediofix = ""
    if temps == "imparfait":
        if radical.endswith("g"):
            mediofix = "e"
        
    return radical + mediofix + suffixes[temps][personne-1]


"""

"""
Exercice 3 : Créer une fonction qui détermine le verbe, les temps et les personnes possible d'un verbe conjugé au premier groupe
"""

def analyse(verbe):
    suffixes = {
        "présent": ["e","es","e","ons","ez","ent"],
        "imparfait": ["ais","ais","ait","ions","iez","aient"]
    }
    possible = []
    for temps, personnes in suffixes.items():
        for personne, suff in enumerate(personnes):
            if verbe.endswith(suff):
                radical = verbe[:-len(suff)]
                possible.append((radical+"er", personne+1, temps))
    return possible

# Vérification
assert analyse("mange") == [("manger", 1, "présent"), ("manger", 3, "présent")]
assert analyse("balayez") == [("balayer", 5, "présent")]
assert analyse("travaillions") == [("travaillier", 4, "présent"), ("travailler", 4, "imparfait")]

"""
Exercice 4 : 

Créer une fonction qui pour un fichier texte donné compte le nombre de mots et retourne les 5 mots les plus fréquents.
"""


def top5(fichier):
    decompte = {}
    with open(fichier) as f:
        texte = f.read()
    mots = texte.split()
    uniques = set(mots)
    for mot in uniques:
        decompte[mot] = mots.count(mot)

    # On récupère les decomptes et on trie uniquement les nombres
    values = sorted(list(decompte.values()))
    # On garde les 5 meilleurs
    values = values[-5:]

    # On tourne sur le decompte et on garde seulement les 5 meilleurs valeurs
    # On préremplie une liste avec 5 valeurs vides
    # Cela nous permet de changer les valeurs à des index précis
    top = [0, 0, 0, 0, 0]
    for mot, cnt in decompte.items():
        # Si le decompte existe, on récupère l'index
        if cnt in values:
            index = values.index(cnt)
            top[index] = (mot, cnt)

    return top


""" Solution avancée
def recupere_deuxieme_valeur(element):
    \""" Sorted prend un paramètre optionel key qui doit être une fonction
    prenant chacun des élements d'une liste et renvoyant la valeur qui servira
    à trier dans l'ordre croissant.
    \"""
    return element[1]


def top5bis(fichier):
    decompte = {}
    with open(fichier) as f:
        texte = f.read().lower()
    mots = texte.split()
    uniques = set(mots)
    for mot in uniques:
        decompte[mot] = mots.count(mot)

    top = []
    for mot, cnt in decompte.items():
        top.append((mot, cnt))

    # https://docs.python.org/fr/3.8/howto/sorting.html
    # CF reverse pour ordonner dans le sens inverse
    return sorted(top, key=recupere_deuxieme_valeur)[-5:]
"""
# Vérification
print(top5("../data/Ballade.XXVIII.dePisan.txt"))
assert top5("../data/Ballade.XXVIII.dePisan.txt") == [('que', 5), ('de', 5), ('car', 6), ('ne', 7), ('vous', 10)]
assert top5("../data/lettre.louisemichel.txt") == [('vous', 12), ('ne', 13), ('me', 13), ('que', 15), ('je', 30)]

#SERIE D'EXERCICES INTERMEDIAIRES SUR LES FONCTIONS

"""

EXERCICE 1 :

Sachant que la fonction et les paramètres glob("../data/*.txt") dans la première cellule retourne l'ensemble des fichiers disponibles finissant par *.txt dans ../data:

    Comptez le nombre de chaque mot dans chaque texte
    Combien de mots ne sont présents que dans un texte ?
"""

from glob import glob

# On prépare les dictionnaores finaux
mots_total = {}
mots_par_texte = {}
# On boucle sur l'ensemble des fichiers
for file in glob("../data/*.txt"):
    print("Reading {}".format(file))
    with open(file) as fio:
        # On lit les fichiers
        texte = fio.read()
    # On trie
    mots = texte.lower().replace("'", " ").replace("-", " ").replace(",", " ") \
        .replace(".", " ").replace("’", " ").replace("?", " ").split()
    mots_par_texte[file] = {}
    for mot in set(mots):
        decompte = mots.count(mot)
        # Si le mot n'a pas encore été rencontré
        # On crée leur entrée
        if mot not in mots_total:
            mots_total[mot] = 0
        # On incrémente le nombre de mots
        mots_total[mot] += decompte
        # Cependant, il est forcément absent de mots_par_texte
        mots_par_texte[file][mot] = decompte

# On crée un dictionnaire où l'on stockera les mots n'apparaissant qu'une fois
mots_specifiques = {}
for mot in mots_total:
    dans_combien_texte = []
    for texte in mots_par_texte:
        if mot in mots_par_texte[texte]:
            dans_combien_texte.append(texte)
    if len(dans_combien_texte) == 1:
        mots_specifiques[mot] = dans_combien_texte

print("Il y a {} mots spécifiques à un texte, soit {:.2f}% des mots rencontrés".format(
    len(mots_specifiques),
    len(mots_specifiques) / len(mots_total) * 100
))
print(sorted(list(mots_specifiques.keys())))

"""

EXERCICE 2 :
À partir de la variage text, créer un fichier lesdeuxamants.xml qui soit de la TEI valide. Le corps du 
texte doit contenir une div, un head, des lgs et des ls. Les ls seront numérotées via l'attribut n.
"""
# Exécuter mais ne pas modifier
with open("../data/lesdeuxamants.txt") as f:
    texte = f.read()
    # On crée un template pour plus tard, on remplira le contenu de
    # {reste_du_contenu} plus tard
    contenu = """<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
      <fileDesc>
         <titleStmt>
            <title>Title</title>
         </titleStmt>
         <publicationStmt>
            <p>Publication information</p>        
         </publicationStmt>
         <sourceDesc>
            <p>Information about the source</p>
         </sourceDesc>
      </fileDesc>
  </teiHeader>
  <text>
      <body>
          {reste_du_contenu}
      </body>
  </text>
</TEI>
"""
    le_reste = []
    last_line_was_empty = False
    text_has_started = False
    for line in texte.split("\n"):
        if line.startswith("#"):
            line = line[1:]  # On enleve le #
            line = line.strip()  # On supprime les espaces autours via strip
            le_reste.append("<head>" + line + "</head>")
            le_reste.append("<lg>")
        else:

            line = line.strip()
            if line:  # Si on a une ligne qui n'est pas vide une fois les espaces en surplus supprimés
                le_reste.append("<l>" + line + "</l>")
                text_has_started = True
            elif text_has_started:
                if last_line_was_empty and le_reste[-1] != "</lg><lg>":
                    le_reste.append("</lg><lg>")
                last_line_was_empty = True

    if le_reste[-1] == "</lg><lg>":
        le_reste[-1] = "</lg>"
    else:
        le_reste[-1] = "</lg>"
    contenu = contenu.format(reste_du_contenu="\n".join(le_reste))
with open("../data/lesdeuxamants.xml", "w") as f:
    f.write(contenu)