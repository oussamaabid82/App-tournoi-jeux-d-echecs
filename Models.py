from random import random, sample

class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        
    def CommencerLeTournoi(self):
        print(f"Le tournoi {self.nom} à commencer le {self.date_debut}")

    def FinirLeTournoi(self):
        print(f"Fin  du tournoi {self.nom} à date la date {self.date_fin} ")

class Tours:
    def __init__(self, numero_de_tours:int):
        self.numero_de_tours = numero_de_tours
        if int(self.numero_de_tours) < 5:
            pass   
        else: 
            return Tours(input("Ce tournoi à seulement 4 entrer le numero correct: "))
    
    def CommencerLeTour(self):
        print(f"Le tour N°{self.numero_de_tours} a commencé")

    def FinirLeTour(self):
        print(f"Le tour N°{self.numero_de_tours} est fini")

class Matchs:
    def __init__(self):
        pass

    def CommencerLeMatch(self):
        print("Le matcha commencé")

    def FinirLeMatch(self):
        print("fin du match")

    def ResultatMatch(self):
        pass
        
class Joueurs:
    def __init__(self, nom_de_famille, prenom, date_de_naissance, sexe, classement):
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement  

    """def SePresenter(self):
        print(f"Nom:{self.nom_de_famille}\nPrénom:{self.prenom}\nDate de naissance:{self.date_de_naissance}\nSexe:{self.sexe}\nClassement:{self.classement}\n")"""
             
    def GenerationPaireJoueur(self):
        print (random(liste_des_joueur))

liste_des_joueur = []



