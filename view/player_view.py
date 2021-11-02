

class PlayerView:
    def __init__(self):
        pass

    def numberOfPlayer(self):
        nombre_of_player = int(input("Veuillez saisir le nombre de participant: "))
        return nombre_of_player

    def playerData(self):
       creation_player = (input("\n* Nom: "), input("* Prénom: "), input("* Date de naissance: "), input("* Sexe: "), input("* Classement:"))
       return creation_player

    def introducePlayer(self, nom_de_famille, prenom, classement):
        print(f"___ le Joueur: {nom_de_famille} {prenom}, Classement: {classement} ___")

