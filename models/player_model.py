from tinydb import TinyDB


class Player: 
    def __init__(self, nom_de_famille, prenom, date_de_naissance, sexe, classement=int):
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

    def save(self):
        db = TinyDB("db.json")
        table_joueur = db.table("joueurs")
        table_joueur.truncate()	# clear the table first
        table_joueur.insert_multiple(self.serialisation_joueur)
        return table_joueur