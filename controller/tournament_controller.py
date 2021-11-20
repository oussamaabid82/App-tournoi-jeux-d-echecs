from tinydb import TinyDB
from view.tournament_view import TournamentView
from models.tournament_model import TournamentModels


class TournamentContoller:
    def __init__(self, players="", round="", matchs=""):
        self.round = round
        self.matchs = matchs
        self.players = players
        self.tournament = TournamentModels()
        self.tournament_view = TournamentView()

    def startTournament(self):
        answer = self.tournament_view.startView()
        return answer

    def creationTournement(self):
        list = self.tournament_view.tournamentCreation()
        self.tournament.nom = list[0]
        self.tournament.lieu = list[1]
        self.tournament.date_debut = list[2]
        self.tournament.date_fin = list[3]

    def chooseRaportMenu(self):
        answer = self.tournament_view.chooseNumberInMenu()
        return answer
    
    def showStartTournament(self):
        self.tournament_view.tournamentStar()

    def createList(self):
        self.tournament.players_list = self.players
        self.tournament.tours_list = self.round
        self.tournament.match_list = self.matchs

    def save(self):
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        tournament_table.insert(self.tournament.serialization_tournoi())
        return tournament_table

    def getTournament(self):
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        self.tournament_view.messaageTournamentRaport()
        for i in tournament_table:
            self.tournament_view.showTournamentList(i["nom"])
        
    def listTournamentWitnNumbers(self):
        number_tournament = []
        list_of_tournament = []
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        [number_tournament.append(number + 1) for number in range(len(tournament_table))]
        [list_of_tournament.append(tournament["nom"]) for tournament in tournament_table]
        liste = tuple(zip(number_tournament, list_of_tournament))
        return liste

    def getPlayersInTournament(self):
        name_list = []
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        for i in self.listTournamentWitnNumbers():
            self.tournament_view.showListTournamentWithNumber(i[0], i[1])
        number = self.tournament_view.chooseNumberOfTournament()
        result = (tournament_table.get(doc_id=number))["list des joueurs"]
        for i in result:
            name_list.append((i[0], i[1]))
        l = name_list
        list_sort = (sorted(l, key=lambda l:l))
        self.tournament_view.messagePlayerSortedInTournament()
        for player in list_sort:
            self.tournament_view.showPlayerName(player[0], player[1])

    def getRound(self):  
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        self.tournament_view.messageToursInTournament()
        for i in self.listTournamentWitnNumbers():
            self.tournament_view.showListTournamentWithNumber(i[0], i[1])
        
        number = self.tournament_view.chooseNumberOfTournament()
        result = (tournament_table.get(doc_id=number))["liste des tours"]
        
        self.tournament_view.messageRoundsRaport()
        for round in result:
            self.tournament_view.show(round)

    def getMatchs(self):
        number_match = []
        list_of_tournament = []  
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        [number_match.append(number + 1) for number in range(len(tournament_table))]
        [list_of_tournament.append(tournament["nom"]) for tournament in tournament_table]
        liste = tuple(zip(number_match, list_of_tournament))
        self.tournament_view.messageMatchInTournament()
        self.tournament_view.messaageTournamentRaport()
        for i in liste:
            self.tournament_view.showListTournamentWithNumber(i[0], i[1])
        number = self.tournament_view.chooseNumberOfTournament()
        result = (tournament_table.get(doc_id=number))["liste des matchs"]
        self.tournament_view.messageMatchList()
        for i in result:
            self.tournament_view.showMatch(i[0], i[1])
        
    def showEndTournament(self):
        self.tournament_view.endView()
