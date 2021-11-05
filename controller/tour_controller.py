from tinydb import TinyDB
from models.tour_model import TourModel
from models.match_model import MatchModel
from view.tour_view import TourView
from view.match_view import MatchView


class TourController:
    def __init__(self, players):
        self.players = players
          
    def createFirstRound(self):
        tour_models = TourModel()
        tour_models.createTourList()
        tour_models.players_list = self.players
        TourView.startTourView(self,tour_models.nom_de_tour)
        tour_models.sortPlayersByRanking()
        for pair in tour_models.genererPairOfPlayers():
            match_view = MatchView()
            match_view.starMatchView()
            match_view.playerMatch(pair)
            match_view.endMatch()
            result = match_view.enterMatchResults(pair)
            match_model = MatchModel(result)
            match_model.creationMatch()
            tour_models.match_list.append(result)
        
    def createNextRound(self):
        for round in range(len(self.players)-2):
            tour_models = TourModel()
            tour_models.createTourList()
            tour_models.players_list = self.players
            TourView.startTourView(self, tour_models.nom_de_tour)
            for pair in tour_models.generatePaire():
                match_view = MatchView()
                match_view.starMatchView()
                match_view.playerMatch(pair)
                match_view.endMatch()
                result = match_view.enterMatchResults(pair)
                match_model = MatchModel(result)
                match_model.creationMatch()
                tour_models.match_list.append(result)
        
    def save(self):
        db = TinyDB("db.json")
        table_tour = db.table("joueurs")
        table_tour.truncate()	# clear the table first
        tour_model = TourModel()
        table_tour.insert_multiple(tour_model.serializationTour())  