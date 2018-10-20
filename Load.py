# import pygame
import SceneManager
import IScene
import json
import Game


class Load(IScene.IScene):
    def __init__(self) -> None:
        pass

    def Load(self) -> None:
        with open('savedata/save.json', 'r') as savefile:
            dictSavefile = json.load(savefile)
            SceneManager.SceneList['Game'] = Game.Game(saveData=dictSavefile)

    def update(self):
        SceneManager.setScene('Game')
