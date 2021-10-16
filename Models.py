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
    joueur_creer = 0 
    def __init__(self, nom_de_famille, prenom, date_de_naissance, sexe, classement=int):
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement
        Joueur.joueur_creer += 1
        self.liste_joueurs = liste_joueurs.append([Joueur.joueur_creer, self.nom_de_famille, self.prenom, classement])
        
    def sePresenter(self):
        """for i in liste_joueurs:
            print(f"Nom:{i[0]}\nPrénom:{i[1]}\nDate de naissance:{i[2]}\nSexe:{i[3]}\n")"""
        print(liste_joueurs)
        
class Tour:
    """Les dates et les heures de debut et de la fin de la tour sont générés automatiquement"""
    round_creer = 0
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
        Tour.round_creer += 1 
         
    def commencerLeTour(self):
        """Afficher la date et l'heure de debut de la tour"""
        print(f"Le {self.nom_de_tour} {Tour.round_creer} a commencé le {self.date_de_debut} à {self.heure_de_debut}")

    def trierParClassement(self):
        """Trier les joueurs en fonction de leur classement"""
        l = liste_joueurs
        liste_trier = (sorted(l, key=lambda l:l[3]))
        return liste_trier

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
    
    def saisirLesResultatDesMatch(self):
        """Saisir les resultat de chaque match  """
        liste_des_paires_plus_resultat = []
        liste_des_paires = self.genererPaireDeJoueursTour()
        for i in (range(len(liste_des_paires))):
            score_joueur1 = list(input(f"Veuillez saisir le score du joueur {liste_des_paires[i][0][0]}: "))
            score_joueur2 = list(input(f"Veuillez saisir le score du joueur {liste_des_paires[i][1][0]}: "))
            liste = (liste_des_paires[i][0] + (score_joueur1)), (liste_des_paires[i][1] + (score_joueur2))
            print(liste)
            liste_des_paires_plus_resultat.append([liste])
        return liste_des_paires_plus_resultat

    def finirLeTour(self):
        print(f"Le tour {self.nom_de_tour} est fini le {self.date_fin} à {self.heure_fin}")

class Match:
    match_creer = 0
    def __init__(self, pair_de_joueur):
        self.pair_de_joueur = pair_de_joueur
        Match.match_creer += 1        

    def commencerLeMatch(self):
        print(f"Le match: {Match.match_creer} a commencé")

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

joueur1 = Joueur("AA", "WW", "10/10/1982", "Homme", 5)
joueur2 = Joueur("BB", "XX", "10/10/1978", "Homme", 15)
joueur3 = Joueur("CC", "VV", "10/10/1979", "Homme", 9)
joueur4 = Joueur("DD", "ZZ", "10/10/1982", "Femme", 2)
joueur5 = Joueur("EE", "YY", "10/10/1978", "Homme", 3)
joueur6 = Joueur("FF", "UU", "10/10/1979", "Homme", 1)
joueur7 = Joueur("GG", "PP", "10/10/1979", "Femme", 8)
joueur8 = Joueur("HH", "LL", "10/10/1979", "Homme", 6)


tour = Tour("Round")
# tour.trierParClassement()
tour.commencerLeTour()
# tour.creerListeDesMatchs()
# tour.saisirLesResultatDesMatch()

for i in tour.creerListeDesMatchs():
    match = Match(i)
    match.commencerLeMatch()

# Joueur.sePresenter(liste_joueurs)

# tour.finirLeTour()
# tournoi.finirLeTournoi()