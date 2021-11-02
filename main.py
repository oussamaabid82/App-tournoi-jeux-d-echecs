from controller.tournament_controller import TournamentContoller
from controller.player_controller import PlayerController
from controller.tour_controller import TourController
from controller.match_controller import ControllerMatch



"""tournament_controller = TournamentContoller()
tournament_controller.startTournament()
tournament_controller.creationTournement()
tournament_controller.showStartTournament()"""

player_conroller = PlayerController()
players = player_conroller.createPlayers()


tour_controller = TourController(players)
tour_controller.createFirstRound()