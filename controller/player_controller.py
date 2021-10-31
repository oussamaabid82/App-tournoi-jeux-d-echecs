from tinydb import TinyDB
from models.player_model import PlayerModel
from models.tour_model import players_list
from view.player_view import PlayerView




class PlayerController:
    def __init__(self):
        pass

    def playerCreation(self):
        for i in range(PlayerView.numberOfPlayer(self)):
            joueur =PlayerView.playerData(self)
            creation = PlayerModel(joueur[0], joueur[1], joueur[2], joueur[3], joueur[4])
            PlayerView.introducePlayer(self, creation.nom_de_famille, creation.prenom, creation.classement)
            players_list.append([creation, creation.classement])
    
    def save(self):
        db = TinyDB("db.json")
        table_joueur = db.table("joueurs")
        table_joueur.truncate()	# clear the table first
        table_joueur.insert_multiple(self.serialisation_joueur)
        return table_joueur