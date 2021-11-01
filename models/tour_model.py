from datetime import datetime


players_list = []
match_list = []

class TourModel:
    """Les dates et les heures de debut et de la fin de la tour sont générés automatiquement"""
    def __init__(self, nom_de_tour="Ronde",
                date_de_debut=datetime.now().date(), 
                heure_de_debut=datetime.now().time(), 
                date_fin=datetime.now().date(), 
                heure_fin=datetime.now().time()
                ):
        self.nom_de_tour = nom_de_tour
        self.date_de_debut = date_de_debut
        self.heure_de_debut = heure_de_debut
        self.date_fin = date_fin
        self.heure_fin = heure_fin
    

    def sortPlayersByRanking(self):
        """Trier les joueurs en fonction de leur classement"""
        l = players_list
        list_sort = (sorted(l, key=lambda l:l[0].classement))
        return list_sort

    def topPlayersList(self):
        """Divisez les joueurs en deux moitiés, une supérieure et une inférieure"""
        list_sort = self.sortPlayersByRanking()
        top_list = list_sort[:int(len(list_sort)/2)]
        return top_list

    def lowerPlayerList(self):
        list_sort = self.sortPlayersByRanking()
        lower_list = list_sort[int(len(list_sort)/2):]
        return lower_list
    
        """Générer les paires de joueurs qui vont s'infronter au premier tour"""   
    def genererPairOfPlayers(self):
        pair_of_player = list(zip(self.topPlayersList(), self.lowerPlayerList())) 
        return pair_of_player

    

    def serialization_tour(self):
        serialization = {
            "nom": self.nom_de_tour,
            "date de debut": self.date_de_debut,
            "heure de debut": self.heure_de_debut,
            "date de la fin": self.date_fin,
            "heure de la fin": self.heure_fin
        }
        return serialization