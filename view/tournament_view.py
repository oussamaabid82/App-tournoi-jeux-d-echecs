

class TournamentView:

    def __init__(self):
        pass

    def startView(self):
        print("\n--------------- BONJOUR ---------------\n")
        print("Voulez vous creez un nouveau tournoi? [y/n]")
            
    def endView(self):
        print("--------------- A la prochaine ---------------")
    
    def tournamentStar(self):
        print("\nVeuillez saisir les données suivantes\n")

    def tournamentCreation(self): 
       return input("Nom du tournoi: "), input("Lieu: "), input("Date de debut: "), input("Date de la fin: ")
    
    def startMessage(self):
        """Afficher à l'utilisateur le debut du tournoi"""
        print(f"\nLe tournoi à commencer")

    def endMessage(self):
            """Afficher à l'utilisateur la fin du tournoi"""
            print(f"Fin du tournoi")

