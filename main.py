from controller.tournament_controller import TournamentContoller
from controller.player_controller import PlayerController
from controller.tour_controller import TourController
#from controller.match_controller import ControllerMatch


tournament_controller = TournamentContoller()
tournament_controller.startTournament()
tournament_controller.creationTournement()
tournament_controller.showStartTournament()

player_conroller = PlayerController()
player_conroller.playerCreation()

tour_controller = TourController()
tour_controller.createRound()