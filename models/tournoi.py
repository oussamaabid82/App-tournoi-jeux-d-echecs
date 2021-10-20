

class Tournoi:
    def __init__(self, nom_du_tournoi, lieu, date_debut, date_fin, nombre_de_tours=4):
        self.nom = nom_du_tournoi
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_de_tours = nombre_de_tours
        
    def commencerLeTournoi(self):
        """Afficher à l'utilisateur le debut du tournoi"""
        print(f"Le tournoi {self.nom} à commencer le {self.date_debut}")

    def finirLeTournoi(self):
        """Afficher à l'utilisateur la fin du tournoi"""
        print(f"Fin du tournoi {self.nom} à la date {self.date_fin}")