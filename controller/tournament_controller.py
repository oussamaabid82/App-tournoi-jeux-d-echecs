from tinydb import TinyDB
from view.tournament_view import TournamentView
from models.tournament_model import TournamentModels


class TournamentContoller:
    tournament_data = []
    def __init__(self, players="", round=""):
        self.players = players
        self.round = round
        self.tournament = TournamentModels()
        self.tournament_view = TournamentView()
    
    def startTournament(self):
        answer = self.tournament_view.startView()
        return answer
       
    def creationTournement(self):
        list = self.tournament_view.tournamentCreation()
        self.tournament.__init__(list[0], list[1], list[2], list[3])
        self.tournament_data.append(
                                    [self.tournament.nom, self.tournament.lieu, 
                                    self.tournament.date_debut, 
                                    self.tournament.date_fin, self.tournament.nombre_de_tours]
                                    )
        self.tournament.createTournamentList()
        return self.tournament
    
    def showStartTournament(self):
        start_message = self.tournament_view.startMessage(self.tournament_data[0][0])
        return start_message
    
    def showEndTournament(self):
        self.tournament_view.endView()
    
    def startReport(self):
        answer = self.tournament_view.showRaportStart()
        return answer
    
    def chooseRaportMenu(self):
        answer = self.tournament_view.chooseNumberInMenu()
        return answer
    
    def createList(self):
        self.tournament.players_list = self.players
        self.tournament.tours_list = self.round

    def reportPlayerController(self):
        answer = self.tournament_view.playerList()
        liste = self.tournament.reportPlayerModel(answer)
        for player in liste: 
            self.tournament_view.show(player.prenom)

    def reportTournamentController(self):
        for tournament in self.tournament.tournamentList:
            self.tournament_view.showTournamentList(tournament.nom)
    
    def reportRoundController(self):
        for round in self.tournament.tours_list:
            self.tournament_view.showRoundList(round)
    
    def reportMatchListController(self):
        self.tournament_view.messageMatchList()
        for tour in self.tournament.tours_list:
            match_list = tour.match_list
        for match in match_list:
            self.tournament_view.showMatch(match[0].prenom, match[1].prenom)

    def save(self):
        db = TinyDB("db.json")
        table_tournoi = db.table("joueurs")
        table_tournoi.truncate()	# clear the table first
        table_tournoi.insert_multiple(TournamentModels.serialisation_tournoi())
        return table_tournoi