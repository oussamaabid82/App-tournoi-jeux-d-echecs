from tinydb import TinyDB
from models.player_model import PlayerModel
from view.player_view import PlayerView


class PlayerController:
    def __init__(self):
        self.player_view = PlayerView()
    
    def createPlayers(self):
        players = []
        for i in range(self.player_view.numberOfPlayer()):
            joueur = self.player_view.playerData()
            player = PlayerModel(joueur[0], joueur[1], joueur[2], joueur[3], joueur[4])
            self.player_view.introducePlayer(player.nom_de_famille, player.prenom, player.classement)
            players.append(player)
        return players

    def save(self):
        db = TinyDB("db.json")
        table_joueur = db.table("joueurs")
        table_joueur.truncate()	# clear the table first
        table_joueur.insert_multiple(self.player_model.serializationPlayer())
        print (table_joueur)