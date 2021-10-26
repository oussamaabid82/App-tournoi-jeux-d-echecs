from controller.controller_tour import ControllerTour
from models.match_model import Match
from view.match_view import CreationMatchView


class ControllerMatch:
    def __init__(self):
        self.match = Match
        self.creationMatchView = CreationMatchView()
    
    def startMatch(self):
        return self.creationMatchView.starMatchView()