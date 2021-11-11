

class MatchModel:
    match_list= []
    def __init__(self, match):
        self.match = match

    def creationMatchList(self):
        self.match_list.append(self)

    def serialization_match(self):
        serialisation = {
            "match": self.match
        }
        return serialisation
