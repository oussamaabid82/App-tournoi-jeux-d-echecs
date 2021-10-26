from models.tour_model import Tour
from models.match_model import Match
from view.tour_view import CreationTourdisplay
from view.match_view import CreationMatchView


list_tours = []
players_list = []
tour_creer = 0

class ControllerTour:
    def __init__(self):
        self.creationTourdisplay = CreationTourdisplay()
        self.creationMatchView = CreationMatchView()
        
    def commencerTour(self):
        return self.creationTourdisplay.starTour(tour_creer+1)

    def creerTour(self):
        for i in range(len(players_list)-1):
            tour = Tour("Round")
            list_tours.append(tour)
            tour.sortPlayersByRanking()
            self.creationTourdisplay.starTour()
            for i in tour.createMatchesList():
                Match(i)
                self.creationMatchView.starMatchView()
                return tour