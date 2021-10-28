

class MatchModel:
    def __init__(self, pair_de_joueur):
        self.pair_de_joueur = pair_de_joueur      

    def serialization_match(self):
        serialisation = {
            "match": self.pair_de_joueur
        }
        return serialisation
    
    def enterMatchResults(self):
        """Saisir les resultat de chaque match  """
        list_of_pairs_more_result = []
        list_of_pairs = self.genererPairOfPlayers()
        for i in (range(len(list_of_pairs))):
            player_score1 = list(input(f"Veuillez saisir le score du joueur {list_of_pairs[i][0][0]}: "))
            player_score2 = list(input(f"Veuillez saisir le score du joueur {list_of_pairs[i][1][0]}: "))
            list = (list_of_pairs[i][0] + (player_score1)), (list_of_pairs[i][1] + (player_score2))
            print(list)
            list_of_pairs_more_result.append([list])
        return list_of_pairs_more_result



