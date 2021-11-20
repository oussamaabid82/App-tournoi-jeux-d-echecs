

class TournamentView:

    def __init__(self):
        pass

    def startView(self):
        print("\n---------------* B I E N V E N U E *---------------\n")
        print("[1] - Creez un nouveau tournoi")
        print("[2] - Rapports")
        print("[3] - MAJ classement")
        print("[4] - Quitter")
        answer = int(input("\nSaisissez votre choix: "))
        return answer

    def tournamentStar(self):
        print("\nVeuillez saisir les données suivantes\n")

    def tournamentCreation(self):
        liste = ["Nom du tournoi: ", "Lieu: ", "Date de debut: ", "Date de la fin: " ]
        liste_answer = []
        for i in liste:
            liste_answer.append(input(i))
        return liste_answer

    def startMessage(self, nom):
        """Afficher à l'utilisateur le debut du tournoi"""
        print(f"\nTournoi {nom} à commencer\n")
    
    def showMatch(self, player1, player2):
        print(f"{player1}   Vs   {player2}")

    def endMessage(self):
        """Afficher à l'utilisateur la fin du tournoi"""
        print("Fin du tournoi")

    def chooseNumberInMenu(self):
        print("\n***** R A P P O R T *****\n")
        print("1- Liste de tous les acteurs")
        print("2- Liste des joueurs dans un tournoi")
        print("3- Liste de tous les tournois")
        print("4- Liste des tours dans un tournoi")
        print("5- Liste des matchs dans un tournoi")
        answer = input("\nSaisissez le numero de la liste que vous voulez afficher: ")
        return int(answer)

    def messaageTournamentRaport(self):
        print("\n***** Liste des tournois *****\n")

    def showTournamentList(self, tournament_list):
        print(f" * {tournament_list}")

    def showRoundList(self, list):
        print(list)
    
    def showMatchsList(self, match):
        print(match)
    
    def messagePlayerSortedInTournament(self):
        print("\nListe des joueurs trier par ordre alphbetique\n")
        print(" {NOM}      {PRENOM}")
        print("----------+----------")
    
    def messageRoundsRaport(self):
        print("\n***** Liste des tours *****\n")

    def messageToursInTournament(self):
        print("\nChoisissez quel tournoi vous voulez afficher ses tours\n")

    def messageMatchInTournament(self):
        print("\nChoisissez quel tournoi vous voulez afficher ses matchs")

    def chooseNumberOfTournament(self):
        number = int(input("\nChoisissez le numero du tournoi: "))
        return number
    
    def viewTours(self):
        print("")
    
    def showPlayerName(self, nom, prenom):
        print(f"{nom}           {prenom}")

    def showListTournamentWithNumber(self, numero, tournament):
        print(f"{numero}- {tournament}")
    
    def show(self, tournament):
        print(tournament)

    def messageMatchList(self):
        print("\n***** Liste des matchs *****\n")

    def endView(self):
        print("\n-----------------* A LA PROCHAINE *-----------------")
