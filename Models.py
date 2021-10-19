from datetime import datetime
from operator import itemgetter, attrgetter

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

class Joueur: 
    def __init__(self, nom_de_famille, prenom, date_de_naissance, sexe, classement=int):
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement
        
    def sePresenter(self):
        print(f"Joueur {joueur_creer}: {self.nom_de_famille} {self.prenom}, Classement: {self.classement} ")
             
class Tour:
    """Les dates et les heures de debut et de la fin de la tour sont générés automatiquement"""
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
        print(f"Le {self.nom_de_tour} a commencé le {self.date_de_debut} à {self.heure_de_debut}")

    def trierLesJoueursParClassement(self):
        """Trier les joueurs en fonction de leur classement"""
        l = liste_joueurs
        liste_trier = (sorted(l, key=lambda l:l[4]))
        return liste_trier

    def genererPaireDeJoueurs(self):
        """Divisez les joueurs en deux moitiés, une supérieure et une inférieure"""
        liste_superieur = self.trierLesJoueursParClassement()[:int(len(self.trierLesJoueursParClassement())/2)]
        liste_inferieur = self.trierLesJoueursParClassement()[int(len(self.trierLesJoueursParClassement())/2):]
        """Générer les paires de joueurs qui vont s'infronter au premier tour"""
        paire_de_joueurs = list(zip(liste_superieur, liste_inferieur)) 
        return paire_de_joueurs
       
    def creerListeDesMatchs(self):
        """liste des matchs"""
        liste_paire_des_joueurs = self.genererPaireDeJoueurs()
        return liste_paire_des_joueurs
    
    def saisirLesResultatDesMatch(self):
        """Saisir les resultat de chaque match  """
        liste_des_paires_plus_resultat = []
        liste_des_paires = self.genererPaireDeJoueurs()
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
    def __init__(self, pair_de_joueur):
        self.pair_de_joueur = pair_de_joueur      

    def commencerLeMatch(self):
        print(f"Le match a commencé {self.pair_de_joueur} ")

    def finirLeMatch(self):
        print("fin du match")

class Classement:
    def __init__(self):
        pass

class Description:
    # Remarque générales du directeur du tournoi
    def __init__(self):
        pass
    
donner_tournoi = []
liste_joueurs = []

# tournoi = Tournoi(input("Nom du tournoi: "), input("Lieu: "), input("Date de debut: "), input("Date de la fin: "))
# donner_tournoi.append(tournoi)
# tournoi.commencerLeTournoi()
joueur_creer = 0
for i in range(int(input("Nombre de participants: "))):
    joueur = Joueur(input("Nom: "), input("Prénom: "), input("Date de naissance: "), input("Sexe: "), input("Classement:"))
    joueur_creer += 1
    liste_joueurs.append([joueur.nom_de_famille, joueur.prenom, joueur.date_de_naissance, joueur.sexe, joueur.classement])
    joueur.sePresenter()

tour1 = Tour("Round")
tour1.trierLesJoueursParClassement()
tour1.creerListeDesMatchs()
tour1.commencerLeTour()
for i in tour1.creerListeDesMatchs():
    match = Match(i)
    match.commencerLeMatch()
tour1.finirLeTour()
tour1.saisirLesResultatDesMatch()

# tournoi.finirLeTournoi()