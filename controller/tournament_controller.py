from tinydb import TinyDB, Query
from view.tournament_view import TournamentView
from models.tournament_model import TournamentModels


class TournamentContoller:
    def __init__(self, players="", round="", matchs=""):
        self.players = players
        self.round = round
        self.matchs = matchs
        self.tournament = TournamentModels()
        self.tournament_view = TournamentView()

    def startTournament(self):
        answer = self.tournament_view.startView()
        return answer

    def creationTournement(self):
        list = self.tournament_view.tournamentCreation()
        self.tournament.__init__(list[0], list[1], list[2], list[3])
        #self.tournament.createTournamentList()
        #return self.tournament

    """def showStartTournament(self):
        start_message = self.tournament_view.startMessage(self.tournament_data[0][0])
        return start_message"""

    """def startReport(self):
        answer = self.tournament_view.showRaportStart()
        return answer"""

    def chooseRaportMenu(self):
        answer = self.tournament_view.chooseNumberInMenu()
        return answer
    
    def showStartTournament(self):
        self.tournament_view.tournamentStar()

    def createList(self):
        self.tournament.players_list = self.players
        self.tournament.tours_list = self.round
        self.tournament.match_list = self.matchs

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
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        tournament_table.insert(self.tournament.serialization_tournoi())
        return tournament_table

    def getTournament(self):
        self.save
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        self.tournament_view.messaageTournamentRaport()
        for i in tournament_table:
            self.tournament_view.showTournamentList(i["nom"])

    """def reportPlayerController(self):
        answer = self.tournament_view.playerList()
        liste = self.tournament.reportPlayerModel(answer)
        for player in liste:
            self.tournament_view.show(player.prenom)"""
    
    def showEndTournament(self):
        self.tournament_view.endView()