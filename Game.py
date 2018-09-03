import json
import pygame
from pygame.locals import *
from IScene import *

class Game(IScene):
    '''
    メニュー画面を担当するクラス
    '''
    def __init__(self, scriptName = 'Script1.json', scriptStartLineNumber = 1):
        with open('scripts/' + scriptName, 'r') as jsonScript:
            self.dictScript = json.load(jsonScript)

    def Save(self):
        pass

    def Load(self):
        pass
