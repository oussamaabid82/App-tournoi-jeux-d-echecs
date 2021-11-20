

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

    def playerList(self):
        print("\nAfficher la liste des joueurs:\n")
        print(" 1: Par ordre Alphabetique")
        print(" 2: Par classement\n")
        answer = input("Saisissez 1 ou 2: \n")
        return int(answer)
    
    def showUpdatePlayerClassement(self, nom, prenom, classement):
        print(f"Veuillez mettre à jour le classement du joueur {nom} {prenom}:")
        print(f"Son ancien classement est {classement}")
        classement = int(input("Saisissez le nouveau classement : "))
        print("")
        return classement
    
    def showMAJ(self):
        print("\n***** Mise a jour du classement d'un joueur *****\n")
    
    def showUdateClassementnsertName(self):
        return input("Saisissez le nom du joueur: ")
    
    def showError(self):
        print("\n** Ce prenom n'existe pas dans la liste des joueurs **")
    
    def showNewClassement(self):
        return int(input("Saisissez le nouveau classement: "))
    
    def chooseNumnerFromPlayer(self):
        return int(input("Saisissez le numéro du joueur que vous voulez mettre son classement à jour: "))
