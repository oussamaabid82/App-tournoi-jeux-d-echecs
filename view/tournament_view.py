

class TournamentView:

    def __init__(self):
        pass

    def showstartMenu(self):
        print("\n---------------* B I E N V E N U E *---------------\n")
        print("[1] - Creez un nouveau tournoi")
        print("[2] - Rapports")
        print("[3] - MAJ classement")
        print("[4] - Quitter")
        answer = int(input("\nSaisissez votre choix: "))
        return answer

    def initializationOfATournament(self):
        """Initialisation d'un tournoi"""
        liste = ["Nom du tournoi: ", "Lieu: ", "Date de debut: ", "Date de la fin: "]
        liste_answer = []
        for i in liste:
            liste_answer.append(input(i))
        return liste_answer

    def tournamenMessage(self):
        print("\nVeuillez saisir les données suivantes\n")

    def startMessage(self, nom):
        """Afficher à l'utilisateur le debut du tournoi"""
        print(f"\nTournoi {nom} à commencer\n")

    def messageMatchList(self):
        print("\n***** Liste des matchs *****\n")

    def showMatch(self, player1, player2):
        print(f"    {player1}   Vs   {player2}")

    def endMessage(self):
        """Afficher à l'utilisateur la fin du tournoi"""
        print("Fin du tournoi")

    def showRaportMenu(self):
        print("\n***** R A P P O R T *****\n")
        print("1- Liste de tous les acteurs")
        print("2- Liste des joueurs dans un tournoi")
        print("3- Liste de tous les tournois")
        print("4- Liste des tours dans un tournoi")
        print("5- Liste des matchs dans un tournoi")
        answer = input("\nSaisissez le numero de la liste que vous voulez afficher: ")
        return int(answer)

    def titelTournamentRaport(self):
        print("\n***** Liste des tournois *****\n")

    def showTournamentList(self, number, tournament_list):
        """Mise en page de l'affichage de la liste des tournois"""
        print(f" {number}- {tournament_list}")

    def titelPlayerSortedInTournament(self):
        """En-tête le la liste des joueurs dans un tournoi"""
        print("\nListe des joueurs trier par ordre alphbetique\n")
        print("{N}|   {NOM}   |  {PRENOM}  |")
        print("---+-----------+------------+")

    def showPlayerName(self, rang, nom, prenom):
        print(f" {rang} |    {nom}    |     {prenom}    |")

    def showListTournamentWithNumber(self, numero, tournament):
        print(f"{numero}- {tournament}")

    def messageRoundsInTournament(self):
        print("\nChoisissez quel tournoi vous voulez afficher ses tours\n")

    def showRoundList(self, list):
        print(list)

    def titelRoundsRaport(self):
        print("\n***** Liste des tours *****\n")

    def showMatchsList(self, match):
        print(match)

    def messageMatchInTournament(self):
        print("\nChoisissez quel tournoi vous voulez afficher ses matchs\n")

    def chooseNumberOfTournament(self):
        number = int(input("\nChoisissez le numero du tournoi: "))
        return number

    def show(self, tournament):
        print(tournament)

    def endView(self):
        print("\n-----------------* A LA PROCHAINE *-----------------")
