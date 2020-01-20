"""
Exercice compréhension
issu du projet EHRI ( https://portal.ehri-project.eu/api/v1#api-usage-python ).

"""

import requests

def scope_content(url):
    print("Fetching: " + url)
    #Une fait une requête sur URL (methode GET) et r = réponse
    r = requests.get(url)
    #On utilise la méthode JSON pour récupérer le contenu JSON comme valeurs python
    data = r.json()
    #On créé une liste vide
    simplified = []
#Boucler sur des données
#D'après la lecture d'un exemple dans le fichier JSON, ce sont des documents
    for item in data["data"]:
        try:
            # fetch (aller chercher) the ID and first description... bloc a essayé
            identifier = item["id"]
            desc = item["attributes"]["descriptions"][0]
            name = desc["name"]
            scopecontent = desc["scopeAndContent"]
            simplified.append((identifier, scopecontent, name))
        except (IndexError, KeyError) as e: #bloc a executé en cas d'erreur #except Exception
            #print(e,type(e))
            # no description or scope and content found... skipping...
            pass #try...except est la rustine pour qu'un code fonctionne

    # fetch the next page of data...
    if data.get("links") and data["links"].get("next"):
        simplified += scope_content(data["links"]["next"]) #paramètre URL dans scope_content
    return simplified #fonction recursive renvoie scope_content

scope_content("https://portal.ehri-project.eu/api/v1/search?type=DocumentaryUnit&q=Potato")

"""
Exercice def_ifff

    Ouvrir http://gallica.bnf.fr/iiif/ark:/12148/btv1b84259980/manifest.json
    Comprendre le format de http://gallica.bnf.fr/iiif/ark:/12148/btv1b84259980/manifest.json
    En Python, faire une fonction qui prend un identifiant ark BNF et qui:
        Affiche l'ensemble des métadonnées sur l'objet décrit en JSON
        Génère un fichier CSV avec les colonnes Numéro | Nom de Page | Lien image | Largeur | Longueur en fonction d'un argument nom_csv


"""

import csv
import requests


def iiif_csv(ark, nom_csv):
    colonnes = ["Numéro", "Nom de Page", "Lien image", "Largeur", "Longueur"]
    # Complétez avec la documentation'
    # LA REPONSE pour la requete HTTP GET sur l'adresse composee par l'ARK
    r = requests.get("http://gallica.bnf.fr/iiif/" + ark + "/manifest.json")
    # Permet de lire le contenu de la reponse json en tant que python
    # CAD de parser le body de la reponse http
    data = r.json()

    for x in data["metadata"]:
        print(x["label"] + " " + x["value"])

    with open(nom_csv, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(colonnes)
        numero = 0
        for canvases in data["sequences"][0]["canvases"]:
            numero += 1
            nom_de_page = canvases["label"]
            lien_image = canvases["images"][0]["resource"]["@id"]
            largeur = canvases["width"]
            longueur = canvases["height"]
            csv_writer.writerow([numero, nom_de_page, lien_image, largeur, longueur])

    return None


# Testez le code ici
iiif_csv("ark:/12148/btv1b84259980", "pages.csv")