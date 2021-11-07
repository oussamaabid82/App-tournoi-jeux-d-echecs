from tinydb import TinyDB
from models.tour_model import TourModel
from models.match_model import MatchModel
from view.tour_view import TourView
from view.match_view import MatchView


class TourController:
    def __init__(self, players):
        self.players = players
        self.tour_view = TourView()
        self.match_view = MatchView()
          
    def createFirstRound(self):
        tour_models = TourModel()
        tour_models.createTourList()
        tour_models.players_list = self.players
        self.tour_view.startTourView(tour_models.nom_de_tour, len(tour_models.round_list))
        tour_models.sortPlayersByRanking()
        for pair in tour_models.genererPairOfPlayers():
            self.match_view.starMatchView()
            self.match_view.playerMatch(pair)
            self.match_view.endMatch()
            result = self.match_view.enterMatchResults(pair)
            match_model = MatchModel(result)
            match_model.creationMatchList()
            tour_models.match_list.append(result)
        return(tour_models.round_list)

    def createNextRound(self):
        for round in range(len(self.players)-2):
            tour_models = TourModel()
            tour_models.createTourList()
            tour_models.players_list = self.players
            self.tour_view.startTourView(tour_models.nom_de_tour, len(tour_models.round_list))
            for pair in tour_models.generatePaire():
                self.match_view.starMatchView()
                self.match_view.playerMatch(pair)
                self.match_view.endMatch()
                result = self.match_view.enterMatchResults(pair)
                match_model = MatchModel(result)
                match_model.creationMatchList()
                tour_models.match_list.append(result)
        
    def save(self):
        db = TinyDB("db.json")
        table_tour = db.table("joueurs")
        table_tour.truncate()	# clear the table first
        tour_model = TourModel()
        table_tour.insert_multiple(tour_model.serializationTour())  