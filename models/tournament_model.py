from tinydb import TinyDB


class TournamentModels:
    def __init__(self, nom_du_tournoi, lieu, date_debut, date_fin, nombre_de_tours=4):
        self.nom = nom_du_tournoi
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_de_tours = nombre_de_tours

    def serialization_tournoi(self):
        serialisation = {
            "nom": self.nom,
            "lieu": self.lieu,
            "date de debut": self.date_debut,
            "date de la fin": self.date_fin,
            "nombre de tour": self.nombre_de_tours
        }
        return serialisation

    def save(self):
        db = TinyDB("db.json")
        table_tournoi = db.table("joueurs")
        table_tournoi.truncate()	# clear the table first
        table_tournoi.insert_multiple(self.serialisation_tournoi)
        return table_tournoi

    