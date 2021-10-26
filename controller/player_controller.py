from models.player_model import Player
from view.player_view import PlayerView

player_list = []
class ControllerPlayer:
    def __init__(self):
        self.PlayerView = PlayerView()

    def playerCreation(self):
        for i in range(self.PlayerView.numberOfPlayer()):
            joueur = self.PlayerView.playerData()
            creation = Player(joueur[0], joueur[1], joueur[2], joueur[3], joueur[4])
            self.PlayerView.introducePlayer(joueur[0], joueur[1], joueur[4])
            player_list.append(creation)   
           
