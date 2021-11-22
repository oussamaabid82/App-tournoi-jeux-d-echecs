

class TournamentModels:
    def __init__(
                self,
                nom_du_tournoi="",
                lieu="",
                date_debut="",
                date_fin="",
                nombre_de_tours=4
                ):
        self.nom = nom_du_tournoi
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_de_tours = nombre_de_tours
        self.descriptions = str
        self.players_list = []
        self.tours_list = []
        self.match_list = []

    def tour_list(self):
        """Importer la liste des tours"""
        return self.tours_list

    def matchs_list(self):
        """Importer la liste des matchs"""
        return self.match_list

    def tournamentDescriptionsModel(self, descriptions):
        self.descriptions = descriptions

    def serialization_tournoi(self):
        players = []
        tour = []
        matchs = []

        for i in self.players_list:
            players.append((i.prenom, i.nom_de_famille))

        for i in self.match_list:
            p0 = i[0].serializationPlayer()["prenom"]
            p1 = i[1].serializationPlayer()["prenom"]
            matchs.append((p0, p1))

        for i in self.tours_list:
            tour.append(i.nom_de_tour)

        serialisation = {
            "nom": self.nom,
            "lieu": self.lieu,
            "date de debut": self.date_debut,
            "date de la fin": self.date_fin,
            "nombre de tour": self.nombre_de_tours,
            "list des joueurs": players,
            "liste des tours": tour,
            "liste des matchs": matchs,
            "Descriptions": self.descriptions
        }
        return serialisation
