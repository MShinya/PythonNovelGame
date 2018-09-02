import pygame
from pygame.locals import *
from IScene import *
import GameSettings

class Menu(IScene):
    '''
    メニュー画面を担当するクラス
    メニュー画面にはタイトルとメニューが含まれる
    '''

    #メニューのリスト
    MenuText = [
            ('はじめから', 'Game'),
            ('つづきから', 'Game'),
            ('せってい', 'Game'),
            ('クレジット', 'Game'),
            ('やめる', 'Exit')
            ]

    class Menus():
        '''
        メニュー画面のメニューを担当するクラス
        '''
        def __init__(self, text, x, y, scene):
            '''
            Parameter
            ---------
            text : string
                メニューに表示する文字列
            x : int
                文字列の左上のx座標
            y : int
                文字列の左上のy座標
            scene : string
                押した時に切り替えるシーン
            '''
            self.textSurf = GameSettings.MenuFont.render(text, True, (0, 0, 0))
            self.mouseOverTextSurf = GameSettings.MenuFont.render(text, True, (200, 37, 50))
            self.mouseOverFlag = False
            self.text = text
            self.size = (self.textSurf.get_width(), self.textSurf.get_height())
            self.pos = (x, y)
            self.scene = scene

        def update(self):
            '''
            メニューがマウスオーバーされた時の動作
            '''
            if Menu.isMouseOver(self.pos[0], self.pos[1], self.size[0], self.size[1]):
                self.mouseOverFlag = True
               # for event in pygame.event.get():
               #     if event.type == MOUSEBUTTONDOWN and event.button == 1:
                pygame.event.get()
                if pygame.mouse.get_pressed()[0]:
                        Menu.cheangeScene(self.scene)
            else:
                self.mouseOverFlag = False

        def draw(self):
            if self.mouseOverFlag:
                Menu.screen.blit(self.mouseOverTextSurf, self.pos)
            else:
                Menu.screen.blit(self.textSurf, self.pos)


    def __init__(self):
        self.DrawList.append(pygame.image.load('images/sougen.jpg'))
        self.MenuList = []
        for i in range(len(self.MenuText)):
            self.MenuList.append(self.Menus(self.MenuText[i][0], 100, 300 + 80 * i, self.MenuText[i][1]))

    def isMouseOver(x, y, width, height):
        '''
        マウスオーバーしているかを返します
        '''
        mousepos = pygame.mouse.get_pos()
        if x <= mousepos[0] <= x + width and y <= mousepos[1] <= y + height:
            return True
        else:
            return False

    def drawTitle(self):
        '''
        ゲームのタイトルを作成、描画する関数
        '''
        title = GameSettings.TitleFont.render('ノベルゲームだよ', True, (0, 0, 0))
        self.screen.blit(title, (GameSettings.WindowSize[0] // 2 - title.get_width() // 2, 50))

    def update(self):
        for M in self.MenuList:
            M.update()

    def draw(self):
        for img in self.DrawList:
            self.screen.blit(img, (0, 0))
        self.drawTitle()
        for M in self.MenuList:
            M.draw()
