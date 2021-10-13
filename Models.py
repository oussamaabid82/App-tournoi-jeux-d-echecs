from random import sample
from datetime import datetime

class Tournoi:
    def __init__(self, nom_du_tournoi, lieu, date_debut, date_fin):
        self.nom = nom_du_tournoi
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        
    def commencerLeTournoi(self):
        print(f"Le tournoi {self.nom} à commencer le {self.date_debut}")

    def finirLeTournoi(self):
        print(f"Fin du tournoi {self.nom} à la date {self.date_fin}")

class Joueur:
     
    def __init__(self, nom_de_famille, prenom, date_de_naissance, sexe, classement=int):
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement
        self.liste_joueurs = liste_joueurs.append([self.nom_de_famille, self.prenom, classement])
        
    def sePresenter(self):
        """for i in liste_joueurs:
            print(f"Nom:{i[0]}\nPrénom:{i[1]}\nDate de naissance:{i[2]}\nSexe:{i[3]}\n")"""
        print(liste_joueurs)
        
class Tour:
    liste_des_rounds = []
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
        print(f"Le tour a commencé le {self.date_de_debut} à {self.heure_de_debut}")

    def trierParClassement(self):
        l = liste_joueurs
        liste_trier = (sorted(l, key=lambda l:l[2]))
        index_joueur = [f"joueur {index}" for index in range(1, len(liste_trier)+1)]
        dictionnaire = dict(zip(index_joueur, liste_trier))
        print(dictionnaire)
        
    def creerListeDesMatchs(self):
        pass

    def finirLeTour(self):
        print(f"Le tour {self.nom_de_tour} est fini le {self.date_fin} à {self.heure_fin}")

class Match:
    def __init__(self):
        pass        

    def commencerLeMatch(self):
        print(f"Le matche a commencé")
    
    def generationPaireDeJoueures(self):
        liste_choisi = sample(Joueur.creerLesIndexes(self), 2)
        for index in liste_choisi:
            print (index, Joueur.creerListeDesJoueursIndexer(self).get(index))
    
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
    

liste_joueurs = []

tournoi = Tournoi("Les champions", "Paris", "05/10/2021", "10/10/2021")
tournoi.commencerLeTournoi()

joueur1 = Joueur("AA", "WW", "10/10/1982", "Homme", 5)
joueur2 = Joueur("BB", "XX", "10/10/1978", "Homme", 15)
joueur3 = Joueur("CC", "VV", "10/10/1979", "Homme", 9)
joueur4 = Joueur("DD", "ZZ", "10/10/1982", "Femme", 2)
joueur5 = Joueur("EE", "YY", "10/10/1978", "Homme", 12)
joueur6 = Joueur("FF", "UU", "10/10/1979", "Homme", 1)
joueur7 = Joueur("GG", "PP", "10/10/1979", "Femme", 8)
joueur8 = Joueur("HH", "LL", "10/10/1979", "Homme", 6)


tour = Tour("Round")
tour.trierParClassement()

tour.commencerLeTour()

generation_joueur = Match()
# generation_joueur.generationPaireDeJoueures()

# Joueur.sePresenter(liste_joueurs)

# tour.finirLeTour()
# tournoi.finirLeTournoi()