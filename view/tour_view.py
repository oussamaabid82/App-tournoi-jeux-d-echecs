

class TourView:
    def __init__(self):
        pass

    def startTourView(self,round_name, number_of_round):
        print(f"\n***** {round_name} {number_of_round} va commencer *****\n")

    def finishTour(self, round_name, number_of_round):
        print(f"\n***** {round_name} {number_of_round} est fini *****")
    
    def showUpdatePlayerClassement(self,nom, prenom, classement):
        print(f"Veuillez mettre à jour le classement du joueur {nom} {prenom}:")
        print(f"Son ancien classement est {classement}")
        classement = input("Saisissez le nouveau classement :\n")