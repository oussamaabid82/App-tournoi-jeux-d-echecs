

class PlayerModel: 
    def __init__(self, nom_de_famille, 
                prenom, 
                date_de_naissance, 
                sexe, 
                classement=int
                ):
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement

          
    def serializationPlayer(self):
        serialization = {
            "nom": self.nom_de_famille,
            "prénom": self.prenom,
            "date de naissance": self.date_de_naissance,
            "sexe": self.sexe,
            "classement": self.classement
        }
        return serialization
