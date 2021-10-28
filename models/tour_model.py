from datetime import datetime


class TourModel:
    """Les dates et les heures de debut et de la fin de la tour sont générés automatiquement"""
    def __init__(self, nom_de_tour, date_de_debut=datetime.now().date(), heure_de_debut=datetime.now().time(), date_fin=datetime.now().date(), 
                heure_fin=datetime.now().time()
                ):
        self.nom_de_tour = nom_de_tour
        self.date_de_debut = date_de_debut
        self.heure_de_debut = heure_de_debut
        self.date_fin = date_fin
        self.heure_fin = heure_fin
       
    def serialization_tour(self):
        serialization = {
            "nom": self.nom_de_tour,
            "date de debut": self.date_de_debut,
            "heure de debut": self.heure_de_debut,
            "date de la fin": self.date_fin,
            "heure de la fin": self.heure_fin
        }
        return serialization