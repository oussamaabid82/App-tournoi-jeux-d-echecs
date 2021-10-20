
joueur_creer = 0
class Joueur: 
    def __init__(self, nom_de_famille, prenom, date_de_naissance, sexe, classement=int):
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement
        
    def sePresenter(self):
        print(f"Joueur {joueur_creer}: {self.nom_de_famille} {self.prenom}, Classement: {self.classement} ")