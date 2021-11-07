from tinydb import TinyDB


class ControllerMatch:
    def __init__(self):
        pass
    
    

    def save(self):
        db = TinyDB("db.json")
        table_match = db.table("joueurs")
        table_match.truncate()
        table_match.insert_multiple(self.serialisation_match)
        return table_match