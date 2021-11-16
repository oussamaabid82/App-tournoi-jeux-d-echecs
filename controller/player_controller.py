from tinydb import TinyDB
from models.player_model import PlayerModel
from view.player_view import PlayerView


class PlayerController:
    players_list_serialized = []
    def __init__(self):
        self.player_view = PlayerView()

    def createPlayers(self):
        players = []
        for i in range(self.player_view.numberOfPlayer()):
            joueur = self.player_view.playerData()
            player = PlayerModel(joueur[0], joueur[1], joueur[2], joueur[3], joueur[4])
            self.player_view.introducePlayer(player.nom_de_famille, player.prenom, player.classement)
            players.append(player)
            self.players_list_serialized.append(player.serializationPlayer())
        return players

    def updatePlayerClassement(self):
        player_list = self.tour_models.updatePlayerClassementModel()
        for player in player_list:
            nom = player.nom_de_famille
            prenom = player.prenom
            classement = player.classement
            self.tour_view.showUpdatePlayerClassement(nom, prenom, classement)

    def save(self):
        db = TinyDB("save/db.json")
        players_table  = db.table("Player")
        for player_serialized in self.players_list_serialized:
            players_table .insert(player_serialized)
        return players_table

    def chooseSortPlayers(self):
        anwer = self.player_view.playerList()
        return anwer

    def getPlayerSortedAlphabetical(self):
        name_list = []
        self.save
        db = TinyDB("save/db.json")
        players_table  = db.table("Player")
        for i in players_table:
            name_list.append(i)

        l = name_list
        list_sort = (sorted(l, key=lambda l:l["nom"]))
        for i in list_sort:
            print(i["nom"])
        
    def getPlayerSortedClassement(self):
        name_list = []
        self.save
        db = TinyDB("save/db.json")
        players_table  = db.table("Player")
        for i in players_table:
            name_list.append(i)

        l = name_list
        list_sort = (sorted(l, key=lambda l:l["classement"]))
        for i in list_sort:
            print(i["nom"])