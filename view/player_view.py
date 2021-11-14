

class PlayerView:
    def __init__(self):
        pass

    def numberOfPlayer(self):
        number_of_player = int(input("\nVeuillez saisir le nombre de participant (un nombre pair): "))
        while number_of_player %2 != 0:
           number_of_player = int(input("\nVeuillez saisir le nombre de participant (un nombre pair): "))
        return number_of_player

    def playerData(self):
        return (input("\n* Nom: "), input("* Prenom: "), input("* Date de naissance: "), input("* Sexe: "), input("* Classement:"))

    def introducePlayer(self, nom_de_famille, prenom, classement):
        print(f"___ le Joueur: {nom_de_famille} {prenom}, Classement: {classement} ___")
