from datetime import datetime

liste_joueurs = []

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