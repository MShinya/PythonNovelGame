import sys
import pygame
from pygame.locals import *
import SceneManager


class IScene():
    '''
    すべてのシーンクラスの基底クラス

    Attributes
    ----------
    DrawList : list
        描画すべき画像、文字列のリスト
    '''
    DrawList = []
    
    def __init__(self):
        print(self.__class__.__name__ + '\'s __init__() has been called.')

    def update(self):
        '''
        毎フレーム呼ばれ、シーンの更新を行う
        '''
        pass

    def draw(self):
        '''
        毎フレーム呼ばれ、シーンの描画を行う
        '''
        pass
    def eventProcess(self):
        '''
        毎フレーム呼ばれ、シーンのイベント処理を行う
        '''
        pass

    def cheangeScene(scene):
        '''
        シーンの切り替えを行う関数

        Parameters
        ----------
        scene : string
            切り替えたいシーン名
        '''
        SceneManager.setScene(scene)
        
    def isMouseOver(x, y, width, height):
        '''
        マウスオーバーしているかを返します
        '''
        mousepos = pygame.mouse.get_pos()
        if x <= mousepos[0] <= x + width and y <= mousepos[1] <= y + height:
            return True
        else:
            return False

    @classmethod
    def setScreen(cls, screen):
        '''
        スクリーンを追加する関数
        ゲーム全体の初期化時に一度だけ呼ばれる

        Parameters
        ----------
        screen : pygame.display.set_mode(GameSettings.WindowSize)
            追加するスクリーン
        '''
        cls.screen = screen
