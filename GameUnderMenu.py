import pygame
import IScene
import GameSettings
import SceneManager


class GameUnderMenu(IScene.IScene):
    flameNum = 0

    def __init__(self):
        self.MenuList = [
            ('Q-SAVE', 'Exit'),
            ('Q-LOAD', 'Exit'),
            ('SAVE', 'Save'),
            ('LOAD', 'Exit'),
            ('SKIP', 'Exit'),
            ('AUTO', 'Exit'),
            ('LOG', 'Exit'),
            ('BACK', 'Exit'),
            ('CONFIG', 'Exit')
        ]
        self.drawList = []
        for i in range(len(self.MenuList)):
            if i == 0:
                self.drawList.append(self.Menus(self.MenuList[i][0], 300, self.MenuList[i][1]))
            else:
                self.drawList.append(self.Menus(self.MenuList[i][0], self.drawList[i - 1].pos[0] + self.drawList[i - 1].size[0] + 20, self.MenuList[i][1]))

    def draw(self):
        self.flameNum += 1
        SceneManager.getBeforeScene().draw()
        for D in self.drawList:
            D.draw()

    def eventProcess(self):
        for D in self.drawList:
            D.eventProcess()

    class Menus():
        '''
        メニュー画面のメニューを担当するクラス
        '''
        def __init__(self, text, x, scene):
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
            self.textSurf = GameSettings.UnderMenuFont.render(text, True, (0, 0, 0))
            self.mouseOverTextSurf = GameSettings.UnderMenuFont.render(text, True, (200, 37, 50))
            self.mouseOverFlag = False
            self.text = text
            self.size = (self.textSurf.get_width(), self.textSurf.get_height())
            self.pos = [x, 0]
            self.scene = scene

        def eventProcess(self):
            '''
            メニューがマウスオーバーされた時の動作
            '''
            if GameUnderMenu.isMouseOver(self.pos[0], self.pos[1], self.size[0], self.size[1]):
                self.mouseOverFlag = True
                pygame.event.get()
                if pygame.mouse.get_pressed()[0]:
                        GameUnderMenu.cheangeScene(self.scene)
            elif pygame.mouse.get_pos()[1] < self.pos[1]:
                GameUnderMenu.cheangeScene('Game')
            else:
                self.mouseOverFlag = False

        def draw(self):
            self.pos[1] = 690 - min(int(GameUnderMenu.flameNum / 100), self.size[1])
            if self.mouseOverFlag:
                GameUnderMenu.screen.blit(self.mouseOverTextSurf, self.pos)
            else:
                GameUnderMenu.screen.blit(self.textSurf, self.pos)
