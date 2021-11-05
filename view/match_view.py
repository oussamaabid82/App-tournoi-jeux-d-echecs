

class MatchView:
    def __init__(self):
        pass

    def starMatchView(self):
        print("____ Le match va commencer ____\n")
    
    def playerMatch(self, match):
        print(f"{match[0].prenom} contre {match[1].prenom}\n")

    def endMatch(self):
        print("____ fin du match ____\n")
    
    def enterMatchResults(self, listPairs):
        player_score1 = int(input(f"* Veuillez saisir le score du joueur {listPairs[0].prenom}: "))
        player_score2 = int(input(f"* Veuillez saisir le score du joueur {listPairs[1].prenom}: "))
        listPairs[0].score.append(player_score1)
        listPairs[1].score.append(player_score2)
        liste = (listPairs[0].prenom , (player_score1)), (listPairs[1].prenom , (player_score2))
        print (liste)
        return (listPairs[0]), (listPairs[1])