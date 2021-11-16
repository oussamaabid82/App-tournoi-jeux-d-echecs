# coding:utf-8


from controller.tournament_controller import TournamentContoller
from controller.player_controller import PlayerController
from controller.tour_controller import TourController


def play():
    tournament_controller = TournamentContoller()
    choice = tournament_controller.startTournament()
    
    if choice == 1:
        tournament_controller.showStartTournament()
        tournament_controller.creationTournement()
        
        player_conroller = PlayerController()
        players = player_conroller.createPlayers()

        tour_controller = TourController(players)
        round = tour_controller.createFirstRound()
        tour_controller.createNextRound()

        match_list = tour_controller.match_list

        tour_controller.updatePlayerClassement()

        tournament_controller.round = round
        tournament_controller.matchs = match_list
        tournament_controller.createList()
        tournament_controller.save()

        player_conroller.save()

    elif choice == 2:
        choice_menu = tournament_controller.chooseRaportMenu()
        players_conroller = PlayerController()

        if choice_menu == 1:
            choose = players_conroller.chooseSortPlayers()
            if choose == 1:
                players_conroller.getPlayerSortedAlphabetical()
            elif choose == 2:
                players_conroller.getPlayerSortedClassement()
        
        if choice_menu == 2:
            tournament_controller.getTournament()

        if choice_menu == 3:
            tournament_controller.getRound()

        if choice_menu == 4:
            tournament_controller.getMatchs()
            tournament_controller.showEndTournament()

    elif choice == 3:
        tournament_controller.showEndTournament()

    else:
        tournament_controller.showEndTournament()