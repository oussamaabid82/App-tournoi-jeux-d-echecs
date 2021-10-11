from random import choice, sample, shuffle
from datetime import datetime, date, time

class Tournoi:
    def __init__(self, nom_du_tournoi, lieu, date_debut, date_fin):
        self.nom = nom_du_tournoi
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        
    def commencerLeTournoi(self):
        print(f"Le tournoi {self.nom} à commencer le {self.date_debut}")

    def finirLeTournoi(self):
        print(f"Fin  du tournoi {self.nom} à date la date {self.date_fin} ")

class Joueurs: 
    liste_des_joueurs = []
    def __init__(self, nom_de_famille, prenom, date_de_naissance, sexe, classement):
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement

    # dictionnaire contien la liste des joueures créer avec un index
    def listeDesJoueursIndexer(self):
        index_joueur = [i for i in range(1, len(Joueurs.liste_des_joueurs)+1)]
        dictionnaire = dict(zip(index_joueur, Joueurs.liste_des_joueurs))
        return dictionnaire    

    def sePresenter(self):
        print(f"Nom:{self.nom_de_famille}\nPrénom:{self.prenom}\nDate de naissance:{self.date_de_naissance}\nSexe:{self.sexe}\nClassement:{self.classement}\n")
    
class Tour:
    def __init__(self, nom_de_tour, date_de_debut=datetime.now().date(), 
                heure_de_debut=datetime.now().time(), date_fin=datetime.now().date(), 
                heure_fin=datetime.now().time()
                ):
        self.nom_de_tour = nom_de_tour
        self.date_de_debut = date_de_debut
        self.heure_de_debut = heure_de_debut
        self.date_fin = date_fin
        self.heure_fin = heure_fin
        
        
    def commencerLeTour(self):
        print(f"Le tour {self.nom_de_tour} a commencé le {self.date_de_debut} à {self.heure_de_debut}")

    def creerListeDesMatchs(self):
        pass

    def finirLeTour(self):
        print(f"Le tour N°{self.numero_de_tours} est fini le {self.date_fin} à {self.heure_fin}")

class Matchs:
    def __init__(self):
        pass        

    def commencerLeMatch(self):
        print(f"Le matche a commencé")
    
    def generationPaireDeJoueures(self):
        liste_choisi = (sample(range(1, len(Joueurs.liste_des_joueurs)+1), 2))
        for index in liste_choisi:
        #liste_indexer = Joueurs.liste_des_joueurs_indexer
            return index
    
    def presenterLePaireDeJoueur(self):
        pass

    def finirLeMatch(self):
        print("fin du match")

    def saisirResultatMatch(self):
        pass

class Classement:
    def __init__(self):
        pass

class ControleDuTemps:
    # bullet, un blitz ou un coup rapide
    def __init__(self):
        pass

class Description:
    # Remarque générales du directeur du tournoi
    def __init__(self):
        pass
    
liste_des_joueurs = Joueurs.liste_des_joueurs

tournoi = Tournoi("Les champions", "Paris", "05/10/2021", "10/10/2021")
tournoi.commencerLeTournoi()


tour = Tour("Round1")
tour.commencerLeTour()
tour.finirLeTour()

joueur1 = Joueurs("abid", "oussama", "10/10/82", "Homme", 2)
joueur2 = Joueurs("BenM", "chadli", "10/10/1978", "Homme", 4)
joueur3 = Joueurs("Esseghir", "moez", "10/10/1979", "Homme", 3)
liste_des_joueurs.extend([joueur1, joueur2, joueur3])

#for joueur in liste_des_joueurs:
    #joueur.sePresenter()

generation_joueur = Matchs.generationPaireDeJoueures
generation_joueur(liste_des_joueurs)
