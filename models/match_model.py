

from models.tour_model import TourModel


class MatchModel:
    def __init__(self, match):
        self.match = match

    def creationMatch(self):
        match_list = self.match
        return match_list

    def serialization_match(self):
        serialisation = {
            "match": self.match
        }
        return serialisation
    




