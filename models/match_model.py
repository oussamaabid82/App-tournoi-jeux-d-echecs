

class MatchModel:

    def __init__(self, match):
        self.match = match

    def serialization_match(self):
        serialisation = {
            "match": self.match
        }
        return serialisation
