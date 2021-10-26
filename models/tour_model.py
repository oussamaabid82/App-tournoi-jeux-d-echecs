from tinydb import TinyDB
from datetime import datetime


match_list = []

class Tour:
    """Les dates et les heures de debut et de la fin de la tour sont générés automatiquement"""
    def __init__(self, nom_de_tour, date_de_debut=datetime.now().date(), heure_de_debut=datetime.now().time(), date_fin=datetime.now().date(), 
                heure_fin=datetime.now().time()
                ):
        self.nom_de_tour = nom_de_tour
        self.date_de_debut = date_de_debut
        self.heure_de_debut = heure_de_debut
        self.date_fin = date_fin
        self.heure_fin = heure_fin
    
    def sortPlayersByRanking(self):
        """Trier les joueurs en fonction de leur classement"""
        l = match_list
        list_sort = (sorted(l, key=lambda l:l[1]))
        return list_sort

    def dividePlayersList(self):
        """Divisez les joueurs en deux moitiés, une supérieure et une inférieure"""
        top_list = self.sortPlayersByRanking()[:int(len(self.sortPlayersByRanking())/2)]
        lower_list = self.sortPlayersByRanking()[int(len(self.sortPlayersByRanking())/2):]
        """Générer les paires de joueurs qui vont s'infronter au premier tour"""
        return (top_list, lower_list)
    
    def genererPairOfPlayers(self):
        pair_of_player = list(zip(self.dividePlayersList()[0], self.dividePlayersList()[1])) 
        return pair_of_player
       
    def createMatchesList(self):
        """liste des matchs"""
        liste_paire_des_joueurs = self.genererPairOfPlayers()
        return liste_paire_des_joueurs
    
    def enterMatchResults(self):
        """Saisir les resultat de chaque match  """
        list_of_pairs_more_result = []
        list_of_pairs = self.genererPairOfPlayers()
        for i in (range(len(list_of_pairs))):
            player_score1 = list(input(f"Veuillez saisir le score du joueur {list_of_pairs[i][0][0]}: "))
            player_score2 = list(input(f"Veuillez saisir le score du joueur {list_of_pairs[i][1][0]}: "))
            list = (list_of_pairs[i][0] + (player_score1)), (list_of_pairs[i][1] + (player_score2))
            print(list)
            list_of_pairs_more_result.append([list])
        return list_of_pairs_more_result
        
    def serialization_tour(self):
        serialization = {
            "nom": self.nom_de_tour,
            "date de debut": self.date_de_debut,
            "heure de debut": self.heure_de_debut,
            "date de la fin": self.date_fin,
            "heure de la fin": self.heure_fin
        }
        return serialization

    def save(self):
        db = TinyDB("db.json")
        table_tour = db.table("joueurs")
        table_tour.truncate()	# clear the table first
        table_tour.insert_multiple(self.serialization_tour)
        return table_tour