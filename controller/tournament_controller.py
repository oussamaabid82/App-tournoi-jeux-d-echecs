from tinydb import TinyDB
from view.tournament_view import TournamentView
from models.tournament_model import TournamentModels

tournament_data = []
class TournamentContoller:

    def __init__(self):
        pass
    
    def startTournament(self):
        TournamentView.startView(self)
        reponse = input()
        if reponse == "y":
            return TournamentView.tournamentStar(self)
        else:
            return TournamentView.endView(self)

    def creationTournement(self):
        creation = TournamentView()
        list = creation.tournamentCreation()
        tournament = TournamentModels(list[0], list[1], list[2], list[3])
        tournament_data.append([tournament.nom, tournament.lieu, tournament.date_debut, 
        tournament.date_fin, tournament.nombre_de_tours])
        return tournament
   
    def showStartTournament(self):
        start_message = TournamentView.startMessage(self, (tournament_data[0][0]))
        return start_message

    def save(self):
        db = TinyDB("db.json")
        table_tournoi = db.table("joueurs")
        table_tournoi.truncate()	# clear the table first
        table_tournoi.insert_multiple(TournamentModels.serialisation_tournoi())
        return table_tournoi
