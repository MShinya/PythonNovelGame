import json
import pygame
from pygame.locals import *
from IScene import *
from Charactors import Charactors
from MessageWindow import MessageWindow

class Game(IScene):
    '''
    メニュー画面を担当するクラス
    '''
    def __init__(self, scriptName = 'Script1.json', scriptStartLineNumber = 1):
        with open('scripts/' + scriptName, 'r') as jsonScript:
            self.dictScript = json.load(jsonScript)
        self.scriptName = scriptName
        self.chapterName = ""
        self.scriptStartLineNumber = scriptStartLineNumber
        self.chapterNumber = self.chapterName + str(scriptStartLineNumber).zfill(3)

    def update(self):
        self.chapter = self.dictScript[self.chapterNumber]
        if "background_img" in self.chapter:
            self.background_img = pygame.image.load(self.chapter["background_img"])
        if "BGM" in self.chapter:
            self.BGM = pygame.mixer.music.load(self.chapter["BGM"])
        self.charactor_img = Charactors.update(self.chapter)
        self.messageWindow = MessageWindow.update(self.chapter)
        Game.eventCheck()

    def draw(self):
        self.screen.blit(self.background_img, (0, 0))

    def eventProcess(self):
        pass

    @classmethod
    def eventCheck(cls):
        pass

    def Save(self):
        pass

    def Load(self):
        pass
