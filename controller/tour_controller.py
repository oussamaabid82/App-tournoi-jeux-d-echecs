from tinydb import TinyDB
from models.tour_model import TourModel
from models.match_model import MatchModel
from models.player_model import PlayerModel
from view.tour_view import TourView
from view.match_view import MatchView


rounds_list = []
players_list = []
tour_creer = 0

class TourController:
    def __init__(self):
        self.tourview = TourView()
        pass

    def sortPlayersByRanking(self):
        """Trier les joueurs en fonction de leur classement"""
        l = players_list
        list_sort = (sorted(l, key=lambda l:l[4]))
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
        
    def startTour(self):
        return self.tourview.startTourView()
         
    def creationMatch(self):
        match_list = self.genererPairOfPlayers()
        for match in match_list:
            return match
    
    def createRound(self):
        for i in range(len(players_list)-1):
            TourModel("Round")
            self.startTour()
            self.sortPlayersByRanking()            
            #match = self.creationMatch()
            match_list = self.genererPairOfPlayers()
            
            for match in match_list:
                MatchModel(match)
                MatchView.starMatchView(self)
                MatchView.playerMatch(self, match)

            #match = MatchModel(self.creationMatch())
    
    def save(self):
        db = TinyDB("db.json")
        table_tour = db.table("joueurs")
        table_tour.truncate()	# clear the table first
        table_tour.insert_multiple(TourModel.serialization_tour(self))
        return table_tour