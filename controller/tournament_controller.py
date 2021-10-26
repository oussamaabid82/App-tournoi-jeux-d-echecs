from view.tournament_view import TournamentView
from models.tournament_model import TournamentModels


class TournametContoller:
    def __init__(self):
        self.tournamentView = TournamentView()
    
    def startTournament(self):
        self.tournamentView.startView()
        reponse = input()
        if reponse == "y" or "Y":
            return self.tournamentView.tournamentStar()
        else:
            return self.tournamentView.endView()

    def creationTournement(self):
        creation = self.tournamentView.tournamentCreation()
        tournoi = TournamentModels(creation[0], creation[1], creation[2], creation[3])
        return tournoi
    
    def showStartTournament(self):
        start_message = self.tournamentView.startMessage()
        return start_message