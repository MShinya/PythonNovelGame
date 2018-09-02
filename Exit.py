import sys
import pygame
from pygame.locals import *
from IScene import *

class Exit(IScene):
    '''
    メニュー画面を担当するクラス
    '''
    def update(self):
        pygame.quit()
        sys.exit()

