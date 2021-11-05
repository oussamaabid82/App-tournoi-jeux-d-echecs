from datetime import datetime

class TourModel:
    players_list = []
    nombre_of_round = []

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
        self.match_list = []
    
    def createTourList(self):
        self.nombre_of_round.append(TourModel())

    def sortPlayersByRanking(self):
        """Trier les joueurs en fonction de leur classement"""
        l = self.players_list
        list_sort = (sorted(l, key=lambda l:l.classement))
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
    
    def genererPairOfPlayers(self):
        """Générer les paires de joueurs qui vont s'infronter au premier tour"""   
        pair_of_player = list(zip(self.topPlayersList(), self.lowerPlayerList())) 
        return pair_of_player

    def sortPlayersByPoints(self):
        l = self.players_list
        list_sort = (sorted(l, key=lambda l:sum(l.score)))
        return list_sort
    
    def generatePaire(self):
        list_sort= self.sortPlayersByPoints()
        list1 = reversed(list_sort[1::2])
        list2 = reversed(list_sort[::2])
        paire = list(zip(list1, list2))
        for i in paire:
            for y in i:
                print (y.score)
        return paire

    def serializationTour(self):
        serialization = {
            "nom": self.nom_de_tour,
            "date de debut": self.date_de_debut,
            "heure de debut": self.heure_de_debut,
            "date de la fin": self.date_fin,
            "heure de la fin": self.heure_fin
        }
        return serialization