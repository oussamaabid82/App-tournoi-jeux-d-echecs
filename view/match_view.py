

class MatchView:
    def __init__(self):
        pass

    def starMatchView(self):
        print("Le match va commencer\n")
    
    def playerMatch(self, match):
        print(f"{match[0]} contre {match[1]}")

    def endMatch(self):
        print("fin du match")