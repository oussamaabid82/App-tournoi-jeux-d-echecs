

class MatchView:
    def __init__(self):
        pass

    def starMatchView(self):
        print("Le match va commencer\n")
    
    def playerMatch(self, match):
        print(f"{match[0]} contre {match[1]}")

    def endMatch(self):
        print("fin du match")
    
    def enterMatchResults(self):
        player_score1 = list(input(f"Veuillez saisir le score du joueur {list_of_pairs[i][0][0]}: "))
        player_score2 = list(input(f"Veuillez saisir le score du joueur {list_of_pairs[i][1][0]}: "))