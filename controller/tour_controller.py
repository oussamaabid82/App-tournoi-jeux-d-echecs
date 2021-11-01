from tinydb import TinyDB
from models.tour_model import TourModel, match_list
from models.match_model import MatchModel
from models.player_model import PlayerModel
from view.tour_view import TourView
from view.match_view import MatchView



class TourController:
    round_create = 0
    
    def __init__(self):
        pass
          
    def createRound(self):
        self.round_create += 1
        tour_models = TourModel()
        TourView.startTourView(self,tour_models.nom_de_tour, self.round_create)
        tour_models.sortPlayersByRanking()
        for pair in tour_models.genererPairOfPlayers():
            match_model = MatchModel(pair)
            match_model.creationMatch()
            match_view = MatchView()
            match_view.starMatchView()
            match_view.playerMatch(pair)
            match_view.endMatch()
            result = match_view.enterMatchResults(pair)
            match_list.append(result)

    def save(self):
        db = TinyDB("db.json")
        table_tour = db.table("joueurs")
        table_tour.truncate()	# clear the table first
        table_tour.insert_multiple(TourModel.serialization_tour(self))
        return table_tour