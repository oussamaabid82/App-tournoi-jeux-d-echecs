from controller.tournament_controller import TournamentContoller
from controller.player_controller import PlayerController
from controller.tour_controller import TourController
from controller.match_controller import ControllerMatch


tournament_controller = TournamentContoller()
if tournament_controller.startTournament() == "y":
    tournament_controller.creationTournement()

    player_conroller = PlayerController()
    players = player_conroller.createPlayers()

    tour_controller = TourController(players)
    round = tour_controller.createFirstRound()
    tour_controller.createNextRound()

    tournament_controller.__init__(players, round)
    tournament_controller.createList()

    tour_controller.updatePlayerClassement()

    if tournament_controller.startReport() == "y":
        if tournament_controller.chooseRaportMenu() == 1:
            tournament_controller.reportPlayerController()
        if tournament_controller.chooseRaportMenu() == 2:
            tournament_controller.reportTournamentController()
        if tournament_controller.chooseRaportMenu() == 3:
            tournament_controller.reportRoundController()
        tournament_controller.showEndTournament()
    else:
        tournament_controller.showEndTournament()
    
else:
    tournament_controller.showEndTournament()

