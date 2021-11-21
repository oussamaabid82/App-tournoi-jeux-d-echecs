

class PlayerView:
    def __init__(self):
        pass

    def numberOfPlayer(self):
        """Nombre des joueurs qui vont jouer un tournoi"""
        number_of_player = int(input("\nVeuillez saisir le nombre de participant (un nombre pair): "))
        while number_of_player %2 != 0:
           number_of_player = int(input("\nVeuillez saisir le nombre de participant (un nombre pair): "))
        return number_of_player

    def playerData(self):
        data = ["* Nom: ", "* Prenom: ", "* Date de naissance: ", "* Sexe: ", "* Classement: "]
        list_data = []
        for i in data:
            list_data.append(input(i))
        #(input("\n* Nom: "), input("* Prenom: "), input("* Date de naissance: "), input("* Sexe: "), input("* Classement:"))
        return list_data

    def introducePlayer(self, nom_de_famille, prenom, classement):
        """S'affiche après chaque joueur créer"""
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
        classement = int(input("Saisissez son nouveau classement : "))
        print("")
        return classement

    def messagePlayerSortedAlphabetical(self):
        """En-tête de la liste des joueurs"""
        print("\nListe des joueurs trier par ordre alphbetique\n")
        print(" {NOM}      {PRENOM}")
        print("----------+----------")
        
    def messagePlayerSortedClassement(self):
        """En-tête de la liste des joueurs"""
        print("\nListe des joueurs trier par classement\n")
        print(" {NOM}      {PRENOM}")
        print("----------+----------")

    def showPlayerName(self, nom, prenom):
        """Corps de la liste des joueurs"""
        print(f"{nom}           {prenom}")

    def showMAJ(self):
        print("\n***** Mise a jour du classement d'un joueur *****\n")
    
    def showUdateClassementnsertName(self):
        return input("Saisissez le nom du joueur: ")
    
    def showNewClassement(self):
        return int(input("Saisissez le nouveau classement: "))
