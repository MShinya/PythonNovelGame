import IScene
# from Game import Game
import SceneManager


class Save(IScene.IScene):
    '''
    セーブを担当するクラス
    '''
    def __init__(self):
        pass

    def update(self):
        # Game.Save()
        SceneManager.SceneList['Game'].Save()
        SceneManager.setScene('Game')
