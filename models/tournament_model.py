

class TournamentModels:

    def __init__(self, 
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
        self.players_list = []
        self.tours_list = []
        self.match_list = []

    def reportPlayerModel(self, view):
        answer = view 
        l = self.players_list       
        if answer == 1:
            list_sorted_by_name = (sorted(l, key=lambda l:l.nom_de_famille))
            return list_sorted_by_name
        elif answer == 2:
            list_sorted_by_classement = (sorted(l, key=lambda l:l.classement))
            return list_sorted_by_classement
        
    def tour_list(self):
        return self.tours_list
    
    def matchs_list(self):
        return self.match_list
    
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
            "liste des matchs": matchs
        }
        return serialisation
