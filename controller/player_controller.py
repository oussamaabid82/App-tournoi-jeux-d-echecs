from tinydb import TinyDB, Query
from models.player_model import PlayerModel
from view.player_view import PlayerView


class PlayerController:
    players_list_serialized = []
    players = []
    def __init__(self):
        self.player_view = PlayerView()

    def createPlayers(self):
        for i in range(self.player_view.numberOfPlayer()):
            joueur = self.player_view.playerData()
            player = PlayerModel(joueur[0], joueur[1], joueur[2], joueur[3], joueur[4])
            self.player_view.introducePlayer(player.nom_de_famille, player.prenom, player.classement)
            self.players.append(player)
            self.players_list_serialized.append(player.serializationPlayer())
        
    def updateClassementAfterMatch(self):
        for i in self.players_list_serialized:
            i["classement"] = self.player_view.showUpdatePlayerClassement(i["nom"], i["prenom"], i["classement"])
       
    def save(self):
        db = TinyDB("save/db.json")
        players_table  = db.table("Player")
        for player_serialized in self.players_list_serialized:
            players_table .insert(player_serialized)
        return players_table

    def updateClassement(self):
        self.player_view.showMAJ()
        user = Query()
        db = TinyDB("save/db.json")
        players_table  = db.table("Player")
        prenom = self.player_view.showUdateClassementnsertName()
        classement = self.player_view.showNewClassement()
        players_table.update({"classement":classement}, user.prenom == prenom)        
        
    def chooseSortPlayers(self):
        anwer = self.player_view.playerList()
        return anwer

    def getPlayerSortedAlphabetical(self):
        name_list = []
        db = TinyDB("save/db.json")
        players_table  = db.table("Player")
        for i in players_table:
            name_list.append(i)
        l = name_list
        list_sort = (sorted(l, key=lambda l:l["nom"]))
        self.player_view.messagePlayerSortedAlphabetical()
        for i in list_sort:
            self.player_view.showPlayerName(i["nom"], i["prenom"])
        
    def getPlayerSortedClassement(self):
        name_list = []
        db = TinyDB("save/db.json")
        players_table  = db.table("Player")
        for i in players_table:
            name_list.append(i)
        l = name_list
        self.player_view.messagePlayerSortedClassement()
        list_sort = (sorted(l, key=lambda l:l["classement"]))
        for i in list_sort:
            self.player_view.showPlayerName(i["nom"], i["prenom"])
    
    

       
    