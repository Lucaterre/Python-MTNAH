"""
CLI iiifquery
#MTNAH
@15/01/2020

iiifquery est un outil en ligne de commande qui permet à l'aide d'un identifiant ARK BNF
d'afficher l'ensemble des métadonnées sur l'objet décrit en JSON et de générer un fichier
CSV avec comme valeurs : Numéro, nom de la page, lien vers l'image, largeur, longueur

"""

#Import des bibliothèques

import csv
import requests
import click

#On écrit les fonctions

def iiif_csv(ark, nom_csv):
    """

    :param ark: lien ark
    :param nom_csv: nom du fichier .csv à créer
    :return: .csv
    """
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
        for canvas in data["sequences"][0]["canvases"]:
            numero += 1
            nom_de_page = canvas["label"]
            lien_image = canvas["images"][0]["resource"]["@id"]
            largeur = canvas["width"]
            longueur = canvas["height"]
            csv_writer.writerow([numero, nom_de_page, lien_image, largeur, longueur])

    return None

@click.command()
@click.argument("ark", type=str)
@click.argument("nom_csv", type=str) # Un décorateur argument par argument
def run_ifff_csv(ark, nom_csv): # On change le nom ici pour conserver la fonction "normale", sinon on l'écraserait
    """
    ************************  IIIF QUERY *******************************

    Outil en ligne de commande qui qui affiche dans un csv
    les métadonnées de l'objet décrit sur Gallica en Json

    ARK : rentrer l'ARK BNF

    NOM_CSV : nom du fichier csv de sortie contenant les métadonnées :
    numero, nom_de_page, lien_image, largeur, longueur

    ********************************************************************
    """
    iiif_csv(ark, nom_csv)

# Et on oublie pas de lancer la fonction
if __name__ == "__main__":
    run_ifff_csv()