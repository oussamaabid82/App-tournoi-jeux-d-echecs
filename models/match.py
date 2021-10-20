
match_creer = 0
class Match:
    def __init__(self, pair_de_joueur):
        self.pair_de_joueur = pair_de_joueur      

    def commencerLeMatch(self):
        print(f"Le match {match_creer} a commencé {self.pair_de_joueur[0]} contre {self.pair_de_joueur[1]} ")

    def finirLeMatch(self):
        print("fin du match")