from tinydb import TinyDB
from models.tour_model import TourModel, players_list
from models.match_model import MatchModel
from models.player_model import PlayerModel
from view.tour_view import TourView
from view.match_view import MatchView



round_create = 0

class TourController:
    
    def __init__(self):
        pass
         
    """def creationMatch(self):
        tour_model = TourModel()
        match_list = tour_model.genererPairOfPlayers()
        for match in match_list:
                MatchModel(match)
                MatchView.starMatchView(self)
                MatchView.playerMatch(self, match)"""
    
    def createRound(self):
        tour_models = TourModel()
        TourView.startTourView(self,tour_models.nom_de_tour, round_create)
        tour_models.sortPlayersByRanking()
        match_model = MatchModel(tour_models.genererPairOfPlayers())
        match_model.creationMatch()
        match_view = MatchView()
        match_view.starMatchView()
        for match in match_model.creationMatch():
            match_view.playerMatch(match)
            match_view.endMatch()

    def save(self):
        db = TinyDB("db.json")
        table_tour = db.table("joueurs")
        table_tour.truncate()	# clear the table first
        table_tour.insert_multiple(TourModel.serialization_tour(self))
        return table_tour