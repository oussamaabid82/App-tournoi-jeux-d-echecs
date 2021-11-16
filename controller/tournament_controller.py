from typing import List
from tinydb import TinyDB, Query
from view.tournament_view import TournamentView
from models.tournament_model import TournamentModels


class TournamentContoller:
    def __init__(self, round="", matchs=""):

        self.round = round
        self.matchs = matchs
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

    def getRound(self):  
        number_tournament = []
        list_of_tournament = []
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        [number_tournament.append(number + 1) for number in range(len(tournament_table))]
        [list_of_tournament.append(tournament["nom"]) for tournament in tournament_table]
        liste = tuple(zip(number_tournament, list_of_tournament))
        for i in liste:
            self.tournament_view.show(i)
        number = self.tournament_view.chooseNumberOfTurnament()
        result = (tournament_table.get(doc_id=number))["liste des tours"]
        self.tournament_view.messageRoundsRaport()
        self.tournament_view.show(result)
        
    def getMatchs(self):   
        db = TinyDB("save/db.json")
        tournament_table = db.table("Tournament")
        self.tournament_view.messageMatchList()
        for i in tournament_table:
            self.tournament_view.showMatchsList(i["liste des matchs"])

    def showEndTournament(self):
        self.tournament_view.endView()
