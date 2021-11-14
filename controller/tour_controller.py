from models.tour_model import TourModel
from models.match_model import MatchModel
from view.tour_view import TourView
from view.match_view import MatchView


class TourController:
    def __init__(self, players):
        self.players = players
        self.match_list = []
        self.tour_view = TourView()
        self.match_view = MatchView()
        self.tour_models = TourModel("Ronde 1")

    def createFirstRound(self):
        """Création de la premiére round """
        self.tour_models.createTourList()
        self.tour_models.players_list = self.players
        self.tour_view.startTourView(self.tour_models.nom_de_tour)
        self.tour_models.sortPlayersByRanking()
        self.match_view.starMatchView()
        for pair in self.tour_models.genererPairOfPlayers():
            self.match_view.playerMatch(pair)
            
        for pair in self.tour_models.genererPairOfPlayers():
            result = self.match_view.enterMatchResults(pair)
            match_model = MatchModel(result)
            self.match_list.append(result)
        self.tour_view.finishTour(self.tour_models.nom_de_tour)
        return(self.tour_models.round_list)

    def createNextRound(self):
        n=1
        for round in range(len(self.players)-2):
            n+=1
            nom = "Ronde" + str(n)
            tour_models = TourModel(nom)
            tour_models.createTourList()
            tour_models.players_list = self.players
            self.tour_view.startTourView(tour_models.nom_de_tour)
            self.match_view.starMatchView()
            for pair in tour_models.generatePaire():
                self.match_view.playerMatch(pair)
                
            for pair in tour_models.generatePaire():
                result = self.match_view.enterMatchResults(pair)
                match_model = MatchModel(result)
                self.match_list.append(result)
            self.tour_view.finishTour(tour_models.nom_de_tour)

    def updatePlayerClassement(self):
        player_list = self.tour_models.updatePlayerClassementModel()
        for player in player_list:
            nom = player.nom_de_famille
            prenom = player.prenom
            classement = player.classement
            self.tour_view.showUpdatePlayerClassement(nom, prenom, classement)
