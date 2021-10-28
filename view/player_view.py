

class PlayerView:
    def __init__(self):
        pass

    def numberOfPlayer(self):
        nombre = int(input("Veuillez saisir le nombre de participant: "))
        return nombre

    def playerData(self):
       creation = (input("Nom: "), input("Prénom: "), input("Date de naissance: "), input("Sexe: "), input("Classement:"))
       return creation

    def introducePlayer(self, nom_de_famille, prenom, classement):
        print(f"le Joueur: {nom_de_famille} {prenom}, Classement: {classement}\n")

