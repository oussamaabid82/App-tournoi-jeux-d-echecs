from tinydb import TinyDB


class Match:
    def __init__(self, pair_de_joueur):
        self.pair_de_joueur = pair_de_joueur      

    def serialization_match(self):
        serialisation = {
            "match": self.pair_de_joueur
        }
        return serialisation

    def save(self):
        db = TinyDB("db.json")
        table_match = db.table("joueurs")
        table_match.truncate()
        table_match.insert_multiple(self.serialisation_match)
        return table_match

