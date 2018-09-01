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
        print(self.__class__.__name__ + '\'s update() has been called.')
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_m:
                    self.chengeScene('Menu')
                if event.key == K_g:
                    self.chengeScene('Game')

    def draw(self):
        '''
        毎フレーム呼ばれ、シーンの描画を行う
        '''
        print(self.__class__.__name__ + '\'s draw() has been called.')

    def cheangeScene(scene):
        '''
        シーンの切り替えを行う関数

        Parameters
        ----------
        scene : string
            切り替えたいシーン名
        '''
        SceneManager.setScene(scene)

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
