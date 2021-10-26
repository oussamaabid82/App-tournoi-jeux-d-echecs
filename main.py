from models.tournament_model import TournamentModels
from models.player_model import Player
from models.tour_model import Tour
from models.match_model import Match
from controller.tournament_controller import TournametContoller
from controller.player_controller import ControllerPlayer
from controller.tour_controller import ControllerTour
from controller.match_controller import ControllerMatch
from view.tournament_view import TournamentView
from view.player_view import PlayerView
from view.tour_view import TourView
from view.match_view import MatchView

tournament_view = TournamentView()
tournament_view.startView()