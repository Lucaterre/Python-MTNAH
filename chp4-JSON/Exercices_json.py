import json
import csv


# Je crééé une fonction pour afficher mes tweets à partir du Json

def affichage_tweets(index):
    """
    Docstring
    """
    Lien = "http://twitter.com/statuses/" + twitter_f["statuses"][index]["id_str"]
    Auteur = twitter_f['statuses'][index]['user']['screen_name']
    Date = twitter_f["statuses"][index]["user"]["created_at"]
    Tweet = twitter_f['statuses'][index]['text']
    return ([Lien, Auteur, Date, Tweet])


# Je crééé un fichier tab_tweet.csv avec l'en-tête : "Lien", "Auteur", "Date", "Tweet"

with open("/Users/lucasterriel/Desktop/Fichiers_Dev/Programation-ENC:autres/ENC-M2/Python-MTNAH/Data/tab_tweets.csv", "w") as csvfile:
    headwriter = csv.writer(csvfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator="\r\n")
    headwriter.writerow(["Lien", "Auteur", "Date", "Tweet"])

# J'écris les tweets de mon fichier json à l'aide d'une boucle dans mon tab_tweet.csv

with open("/Users/lucasterriel/Desktop/Fichiers_Dev/Programation-ENC:autres/ENC-M2/Python-MTNAH/Data/twitter.humanitesnumeriques.json") as json_file:
    twitter_f = json.load(json_file)
    index = 0
    for line in twitter_f['statuses']: #ne pas oublier l'index [] sinon il continue sur le document
        row = affichage_tweets(index)
        with open("/Users/lucasterriel/Desktop/Fichiers_Dev/Programation-ENC:autres/ENC-M2/Python-MTNAH/Data/tab_tweets.csv", "a") as csvfile:
            tweetwriter = csv.writer(csvfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL,
                                         lineterminator="\r\n")
            tweetwriter.writerow(row)
            index += 1

"""
Alternative propre : 

import json
import csv

def affichage_tweet(index, data):
    lien = "http://twitter.com/statuses/" + \
        data["statuses"][index]["id_str"]
    auteur = data["statuses"][index]["user"]["screen_name"]
    date = data["statuses"][index]["user"]["created_at"]
    tweet = data["statuses"][index]["text"]
    return [lien, auteur, date, tweet]

def affichage_propre(statut):
    lien = "http://twitter.com/statuses/" + statut["id_str"]
    auteur = statut["user"]["screen_name"]
    date = statut["created_at"]
    tweet = statut["text"]
    return [lien, auteur, date, tweet]

with open("data/json/twitter.humanitesnumeriques.json") as json_file:
    tweeter_f = json.load(json_file)

with open("tab_tweet.csv", mode="w") as csv_file:
    head_writer = csv.writer(csv_file)
    head_writer.writerow(["Lien", "Auteur", "Date", "Tweet"])
    
    for line in tweeter_f["statuses"]:
        row = affichage_propre(line)
        head_writer.writerow(row)



"""