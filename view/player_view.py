

class PlayerView:
    def __init__(self):
        pass

    def numberOfPlayer(self):
        nombre_of_player = int(input("\nVeuillez saisir le nombre de participant: "))
        return nombre_of_player

    def playerData(self):
        return (input("\n* Nom: "), input("* Prénom: "), input("* Date de naissance: "), input("* Sexe: "), input("* Classement:"))

    def introducePlayer(self, nom_de_famille, prenom, classement):
        print(f"___ le Joueur: {nom_de_famille} {prenom}, Classement: {classement} ___")
