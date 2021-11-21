

class TourView:
    def __init__(self):
        pass

    def startTourView(self, round_name):
        print(f"\n***** {round_name} va commencer *****\n")

    def finishTour(self, round_name):
        print(f"\n***** {round_name} est fini *****")

    def showMatchList(self, player_name1, player_name2):
        print(f" \n* {player_name1} Vs {player_name2}")
