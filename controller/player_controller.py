from tinydb import TinyDB
from models.player_model import PlayerModel
from view.player_view import PlayerView


class PlayerController:
    players_list_serialized = []
    def __init__(self):
        self.player_view = PlayerView()
        self.player_model = PlayerModel()

    def createPlayers(self):
        players = []
        for i in range(self.player_view.numberOfPlayer()):
            joueur = self.player_view.playerData()
            self.player_model.__init__(joueur[0], joueur[1], joueur[2], joueur[3], joueur[4])
            self.player_view.introducePlayer(
                                            self.player_model.nom_de_famille, self.player_model.prenom,
                                            self.player_model.classement
                                            )
            players.append(self.player_model)
            self.players_list_serialized.append(self.player_model.serializationPlayer())
        return players

    def save(self):
        
        db = TinyDB("save/players/db.json")
        players_table  = db.table("players")
        players_table .truncate()  # clear the table first
        for player_serialized in self.players_list_serialized:
            players_table .insert(player_serialized)
