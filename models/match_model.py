

class MatchModel:
    def __init__(self, match):
        self.match = match

    def creationMatch(self):
        match = self.match
        return match

    def serialization_match(self):
        serialisation = {
            "match": self.match
        }
        return serialisation
    




