

class TourView:
    def __init__(self):
        pass

    def startTourView(self, round_name):
        print(f"\n***** {round_name} va commencer *****\n")

    def finishTour(self, round_name):
        print(f"\n***** {round_name} est fini *****")

    def showUpdatePlayerClassement(self, nom, prenom, classement):
        print(f"Veuillez mettre à jour le classement du joueur {nom} {prenom}:")
        print(f"Son ancien classement est {classement}")
        classement = int(input("Saisissez le nouveau classement :\n"))
        return classement

    def showMatchList(self, player_name1, player_name2):
        print(f" \n* {player_name1} Vs {player_name2}")
