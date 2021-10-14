from datetime import datetime

class Tournoi:
    def __init__(self, nom_du_tournoi, lieu, date_debut, date_fin):
        self.nom = nom_du_tournoi
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        
    def commencerLeTournoi(self):
        """Afficher à l'utilisateur le debut du tournoi"""
        print(f"Le tournoi {self.nom} à commencer le {self.date_debut}")

    def finirLeTournoi(self):
        """Afficher à l'utilisateur la fin du tournoi"""
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
    """Les dates et les heures de debut et de la fin de la tour sont générés automatiquement"""
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
        """Afficher la date et l'heure de debut de la tour"""
        print(f"Le tour a commencé le {self.date_de_debut} à {self.heure_de_debut}")

    def trierParClassement(self):
        """Trier les joueurs en fonction de leur classement"""
        l = liste_joueurs
        liste_trier = (sorted(l, key=lambda l:l[2]))
        index_joueur = [f"joueur {index}" for index in range(1, len(liste_trier)+1)]
        dictionnaire = list(zip(index_joueur, liste_trier))
        return dictionnaire

    def genererPaireDeJoueursTour(self):
        """Divisez les joueurs en deux moitiés, une supérieure et une inférieure"""
        liste_superieur = self.trierParClassement()[:int(len(self.trierParClassement())/2)]
        liste_inferieur = self.trierParClassement()[int(len(self.trierParClassement())/2):]
        """Générer les paires de joueurs qui vont s'infronter au premier tour"""
        paire_de_joueurs = list(zip(liste_superieur, liste_inferieur)) 
        return paire_de_joueurs
       
    def creerListeDesMatchs(self):
        """liste des matchs"""
        liste_paire_des_joueurs = self.genererPaireDeJoueursTour()
        return liste_paire_des_joueurs

    def finirLeTour(self):
        print(f"Le tour {self.nom_de_tour} est fini le {self.date_fin} à {self.heure_fin}")

class Match:
    def __init__(self, numero_de_match):
        self.numero_de_match = numero_de_match        

    def commencerLeMatch(self):
        print(f"Le matche a commencé")
    
    def presenterLePaireDeJoueur(self):
        pass

    def finirLeMatch(self):
        print("fin du match")

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

joueur = Joueur
joueur("AA", "WW", "10/10/1982", "Homme", 5)
joueur("BB", "XX", "10/10/1978", "Homme", 15)
joueur("CC", "VV", "10/10/1979", "Homme", 9)
joueur("DD", "ZZ", "10/10/1982", "Femme", 2)
joueur("EE", "YY", "10/10/1978", "Homme", 3)
joueur("FF", "UU", "10/10/1979", "Homme", 1)
joueur("GG", "PP", "10/10/1979", "Femme", 8)
joueur("HH", "LL", "10/10/1979", "Homme", 6)


tour = Tour("Round 1")
tour.trierParClassement()
tour.commencerLeTour()
tour.creerListeDesMatchs()


# Joueur.sePresenter(liste_joueurs)

# tour.finirLeTour()
# tournoi.finirLeTournoi()